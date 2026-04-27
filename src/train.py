from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader


def prepare_training_data(sentences1, sentences2, scores):
    train_examples = []
    for s1, s2, score in zip(sentences1, sentences2, scores):
        train_examples.append(InputExample(texts=[s1, s2], label=float(score)))
    return train_examples


def train_model(sentences1, sentences2, scores, output_path="models/sbert_finetuned"):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    train_examples = prepare_training_data(sentences1, sentences2, scores)
    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)

    train_loss = losses.CosineSimilarityLoss(model)

    model.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=4,
        warmup_steps=100,
        output_path=output_path
    )

    return model