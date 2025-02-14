import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os
import pickle

# Set paths
PROCESSED_DATA_DIR = "/home/ambarshingade/mental_health_analysis/data/processed"
SENTIMENT_FILE = "../results/user_sentiment_scores.csv"  # Ensure this file exists
OUTPUT_IMAGE = "../results/graph_with_sentiment.png"

# Load the graph
graph_files = [f for f in os.listdir(PROCESSED_DATA_DIR) if f.endswith("graph.gpickle")]
G_combined = nx.Graph()

for file in graph_files:
    graph_path = os.path.join(PROCESSED_DATA_DIR, file)
    with open(graph_path, "rb") as f:
        G = pickle.load(f)
        if isinstance(G, nx.DiGraph):
            G = G.to_undirected()
        G_combined = nx.compose(G_combined, G)

print(f"Merged {len(graph_files)} graphs into one large graph with {len(G_combined.nodes)} nodes and {len(G_combined.edges)} edges.")

# Apply PageRank for node size
pagerank_scores = nx.pagerank(G_combined)

# Load sentiment scores
sentiment_df = pd.read_csv(SENTIMENT_FILE)  # Ensure sentiment data exists
sentiment_dict = dict(zip(sentiment_df["user"], sentiment_df["sentiment"]))

# Assign sentiment to nodes (default 0 for missing users)
sentiment_scores = {node: sentiment_dict.get(node, 0) for node in G_combined.nodes}

# Normalize sentiment for coloring (-1 to 1 scaled to 0 to 1)
min_sent, max_sent = -1, 1
node_colors = [(sentiment_scores[node] - min_sent) / (max_sent - min_sent) for node in G_combined.nodes]

# Normalize PageRank for node sizing
min_pr, max_pr = min(pagerank_scores.values()), max(pagerank_scores.values())
node_sizes = [(pagerank_scores[node] - min_pr) / (max_pr - min_pr) * 500 for node in G_combined.nodes]

# Take a smaller subgraph for visualization
num_nodes = min(1000, len(G_combined.nodes))
subG = G_combined.subgraph(list(G_combined.nodes)[:num_nodes])

# Apply layout
pos = nx.spring_layout(subG, k=0.3, seed=42)

# Draw the graph with both PageRank and sentiment visualization
plt.figure(figsize=(12, 8))
nx.draw(
    subG, pos, 
    node_size=node_sizes,  # PageRank-based sizing
    node_color=node_colors,  # Sentiment-based coloring
    cmap=plt.cm.coolwarm,  # Red = negative sentiment, Blue = positive sentiment
    edge_color="gray", alpha=0.6, with_labels=False
)

plt.title("Graph Visualization with Sentiment-Based Coloring and PageRank Sizing")
plt.savefig(OUTPUT_IMAGE, dpi=300)
print(f"Graph with sentiment-based coloring saved as {OUTPUT_IMAGE}")
