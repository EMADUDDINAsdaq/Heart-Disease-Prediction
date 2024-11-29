# Heart Disease Prediction

This project is a machine learning-based application for predicting heart disease based on various health parameters. The model is built using a dataset of patient health features, and it predicts whether a person is at risk of heart disease.

## Features

The system takes the following health features as inputs:

- **Age**: Age of the patient
- **Sex**: Gender of the patient (1 for male, 0 for female)
- **cp**: Chest pain type (0-3)
- **trestbps**: Resting blood pressure (in mm Hg)
- **chol**: Serum cholesterol level (in mg/dl)
- **fbs**: Fasting blood sugar (1 if greater than 120 mg/dl, 0 otherwise)
- **restecg**: Resting electrocardiographic results (0-2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise-induced angina (1 for yes, 0 for no)
- **oldpeak**: Depression induced by exercise relative to rest
- **slope**: Slope of the peak exercise ST segment (0-2)
- **ca**: Number of major vessels colored by fluoroscopy (0-3)
- **thal**: Thalassemia type (3 for normal, 6 for fixed defect, 7 for reversable defect)

The model predicts the presence of heart disease or no heart disease.
 Dataset

The dataset used for training the model is from Kaggle:

- **Dataset**: [Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

## Installation

## Project Structure

The project consists of the following components:

- **app.py**: Flask application file, which serves as the backend. It handles input data, makes predictions using the machine learning model, and returns the results to the user.
- **model.pkl**: The trained machine learning model saved using `pickle`. This model is used for making predictions.
- **static/**: Folder containing static files like CSS styles for the frontend.
- **templates/**: Folder containing HTML templates for the frontend.
- **README.md**: Project documentation.

## How to Run

### 1. Clone the Repository
Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/EMADUDDINAsdaq/Heart-Disease-Prediction.git

### Key Sections in the README:
1. **Project Description**: Explains the purpose of the project.
2. **Features**: Lists the input features required by the model.
3. **Project Structure**: Describes the folder structure of the project.
4. **How to Run**: Instructions on how to clone, install dependencies, and run the app.
5. **Technologies Used**: Lists the libraries and technologies used.
6. **License**: Information about the project's license.
7. **Acknowledgments**: Credits to datasets, libraries, or frameworks used.

You can copy this README into a `README.md` file in the root of your project directory. Let me know if you need any adjustments!
