
import csv
import re
import urllib.request
import zipfile
import io
from collections import Counter

# ---------------------------------
# 1. DATASET CONFIGURATION
# ---------------------------------

DATASET_URL = (
    "https://archive.ics.uci.edu/static/"
    "public/228/sms+spam+collection.zip"
)

DATASET_FILE = "SMSSpamCollection"
OUTPUT_FILE = "processed_sms.csv"

STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "am", "be", "been", "being", "to", "of", "in",
    "on", "at", "for", "from", "with", "by", "as",
    "and", "or", "but", "if", "then", "so", "than",
    "this", "that", "these", "those", "it", "its",
    "i", "you", "he", "she", "we", "they", "me",
    "my", "your", "his", "her", "our", "their",
    "them", "us", "do", "does", "did", "have",
    "has", "had", "can", "could", "will", "would",
    "shall", "should", "may", "might", "must",
    "not", "no", "yes", "what", "which", "who",
    "when", "where", "how", "why", "all", "any",
    "some", "more", "most", "very", "just", "now"
}


# ---------------------------------
# 2. DOWNLOAD AND LOAD DATASET
# ---------------------------------

def load_dataset():

    print("\nDownloading SMS Spam Dataset...")

    try:
        request = urllib.request.Request(
            DATASET_URL,
            headers={"User-Agent": "Python Spam Detector"}
        )

        with urllib.request.urlopen(
            request, timeout=30
        ) as response:
            zip_data = response.read()

        with zipfile.ZipFile(io.BytesIO(zip_data)) as archive:

            with archive.open(DATASET_FILE) as file:
                content = file.read().decode(
                    "utf-8", errors="replace"
                )

        messages = []

        for row in csv.reader(
            io.StringIO(content), delimiter="\t"
        ):
            if len(row) >= 2:
                label = row[0].strip().lower()
                message = row[1].strip()

                if label in ("spam", "ham") and message:
                    messages.append({
                        "label": label,
                        "message": message
                    })

        print("Dataset loaded successfully!")
        return messages

    except Exception as error:
        print("Dataset loading failed:", error)
        print(
            "Download the dataset manually from UCI "
            "and extract SMSSpamCollection into this folder."
        )
        return []


# ---------------------------------
# 3. TEXT PREPROCESSING
# ---------------------------------

def clean_text(message):

    # Convert to lowercase
    message = message.lower()

    # Remove URLs
    message = re.sub(
        r"http\S+|www\.\S+", " ", message
    )

    # Remove numbers and punctuation
    message = re.sub(
        r"[^a-z\s]", " ", message
    )

    # Split into words
    words = message.split()

    # Remove stopwords
    cleaned_words = [
        word for word in words
        if word not in STOPWORDS
    ]

    return " ".join(cleaned_words)


# ---------------------------------
# 4. PREPROCESS ALL MESSAGES
# ---------------------------------

def preprocess_messages(messages):

    processed = []

    for item in messages:

        cleaned = clean_text(item["message"])

        processed.append({
            "label": item["label"],
            "original_message": item["message"],
            "cleaned_message": cleaned
        })

    return processed


# ---------------------------------
# 5. EXPLORE DATA PATTERNS
# ---------------------------------

def analyze_messages(messages):

    spam_messages = [
        item for item in messages
        if item["label"] == "spam"
    ]

    ham_messages = [
        item for item in messages
        if item["label"] == "ham"
    ]

    spam_words = Counter()
    ham_words = Counter()

    for item in spam_messages:
        spam_words.update(
            item["cleaned_message"].split()
        )

    for item in ham_messages:
        ham_words.update(
            item["cleaned_message"].split()
        )

    print("\n" + "=" * 50)
    print("SPAM DETECTION - DATA ANALYSIS")
    print("=" * 50)

    total = len(messages)

    print("Total messages:", total)
    print("Spam messages:", len(spam_messages))
    print("Ham messages:", len(ham_messages))

    if total:
        print(
            "Spam percentage:",
            round(len(spam_messages) / total * 100, 2),
            "%"
        )

    print("\nTop 10 Spam Words:")

    for word, count in spam_words.most_common(10):
        print(word, ":", count)

    print("\nTop 10 Ham Words:")

    for word, count in ham_words.most_common(10):
        print(word, ":", count)

    print("=" * 50)


# ---------------------------------
# 6. SAVE CLEANED DATASET
# ---------------------------------

def save_processed_data(messages):

    with open(
        OUTPUT_FILE, "w", newline="", encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "label",
                "original_message",
                "cleaned_message"
            ]
        )

        writer.writeheader()
        writer.writerows(messages)

    print("\nCleaned dataset saved to", OUTPUT_FILE)


# ---------------------------------
# 7. MAIN PROGRAM
# ---------------------------------

def main():

    print("\nSMART SPAM DETECTOR - PART 1")
    print("-" * 50)

    raw_messages = load_dataset()

    if not raw_messages:
        print("Cannot continue without dataset.")
        return

    print("\nPreprocessing messages...")

    processed_messages = preprocess_messages(
        raw_messages
    )

    print("Text preprocessing completed!")

    print("\nSample Before and After Cleaning:")

    for item in processed_messages[:5]:

        print("\nLabel:", item["label"])
        print("Original:", item["original_message"])
        print("Cleaned :", item["cleaned_message"])

    analyze_messages(processed_messages)

    save_processed_data(processed_messages)

    print("\nProject completed successfully!")


if __name__ == "__main__":
    main()
