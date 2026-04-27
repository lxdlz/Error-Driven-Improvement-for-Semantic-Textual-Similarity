# Error-Driven-Improvement-for-Semantic-Textual-Similarity

## 【1.OVERVIEW】
This project investigates how to improve Semantic Textual Similarity (STS) models through an error-driven framework. Rather than relying solely on aggregate evaluation metrics, we focus on identifying and addressing model weaknesses on specific linguistic phenomena.
Conducted on the mteb/sts12-sts dataset using a Sentence-BERT model.

---

## 【2.OBJECTIVES】

* Improve performance on challenging linguistic phenomena
* Enhance robustness in handling negation and numerical reasoning
* Maintain strong overall STS performance
* Provide interpretable insights into model behavior

---

## 【3.DATASET AND MODEL】

**【Dataset】**

* mteb/sts12-sts
* 3,108 sentence pairs

**【Model】**

* Sentence-BERT (all-MiniLM-L6-v2)

---

## 【4. METHODOLOGY】

The proposed framework consists of three main stages:

### 4.1 Challenge Set Construction

We partition the dataset into targeted slices to expose model weaknesses:

* Negation pairs
* Numerical differences
* Control pairs

This enables fine-grained evaluation beyond aggregate metrics and reveals hidden performance gaps.

---

### 4.2 Controlled Comparison

We compare baseline and fine-tuned models under controlled experimental settings:

* Fixed model architecture
* Fixed random seeds
* Standardized evaluation protocol

Evaluation metrics:

* Pearson correlation
* Spearman correlation
* Mean Squared Error (MSE)

---

### 4.3 Targeted Fine-Tuning

We apply targeted fine-tuning to improve performance on difficult cases:

* Data mixture:

  * 70–85% general data
  * 15–30% hard cases

* Hard negatives:

  * Minimal perturbations (negation and numerical changes)

Training configuration:

* Loss: CosineSimilarityLoss
* Learning rate: 2e-5
* Batch size: 16
* Epochs: 4

---

## 【5.RESULT】

### 5.1 Baseline

* Pearson: 0.8136
* Spearman: 0.7237

---

 Fine-Tuned Model

Performance improvements across slices:

| Slice     | Improvement |
| --------- | ----------- |
| Negation  | +0.15       |
| Numerical | +0.27       |
| Control   | +0.08       |

Key observations:

* Significant improvements on challenging slices
* No degradation in overall performance

---

## 【6.INTERPRETABILITY ANALYSIS】

We analyze model behavior using:

* Token-level similarity (cosine similarity between embeddings)
* Linguistic phenomenon analysis

The following phenomena are considered:

* Synonym substitution
* Negation
* Numerical sensitivity
* Lexical overlap

This analysis helps move beyond performance metrics toward understanding model decision mechanisms.

---

## 【7.KEY CONSTRUCTURE】

1. A slice-based evaluation framework for STS
2. An error-driven improvement pipeline
3. Empirical validation of targeted fine-tuning
4. Integration of interpretability analysis

---

## 【8.PROJRECT STRUCTURE】

```
.
├── data/
├── notebooks/
├── models/
├── src/
├── results/
└── README.md
```

---

## 【9.FUTURE WORK】

* Finer-grained numerical subtypes (e.g., magnitude, units, comparisons)
* Additional interpretability methods (e.g., LIME, attention visualization)
* Trade-off analysis between slice performance and overall metrics
* Extension to other STS benchmarks

---

## 【10.SUMMARY】

This project demonstrates that targeted, error-driven improvements can significantly enhance model robustness on challenging semantic phenomena without sacrificing overall performance.
