"""Multilingual social-media analytics demonstration pipeline.

The script generates a synthetic dataset, performs text preprocessing,
exploratory analysis, network analysis, TF-IDF vectorization, and optional
multilingual BERT inference.

The source dataset is synthetic because direct Instagram API access is not
part of this project.
"""

# The original analysis is preserved in the repository history. This module
# provides a clean entrypoint for future modularization of the notebook work.

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_FILE = PROJECT_ROOT / "instagram_data.jsonl"


def project_paths() -> dict[str, Path]:
    """Return the important project paths."""
    return {"root": PROJECT_ROOT, "data": DATA_FILE}


if __name__ == "__main__":
    print("Multilingual social-media analysis project")
    print(f"Data path: {DATA_FILE}")
    print("See the repository README for the analysis workflow and setup.")
