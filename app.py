import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# Load the iris dataset
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=["species"])

# Train the model
rfc = RandomForestClassifier()
rfc.fit(X, y)

# Define the app
def app():
    st.write("""
    # Iris Flower Prediction App
    This app predicts the **Iris flower** species!
    """)

    # Define user input parameters
    st.sidebar.header('User Input Parameters')
    def user_input_features():
        sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
        sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
        petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
        petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
        data = {'sepal_length': sepal_length,
                'sepal_width': sepal_width,
                'petal_length': petal_length,
                'petal_width': petal_width}
        features = pd.DataFrame(data, index=[0])
        return features

    # Get user input
    df = user_input_features()

    # Display user input
    st.subheader('User Input parameters')
    st.write(df)

    # Make predictions
    prediction = rfc.predict(df)
    prediction_proba = rfc.predict_proba(df)

    # Display prediction
    st.subheader('Prediction')
    st.write(iris.target_names[prediction])

    # Display prediction probabilities
    st.subheader('Prediction Probability')
    st.write(prediction_proba)

# Run the app
if __name__ == '__main__':
    app()
