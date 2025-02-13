A Graph-Based Approach for Identifying At-Risk Users in Mental Health Communities

The goal of this project is to analyze mental health communities and identify influential users using Google PageRank. Additionally, we perform sentiment analysis to detect at-risk users who may be experiencing distress based on their posts.

📌 Step 1: Data Collection & Preprocessing
✅ Collected datasets from mental health communities (Depression, Anxiety, PTSD, Suicide Watch, etc.).
✅ Cleaned the data by removing missing values and pre-processing text features.
✅ Stored the cleaned data in the /data/processed/ folder (not uploaded to GitHub due to size limitations).
🔍 Key File: 
data_preprocessing.py

📌 Step 2: Graph Construction & PageRank Calculation
✅ Built a user interaction graph, where:
Nodes represent users.
Edges represent interactions (e.g., replying to each other's posts).
✅ Applied Google PageRank to rank the most influential users.
✅ Detected communities within the mental health space using the Louvain algorithm.
🔍 Key Files:
graph_construction.py → PageRank computation
user_pagerank_scores.csv → List of most influential users
community_assignments.csv → List of user communities

 Step 3: Graph Visualization
✅ Merged multiple graphs into one large graph to visualize the network.
✅ Filtered low-degree nodes to focus on strongly connected users.
✅ Created a visualization to show the network structure.
📊 Graph Example:
🔍 Key Files:
graph_visualization.py → Code for visualizing the graph
fixed_filtered_graph.png → Graph image

📌 Step 4: Sentiment Analysis
✅ Used TextBlob to analyze sentiment in user posts.
✅ Identified users with negative sentiment, labeling them as at-risk users.
✅ Saved the list of at-risk users.
🔍 Key Files:
sentiment_analysis.py → Code for sentiment analysis
at_risk_users.csv → List of users with negative sentiment

📌 Step 5: Identifying Critical At-Risk Users
✅ Combined PageRank scores (influence) with sentiment analysis.
✅ Identified users who are both influential AND at risk.
✅ These are the most critical users to monitor, as they can impact others negatively.
🔍 Key Files:
identify_critical_users.py → Code for merging PageRank & sentiment analysis
critical_at_risk_users.csv → Final list of high-risk influential users
