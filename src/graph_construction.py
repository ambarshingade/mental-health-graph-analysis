import networkx as nx
import pandas as pd
import os
import pickle
import community  # Louvain package

# Set paths
PROCESSED_DATA_DIR = "/home/ambarshingade/mental_health_analysis/data/processed"

# Get all graph files
graph_files = [f for f in os.listdir(PROCESSED_DATA_DIR) if f.endswith("graph.gpickle")]

# Initialize an empty graph
G_combined = nx.DiGraph()

# Load and merge all graphs
for file in graph_files:
    graph_path = os.path.join(PROCESSED_DATA_DIR, file)
    with open(graph_path, "rb") as f:
        G = pickle.load(f)
        G_combined = nx.compose(G_combined, G)  # Merge graphs

print(f"Merged {len(graph_files)} graphs into one large graph with {len(G_combined.nodes)} nodes and {len(G_combined.edges)} edges.")

# Apply Google PageRank algorithm
pagerank_scores = nx.pagerank(G_combined)

# Convert to DataFrame
df_pagerank = pd.DataFrame(
    pagerank_scores.items(), columns=["author", "pagerank"]
)

# Save the user-based PageRank
df_pagerank.to_csv("../results/user_pagerank_scores.csv", index=False)
print("User-based PageRank scores saved in results/user_pagerank_scores.csv")


# Sort users by influence (highest scores first)
top_users = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)[:20]

# Save PageRank scores for further analysis
df_pagerank = pd.DataFrame(top_users, columns=["User", "PageRank"])
df_pagerank.to_csv("../results/pagerank_scores.csv", index=False)

print("PageRank computed! Top 20 Influential Users saved in results/pagerank_scores.csv")



# Convert the directed graph to an undirected graph
G_undirected = G_combined.to_undirected()

# Apply Louvain Community Detection
partition = community.best_partition(G_undirected)  # Detect communities

# Convert to DataFrame and save
df_communities = pd.DataFrame(partition.items(), columns=["User", "Community"])
df_communities.to_csv("../results/community_assignments.csv", index=False)

print("Community Detection Completed! Results saved in results/community_assignments.csv")
