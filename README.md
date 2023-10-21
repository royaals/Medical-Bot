## Medical Health Advisor
The services offered by our platform cater specifically to the needs of elderly individuals. We provide:

1. *Disease Prediction*: Early detection of health issues through cutting-edge algorithms.

2. *Doctor Appointment Booking*: Simplified and accessible healthcare appointments.

3. *Mental Health Chatbots*: Emotional support to address loneliness and mental health concerns.

4. *Medical Chatbots*: Reliable information and guidance for health-related queries.

These services are designed to empower seniors, improve their quality of life, and enhance their overall healthcare and well-being.

## Hosting
Hosted Link- https://royaals.github.io/med-advisor/

## Demo

Youtube link: https://www.youtube.com/watch?v=6p0oHkE6j1E

# Medical Chatbot

This is a Flask application that uses OpenAI's GPT-3.5-turbo model to power a medical chatbot. The chatbot strictly provides information within the medical domain.

## Setup

1. Install the required Python packages: 
```bash
pip install flask openai python-dotenv
```
2. Set your OpenAI API key in an environment variable:
```bash
export OPENAI_API_KEY='your-api-key'
```

## Usage

1. Run the Flask application:
```bash
python app.py
```
2. Navigate to the root URL to access the chatbot interface.
3. Send POST requests to the "/api" endpoint with a JSON payload containing a "message" key to interact with the chatbot.

# Streamlit Application for Naive Bayes Classifier

This is a Streamlit application that uses a Multinomial Naive Bayes classifier for some sort of prediction task.

## Setup

1. Install the required Python packages: 
```bash
pip install streamlit numpy pandas scikit-learn
```
2. Set your Google Cloud project ID and location in environment variables:
```bash
export PROJECT_ID='your-project-id'
export LOCATION='your-location'
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```
2. Use the interface to interact with the Naive Bayes classifier.


