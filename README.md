# Multilingual Social Media Analytics

A Python-based social-media analytics project exploring multilingual text, engagement patterns, hashtags, and follower-network structure across Indian regional languages.

## Project goal

The project demonstrates an analytics workflow for social-media data:

**Synthetic data generation → preprocessing → exploratory analysis → network analysis → TF-IDF → multilingual BERT inference**

The dataset is synthetic. This is intentional because the project does not depend on direct Instagram API access.

## Analysis workflow

### 1. Synthetic dataset

The pipeline generates JSON Lines records containing:

- User/profile information
- Captions and timestamps
- Likes, comments, and shares
- Hashtags
- Follower/following relationships
- Basic engagement metrics

The current analysis uses a 500,000-record synthetic dataset configuration.

### 2. Multilingual preprocessing

The analysis includes text cleaning, URL/mention removal, Indic tokenization where applicable, and language-aware processing for English plus regional Indian languages.

### 3. Exploratory analysis

The project examines:

- Language distribution
- Word frequency
- Hashtag frequency
- Engagement distributions
- Correlations between engagement features

### 4. Network analysis

NetworkX is used to build a sample follower graph and inspect node connectivity and degree distributions.

### 5. Text representation

TF-IDF provides a lightweight lexical baseline for caption analysis.

### 6. Multilingual BERT inference

The pipeline demonstrates inference with `bert-base-multilingual-cased` for multilingual sequence classification. The current notebook-style implementation uses an untrained classification head, so its predictions should be treated as a model-integration demonstration rather than a validated sentiment model.

## Repository structure

```text
.
├── instagram_analysis.py
└── README.md
```

## Run

The repository currently contains the cleaned project entrypoint and documentation. The full exploratory implementation can be modularized further as the project evolves.

```bash
git clone https://github.com/pallavi12-code/Instagram-Multilingual-Social-Media-Analysis.git
cd Instagram-Multilingual-Social-Media-Analysis
python instagram_analysis.py
```

## Tech stack

- Python
- Pandas / NumPy
- Scikit-learn
- NetworkX
- PyTorch
- Hugging Face Transformers
- Indic NLP
- Matplotlib / Seaborn / Plotly

## Engineering improvements to pursue

- Split data generation, preprocessing, NLP, and graph analysis into modules
- Add tests for text cleaning and feature engineering
- Add a real labeled multilingual sentiment dataset for model evaluation
- Add configuration instead of hard-coded dataset size and model settings
- Add reproducible seeds and experiment tracking

## Author

**Pallavi Reddy**  
Artificial Intelligence & Machine Learning Engineering Student, CBIT
