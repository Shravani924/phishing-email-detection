import pandas as pd
import re
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# -------- TEXT CLEANING FUNCTION -------- #
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# -------- LOAD DATA -------- #
df = pd.read_csv("data/emails.csv")

# Convert labels
df['label'] = df['Email Type'].map({
    'Safe Email': 0,
    'Phishing Email': 1
})

# Clean text
df['clean_text'] = df['Email Text'].apply(clean_text)

# -------- TF-IDF -------- #
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['clean_text'])
y = df['label']

# -------- TRAIN TEST SPLIT -------- #
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------- TRAIN MODEL -------- #
model = LogisticRegression()
model.fit(X_train, y_train)

# -------- EVALUATE -------- #
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -------- SAVE MODEL -------- #
with open("model/phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved successfully.")