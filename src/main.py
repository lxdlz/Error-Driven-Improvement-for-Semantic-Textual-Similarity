from data_loader import load_sts12
from utils import load_model, compute_sbert_scores
from evaluation import evaluate_all
from challenge_sets import build_challenge_sets


def main():
    print("Loading data...")
    s1, s2, scores = load_sts12()

    print("Loading model...")
    model = load_model()

    print("Computing similarity...")
    preds = compute_sbert_scores(model, s1, s2)

    print("Evaluating...")
    results = evaluate_all(scores, preds)

    print("Results:")
    for k, v in results.items():
        print(f"{k}: {v:.4f}")

    print("Building challenge sets...")
    neg, num, pres, ctrl = build_challenge_sets(s1, s2, scores)

    print(f"Negation: {len(neg)}")
    print(f"Numerical: {len(num)}")
    print(f"Presence/Absence: {len(pres)}")
    print(f"Control: {len(ctrl)}")


if __name__ == "__main__":
    main()