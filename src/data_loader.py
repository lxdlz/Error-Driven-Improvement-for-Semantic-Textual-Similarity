from datasets import load_dataset


def load_sts12():
    """
    Load mteb/sts12-sts dataset (test split)
    """
    dataset = load_dataset("mteb/sts12-sts")
    sts_data = dataset["test"]

    sentences1 = [item["sentence1"] for item in sts_data]
    sentences2 = [item["sentence2"] for item in sts_data]
    scores = [item["score"] for item in sts_data]

    return sentences1, sentences2, scores