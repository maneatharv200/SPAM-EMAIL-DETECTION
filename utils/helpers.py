import re
import string

def clean_text(text):

    text = str(text).lower()

    # remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove numbers
    text = re.sub(r"\d+", "", text)

    # remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    return text.strip()