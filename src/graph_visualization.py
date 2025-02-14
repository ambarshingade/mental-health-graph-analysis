import networkx as nx
import matplotlib.pyplot as plt
import os
import pickle

# Set paths
PROCESSED_DATA_DIR = "/home/ambarshingade/mental_health_analysis/data/processed"

# Get all graph files
graph_files = [f for f in os.listdir(PROCESSED_DATA_DIR) if f.endswith("graph.gpickle")]

# Initialize an empty graph
G_combined = nx.Graph()  # Ensure all graphs are merged as undirected

# Load and merge all graphs
for file in graph_files:
    graph_path = os.path.join(PROCESSED_DATA_DIR, file)
    with open(graph_path, "rb") as f:
        G = pickle.load(f)
        
        # Convert to undirected before merging
        if isinstance(G, nx.DiGraph):  
            G = G.to_undirected()
        
        G_combined = nx.compose(G_combined, G)  # Merge graphs

print(f"Merged {len(graph_files)} graphs into one large graph with {len(G_combined.nodes)} nodes and {len(G_combined.edges)} edges.")

# Apply a filtering step to remove nodes with very few connections
min_degree = 5  # Only keep nodes that have at least this many edges
filtered_nodes = [node for node, degree in dict(G_combined.degree()).items() if degree >= min_degree]
G_filtered = G_combined.subgraph(filtered_nodes)

print(f"Filtered graph with {len(G_filtered.nodes)} nodes and {len(G_filtered.edges)} edges.")

# Take a smaller subgraph for visualization
num_nodes = min(1000, len(G_filtered.nodes))  # Adjust size for better readability
subG = G_filtered.subgraph(list(G_filtered.nodes)[:num_nodes])

# Apply an improved layout
pos = nx.spring_layout(subG, k=0.3, seed=42)  # Adjust k to control spacing

# Compute PageRank for node coloring
pagerank_scores = nx.pagerank(G_filtered)

# Normalize PageRank values for coloring
min_pr, max_pr = min(pagerank_scores.values()), max(pagerank_scores.values())
node_colors = [(pagerank_scores[node] - min_pr) / (max_pr - min_pr) for node in subG.nodes]

# Draw the filtered graph with PageRank-based coloring
plt.figure(figsize=(12, 8))
nx.draw(
    subG, pos, node_size=50, node_color=node_colors, cmap=plt.cm.viridis, 
    edge_color="gray", alpha=0.6, with_labels=False
)

plt.title("Filtered Graph Visualization with PageRank Coloring")
plt.savefig("../results/fixed_filtered_graph.png", dpi=300)

print("Graph with strong connections saved as fixed_filtered_graph.png")
