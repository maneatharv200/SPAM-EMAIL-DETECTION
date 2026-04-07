def generate_explanation(text, label):

    if label == "SPAM":

        return (
            "This email is classified as SPAM "
            "because it contains suspicious patterns "
            "or promotional content."
        )

    else:

        return (
            "This email is classified as HAM "
            "because it appears to be normal communication."
        )