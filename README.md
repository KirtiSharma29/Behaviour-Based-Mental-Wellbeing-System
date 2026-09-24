# Behaviour-Based-Mental-Wellbeing-System
Behaviour-based ML system for analyzing emotional states and providing suggestions to improve the mental well-being of special children.
# Behaviour-Based Analysis and Suggestion System to Improve Mental Well-Being of Special Children
📌 Project Overview

The **Behaviour-Based Analysis and Suggestion System** is a machine learning-based application designed to analyze behavioural patterns of special children and identify their possible emotional states. Based on the predicted state and behavioural ratings, the system provides suitable suggestions to support and improve mental well-being.

The system uses **Machine Learning, Flask, Python, HTML, CSS, and JavaScript** to provide an interactive web-based platform for behaviour analysis and suggestion generation.

🎯 Objectives

- Analyze behavioural patterns of special children.
- Predict possible emotional states using machine learning.
- Provide a simple and interactive interface for entering behavioural information.
- Generate suitable suggestions based on the prediction.
- Support caregivers and users in understanding behavioural and emotional patterns.
- Provide a structured approach for monitoring behavioural changes.

🚀 Key Features

- Behaviour-based emotional state prediction
- Machine learning-based analysis
- SVM-based prediction model
- Rating-based input system
- Suggestion generation
- Flask web application
- Interactive web interface
- Prediction history
- Report generation
- Dataset-based model training

🧠 Machine Learning Model

The project uses **Support Vector Machine (SVM)** for classification.

Other machine learning algorithms were considered during the development and evaluation process, including:

- Support Vector Machine (SVM)
- Random Forest
- Decision Tree
- K-Nearest Neighbors (KNN)

SVM was selected for the final prediction system based on the evaluation performed during the project.

📊 Dataset

The project uses a behavioural dataset containing approximately **20,000 records**.

The dataset contains behavioural attributes used for training the machine learning model and predicting emotional states.

### Dataset File

```text
special_children_behavior_dataset_20k.csv

🔄 System Workflow
User Behavioural Input
        ↓
Data Preprocessing
        ↓
Feature Processing
        ↓
Machine Learning Model
        ↓
SVM Prediction
        ↓
Emotional State
        ↓
Suggestion Generation
        ↓
Mental Well-Being Support

🛠️ Technologies Used
Programming Language
Python
Machine Learning
Scikit-learn
Support Vector Machine (SVM)
Pandas
NumPy
Web Technologies
HTML
CSS
JavaScript
Backend
Flask
Development Tools
Jupyter Notebook
Python
GitHub

Project Structure
Behaviour-Based-Mental-Wellbeing-System/
│
├── app.py
├── run.py
├── config.py
├── ml.py
├── reports.py
├── requirements.txt
│
├── Child Behaviour.ipynb
├── special_children_behavior_dataset_20k.csv
├── best_emotion_model.pkl
│
├── templates/
├── static/
├── database/
└── utils/


▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/KirtiSharma29/Behaviour-Based-Mental-Wellbeing-System.git
2. Open the project folder
cd Behaviour-Based-Mental-Wellbeing-System
3. Install the required packages
pip install -r requirements.txt
4. Run the Flask application
python app.py
or, depending on the project configuration:
python run.py
5. Open the application
Open the local Flask URL shown in the terminal, usually:
http://127.0.0.1:5000/


📈 Results
The machine learning model was evaluated during development, and the SVM model achieved approximately 90% accuracy in the reported project evaluation.
The system provides an emotional-state prediction followed by appropriate suggestions intended to support mental well-being.

🔮 Future Scope
Integration with real-time behavioural monitoring.
Improved prediction using larger and more diverse datasets.
Integration of additional machine learning and deep learning models.
Mobile application development.
Voice and facial-expression-based analysis.
Personalized recommendation generation.
Integration with caregiver monitoring systems.


⚠️ Disclaimer
This project is developed for academic and research purposes. The predictions and suggestions provided by the system should not be considered a medical diagnosis or a replacement for professional assessment.


👩‍💻 Author
Kirti Sharma
Master of Computer Applications (MCA)
VidyaVardhaka College of Engineering, Mysuru
