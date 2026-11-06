
# 🛡️ Smart Spam Detector – Part 1

A Python mini-project that collects, cleans and analyzes SMS messages
to understand spam and non-spam patterns.

## Project Objective

Prepare SMS text data for a future machine-learning spam
classification model.

## Features

- Load the SMS Spam Collection dataset.
- Separate spam and legitimate messages.
- Convert text into lowercase.
- Remove URLs, punctuation and numbers.
- Remove common English stopwords.
- Identify frequently occurring words.
- Analyze spam and ham message patterns.
- Export cleaned data into a CSV file.

## Technologies

- Python
- Regular Expressions
- CSV
- JSON-independent file processing
- Collections Counter
- UCI SMS Spam Collection Dataset

## Project Structure

smart-spam-detector/
- spam_detector.py
- requirements.txt
- README.md
- processed_sms.csv

## Dataset

Source: UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/228/sms+spam+collection

## How to Run

1. Download and extract the dataset.
2. Place SMSSpamCollection in the project folder.
3. Run:

   python spam_detector.py

## Text Preprocessing

1. Lowercase conversion
2. URL removal
3. Punctuation removal
4. Number removal
5. Stopword removal
6. Word frequency analysis

## Output

The application generates:

- Spam and ham message counts.
- Most frequent spam words.
- Most frequent ham words.
- Original and cleaned message samples.
- processed_sms.csv

## Learning Outcomes

- Dataset collection and loading.
- Text preprocessing.
- Regular expressions.
- Stopword removal.
- Word frequency analysis.
- Exploratory data analysis.

## Future Improvements

- Train a machine-learning classifier.
- Use TF-IDF vectorization.
- Detect spam messages automatically.
- Evaluate accuracy, precision, recall and F1-score.

## Project Status

Part 1: Data collection and preprocessing completed.
