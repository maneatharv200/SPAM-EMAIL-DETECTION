# import pandas as pd
# import re

# # File path
# file_path = "dataset/spam_ham_dataset.csv"

# print("Loading dataset...")

# # Load dataset
# df = pd.read_csv(file_path)

# print("Dataset loaded successfully!")
# print("Total rows:", len(df))

# # Clean text function
# def clean_text(text):

#     text = str(text).lower()

#     # Remove special characters
#     text = re.sub(r"[^a-zA-Z\s]", "", text)

#     return text

# print("Cleaning text...")

# # Apply cleaning
# df["clean_text"] = df["text"].apply(clean_text)

# # Save cleaned dataset
# output_path = "dataset/cleaned_dataset.csv"

# df.to_csv(output_path, index=False)

# print("Cleaning completed!")
# print("Saved cleaned dataset at:", output_path)


import pandas as pd
import sys
import os

# Fix import path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from utils.helpers import clean_text


def clean_dataset():

    print("Loading raw dataset...")

    df = pd.read_csv(
        "dataset/spam_ham_dataset.csv"
    )

    print("Cleaning text...")

    df["clean_text"] = df["text"].apply(
        clean_text
    )

    df["label_num"] = df["label"].map({
        "spam": 1,
        "ham": 0
    })

    df.to_csv(
        "dataset/cleaned_dataset.csv",
        index=False
    )

    print("Dataset cleaned successfully!")


if __name__ == "__main__":
    clean_dataset()