# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# import pickle

# print("Loading cleaned dataset...")

# # Load dataset
# df = pd.read_csv("dataset/cleaned_dataset.csv")

# print("Dataset loaded successfully!")

# # Features and labels
# X = df["clean_text"]
# y = df["label"]

# print("Splitting dataset...")

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# print("Vectorizing text...")

# # Convert text to numbers
# vectorizer = TfidfVectorizer(max_features=5000)

# X_train_vec = vectorizer.fit_transform(X_train)
# X_test_vec = vectorizer.transform(X_test)

# print("Training Random Forest model...")

# # Train model
# model = RandomForestClassifier()

# model.fit(X_train_vec, y_train)

# print("Model trained successfully!")

# # Test model
# y_pred = model.predict(X_test_vec)

# accuracy = accuracy_score(y_test, y_pred)

# print("Model Accuracy:", accuracy)

# # Save model
# pickle.dump(model, open("model/model.pkl", "wb"))

# # Save vectorizer
# pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

# print("Model saved as model/model.pkl")
# print("Vectorizer saved as model/vectorizer.pkl")






import pandas as pd
import joblib
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model():

    print("Loading dataset...")

    df = pd.read_csv("dataset/cleaned_dataset.csv")

    X = df["clean_text"]

    y = df["label_num"]

    print("Applying TF-IDF...")

    vectorizer = TfidfVectorizer(
        max_features=10000,
        ngram_range=(1,2),
        min_df=2
    )

    X_tfidf = vectorizer.fit_transform(X)

    print("Splitting dataset...")

    X_train, X_test, y_train, y_test = train_test_split(
        X_tfidf,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("Training model...")

    model = MultinomialNB(alpha=0.1)

    model.fit(X_train, y_train)

    print("Evaluating model...")

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("Accuracy:", accuracy * 100)

    os.makedirs("model", exist_ok=True)

    joblib.dump(
        model,
        "model/model.pkl"
    )

    joblib.dump(
        vectorizer,
        "model/vectorizer.pkl"
    )

    print("Model saved successfully!")


if __name__ == "__main__":
    train_model()