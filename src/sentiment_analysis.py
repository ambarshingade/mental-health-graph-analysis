import pandas as pd
from textblob import TextBlob
import os

# Set paths
PROCESSED_DATA_DIR = "../data/processed/"
RESULTS_DIR = "../results/"
os.makedirs(RESULTS_DIR, exist_ok=True)

# Get all cleaned files
files = [f for f in os.listdir(PROCESSED_DATA_DIR) if f.endswith("_cleaned.csv")]

at_risk_users = []

print("Performing sentiment analysis on user posts...")

for file in files:
    file_path = os.path.join(PROCESSED_DATA_DIR, file)
    df = pd.read_csv(file_path)

    # Ensure required columns exist
    if "author" not in df.columns or "post" not in df.columns:
        print(f"⚠ Skipping {file} - Missing required columns.")
        continue

    # Compute sentiment scores
    df["sentiment"] = df["post"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

    # Identify at-risk users (Negative Sentiment)
    df_at_risk = df[df["sentiment"] < -0.5][["author", "sentiment"]]
    at_risk_users.append(df_at_risk)

# Combine all at-risk users
df_at_risk_all = pd.concat(at_risk_users, ignore_index=True)

# Save results
at_risk_file = os.path.join(RESULTS_DIR, "at_risk_users.csv")
df_at_risk_all.to_csv(at_risk_file, index=False)

print(f"At-risk users identified and saved in {at_risk_file}")
