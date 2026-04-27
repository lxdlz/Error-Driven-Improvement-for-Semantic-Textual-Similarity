# Dataset

This project uses the dataset:

- Name: mteb/sts12-sts
- Source: Hugging Face
- Task: Semantic Textual Similarity (STS)

## Structure

Each example contains:

- sentence1: first sentence
- sentence2: second sentence
- score: similarity score (0–1)

## Split Used

- test split only
- total: 3,108 sentence pairs

## Usage

The dataset is loaded dynamically:

```python
from datasets import load_dataset
dataset = load_dataset("mteb/sts12-sts")