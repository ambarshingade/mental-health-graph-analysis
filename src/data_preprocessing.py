import pandas as pd
import os

# Set paths
RAW_DATA_DIR = "/home/ambarshingade/mental_health_analysis/data/raw"
PROCESSED_DATA_DIR = "/home/ambarshingade/mental_health_analysis/data/processed"
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# List of datasets
datasets = [
    "depression_2018_features_tfidf_256.csv",
    "depression_2019_features_tfidf_256.csv",
    "depression_post_features_tfidf_256.csv",
    "depression_pre_features_tfidf_256.csv",
    "anxiety_2018_features_tfidf_256.csv",
    "anxiety_2019_features_tfidf_256.csv",
    "anxiety_post_features_tfidf_256.csv",
    "anxiety_pre_features_tfidf_256.csv",
    "suicidewatch_2018_features_tfidf_256.csv",
    "suicidewatch_2019_features_tfidf_256.csv",
    "suicidewatch_post_features_tfidf_256.csv",
    "suicidewatch_pre_features_tfidf_256.csv",
    "ptsd_2018_features_tfidf_256.csv",
    "ptsd_2019_features_tfidf_256.csv",
    "ptsd_post_features_tfidf_256.csv",
    "ptsd_pre_features_tfidf_256.csv",
    "socialanxiety_2018_features_tfidf_256.csv",
    "socialanxiety_2019_features_tfidf_256.csv",
    "socialanxiety_post_features_tfidf_256.csv",
    "socialanxiety_pre_features_tfidf_256.csv",
    "mentalhealth_2018_features_tfidf_256.csv",
    "mentalhealth_2019_features_tfidf_256.csv",
    "mentalhealth_post_features_tfidf_256.csv",
    "mentalhealth_pre_features_tfidf_256.csv"
]

# Process each dataset
for file in datasets:
    raw_file_path = os.path.join(RAW_DATA_DIR, file)
    processed_file_path = os.path.join(PROCESSED_DATA_DIR, file.replace("features_tfidf_256", "cleaned"))
    
    if os.path.exists(raw_file_path):
        df = pd.read_csv(raw_file_path)
        
        # Perform any required preprocessing (if needed)
        df = df.dropna()  # Removing missing values
        
        # Save processed file
        df.to_csv(processed_file_path, index=False)
        print(f"✅ Processed and saved: {processed_file_path}")
    else:
        print(f"❌ File not found: {raw_file_path}")

print("🎉 Processing Complete! 24 files processed.")
