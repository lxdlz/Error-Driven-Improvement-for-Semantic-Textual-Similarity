#visualize.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_similarity_distribution(scores, title="Similarity Distribution"):
    plt.figure()
    sns.histplot(scores, bins=50)
    plt.title(title)
    plt.xlabel("Similarity")
    plt.ylabel("Frequency")
    plt.show()


def plot_bar(metrics_dict):
    names = list(metrics_dict.keys())
    values = list(metrics_dict.values())

    plt.figure()
    plt.bar(names, values)
    plt.title("Evaluation Metrics")
    plt.show()