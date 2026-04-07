import re

SUSPICIOUS_DOMAINS = [
    "bit.ly",
    "tinyurl",
    "goo.gl",
    "t.co"
]


def extract_links(text):

    pattern = r"http[s]?://\S+"

    return re.findall(pattern, text)


def check_links(text):

    links = extract_links(text)

    suspicious = []

    for link in links:

        for domain in SUSPICIOUS_DOMAINS:

            if domain in link:

                suspicious.append(link)

    return {

        "links": links,

        "suspicious_links": suspicious,

        "count": len(suspicious)

    }