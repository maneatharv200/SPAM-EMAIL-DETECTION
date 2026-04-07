# from fastapi import FastAPI
# import pickle

# # Create API
# app = FastAPI()

# print("Loading model...")

# # Load model
# model = pickle.load(open("model/model.pkl", "rb"))
# vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# print("Model loaded successfully!")

# # Prediction function
# def predict_spam(email_text):

#     text_vector = vectorizer.transform([email_text])

#     prediction = model.predict(text_vector)

#     if prediction[0] == "spam":
#         return "SPAM"
#     else:
#         return "NOT SPAM"


# # API route
# @app.get("/")
# def home():
#     return {"message": "Spam Detection API Running"}


# # Prediction route
# @app.post("/predict/")
# def predict(email: str):

#     result = predict_spam(email)

#     return {
#         "email": email,
#         "prediction": result
#     }








from fastapi import FastAPI
import sys
import os

print("Starting server...")

# Add project root path
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(BASE_DIR)

print("BASE_DIR:", BASE_DIR)

try:
    from backend.predict import predict_email
    print("predict_email imported successfully")

except Exception as e:
    print("IMPORT ERROR:", e)
    raise


app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Spam Detection API Running"
    }


@app.post("/predict")
def predict(text: str):

    try:

        result = predict_email(text)

        return result

    except Exception as e:

        return {
            "error": str(e)
        }