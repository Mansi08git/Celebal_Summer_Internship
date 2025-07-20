import streamlit as st
import pandas as pd
import numpy as np # type: ignore
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px # type: ignore

# Set page configuration
st.set_page_config(
    page_title="Iris Flower Prediction App", page_icon="🌸", layout="wide"
)


# Function to load and train the model
@st.cache_data
def load_and_train_model():
    # Load iris dataset
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model, iris.target_names


# Load the model
model, target_names = load_and_train_model()


# Main app
def main():
    st.title("🌸 Iris Flower Prediction App")
    st.write("This app predicts the type of Iris flower based on its measurements.")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Prediction", "Data Visualization"])

    if page == "Prediction":
        show_prediction_page()
    else:
        show_visualization_page()


def show_prediction_page():
    st.header("Make Predictions")

    # Create input fields
    col1, col2 = st.columns(2)

    with col1:
        sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
        sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)

    with col2:
        petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.7)
        petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.4)

    # Make prediction
    if st.button("Predict"):
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)

        # Display results
        st.success(f"Predicted Iris Type: **{target_names[prediction[0]]}**")

        # Display probability distribution
        st.write("Prediction Probabilities:")
        prob_df = pd.DataFrame(
            {"Iris Type": target_names, "Probability": prediction_proba[0]}
        )

        fig = px.bar(
            prob_df,
            x="Iris Type",
            y="Probability",
            title="Prediction Probability Distribution",
        )
        st.plotly_chart(fig)


def show_visualization_page():
    st.header("Data Visualization")

    # Load iris dataset for visualization
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["target"] = iris.target
    df["species"] = df["target"].map({i: target_names[i] for i in range(3)})

    # Feature correlation plot
    st.subheader("Feature Correlation Plot")
    fig_corr = px.scatter_matrix(
        df,
        dimensions=iris.feature_names,
        color="species",
        title="Iris Features Correlation Matrix",
    )
    st.plotly_chart(fig_corr)

    # Feature importance plot
    st.subheader("Feature Importance")
    importance_df = pd.DataFrame(
        {"Feature": iris.feature_names, "Importance": model.feature_importances_}
    )
    fig_imp = px.bar(
        importance_df,
        x="Feature",
        y="Importance",
        title="Feature Importance in Model Prediction",
    )
    st.plotly_chart(fig_imp)


if __name__ == "__main__":
    main()
