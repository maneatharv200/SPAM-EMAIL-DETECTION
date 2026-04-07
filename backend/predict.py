# import pickle

# # Load model and vectorizer
# print("Loading model...")

# model = pickle.load(open("model/model.pkl", "rb"))
# vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# print("Model loaded successfully!")

# # Prediction function
# def predict_spam(email_text):

#     # Transform text
#     text_vector = vectorizer.transform([email_text])

#     # Predict
#     prediction = model.predict(text_vector)

#     # Return result
#     if prediction[0] == "spam":
#         return "SPAM"
#     else:
#         return "NOT SPAM"


# # Test example
# if __name__ == "__main__":

#     test_email = "Let's meet tomorrow at 5 pm"

#     result = predict_spam(test_email)

#     print("Test Email:", test_email)
#     print("Prediction:", result)











import joblib
import sys
import os

# Get absolute project root
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

# Add root to Python path
sys.path.append(BASE_DIR)

from llm.link_scanner import check_links
from llm.explain import generate_explanation


# Correct absolute paths
MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "model",
    "vectorizer.pkl"
)

print("Loading model from:", MODEL_PATH)
print("Loading vectorizer from:", VECTORIZER_PATH)

# Load files
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_email(text):

    features = vectorizer.transform([text])

    prediction = model.predict(features)[0]

    prob = model.predict_proba(features)[0]

    label = "SPAM" if prediction == 1 else "HAM"

    links = check_links(text)

    explanation = generate_explanation(
        text,
        label
    )

    return {

        "label": label,

        "spam_probability":
        float(prob[1]),

        "ham_probability":
        float(prob[0]),

        "links": links,

        "explanation": explanation

    }