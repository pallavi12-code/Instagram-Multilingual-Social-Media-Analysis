# 📊 Multilingual Social Media Analytics Engine & Graph Pipeline

## 📌 Project Overview
This repository features an advanced, end-to-end data analytics and natural language processing pipeline built to analyze large-scale, unstructured social media interactions. Processing a dataset of **500,000 records**, the engine specializes in handling high-frequency regional variations, extraction of linguistic semantic clusters, and structural network mapping of user interactions.

The primary objective of this project is to decode how regional demographics interact across diverse languages by blending Deep Learning NLP architectures, Graph Theory, and High-Dimensional Vector Reduction.

---

## 🚀 Core Architectural Features

### 1. Multilingual Natural Language Processing
* **Semantic Analysis:** Implements **Multilingual BERT (mBERT)** via the Hugging Face `transformers` pipeline to calculate cross-lingual contextual sentiments.
* **Linguistic Representation:** Leverages text vectorization pipelines (`TF-IDF` and tokenization models) engineered to support **9+ regional Indian languages** (including Hindi, Telugu, Marathi, and Tamil), eliminating geographic and script bias in sentiment modeling.

### 2. High-Dimensional Cluster Reduction
* **Dimensionality Compression:** Employs **Principal Component Analysis (PCA)** to capture global variance and condense dense embeddings.
* **Spatial Local Clustering:** Implements **t-Distributed Stochastic Neighbor Embedding (t-SNE)** to optimize local structures, translating 768-dimension transformer tensors into interactive 2D and 3D space maps.

### 3. Graph Network & Topology Analysis
* **Network Graph Formulation:** Constructs a massive, relational interaction graph utilizing **NetworkX** where nodes represent users and edges represent multi-point engagements.
* **Community Detection:** Applies graph-partitioning logic to isolate structural communication clusters and map localized viral echo chambers.

### 4. Interactive Enterprise Dashboard
* Built a sleek, production-grade **Streamlit application** featuring an optimized dark theme.
* Features advanced sidebar multi-filtering, dynamic geographic/linguistic segment drill-downs, cross-tab visual analytics, and real-time computation of high-level operational KPIs.

---

## 🛠️ System Tech Stack
* **Core Frameworks:** Python, Pandas, NumPy
* **Machine Learning & NLP:** Scikit-Learn, PyTorch, Transformers (mBERT)
* **Graph Network Theory:** NetworkX
* **Data Visualization & Delivery:** Plotly, Streamlit, Seaborn, Matplotlib

---

## 📂 Project Structure
text
├── DVA_A2.ipynb         # Deep Dive Notebook: NLP Embeddings, t-SNE, & Network Modeling
├── app.py               # Enterprise Streamlit Dashboard Execution Script
├── instagram_data.jsonl # Scaled Core Ingestion Dataset (500k Simulated Records)
└── README.md            # System Executive Summary

---
#🚀 Installation & Local Deployment
Clone the personal workspace repository:

Bash
git clone [https://github.com/pallavi12-code/YOUR-REPO-NAME.git](https://github.com/pallavi12-code/Multilingual Social Media Analytics Engine & Graph Pipeline
.git)
cd YOUR-REPO-NAME
Provision the required environment dependencies:

Bash
pip install streamlit pandas numpy plotly scikit-learn networkx transformers torch
Execute the local analytical dashboard server:


👥 Core Project Engineering Team
Marikanti Pallavi Reddy — marikantipallavireddy@gmail.com
