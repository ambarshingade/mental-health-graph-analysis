import pandas as pd
import os

# Set paths
RESULTS_DIR = "../results/"
os.makedirs(RESULTS_DIR, exist_ok=True)

# Load at-risk users and PageRank scores
at_risk_file = os.path.join(RESULTS_DIR, "at_risk_users.csv")
pagerank_file = os.path.join(RESULTS_DIR, "user_pagerank_scores.csv")  # Ensure correct PageRank file

if os.path.exists(at_risk_file) and os.path.exists(pagerank_file):
    # Load the datasets
    df_at_risk = pd.read_csv(at_risk_file)
    df_pagerank = pd.read_csv(pagerank_file)

    # Ensure column names are correct
    if "author" not in df_at_risk.columns:
        raise KeyError("`at_risk_users.csv` is missing the `author` column.")
    if "author" not in df_pagerank.columns:
        raise KeyError("`user_pagerank_scores.csv` is missing the `author` column.")

    # Merge both datasets based on users
    df_critical_users = df_at_risk.merge(
        df_pagerank, on="author", how="inner"
    )

    # Save the final list of at-risk influential users
    critical_users_file = os.path.join(RESULTS_DIR, "critical_at_risk_users.csv")
    df_critical_users.to_csv(critical_users_file, index=False)

    print(f"Critical At-Risk Users (High PageRank + Negative Sentiment) saved in {critical_users_file}")

else:
    print("Missing required files: at_risk_users.csv or user_pagerank_scores.csv")
    print("Make sure you have run sentiment analysis and PageRank computation first.")
