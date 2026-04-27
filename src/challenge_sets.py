import re


def contains_negation(sentence):
    negation_words = ["not", "no", "never", "none", "n't"]
    return any(word in sentence.lower() for word in negation_words)


def extract_numbers(sentence):
    return re.findall(r"\d+", sentence)


def has_numerical_difference(s1, s2):
    nums1 = extract_numbers(s1)
    nums2 = extract_numbers(s2)
    return nums1 != nums2


def has_numerical_presence_absence(s1, s2):
    nums1 = extract_numbers(s1)
    nums2 = extract_numbers(s2)
    return (len(nums1) == 0 and len(nums2) > 0) or (len(nums1) > 0 and len(nums2) == 0)


def build_challenge_sets(sentences1, sentences2, scores):
    negation = []
    numerical = []
    presence_absence = []
    control = []

    for s1, s2, score in zip(sentences1, sentences2, scores):
        if contains_negation(s1) or contains_negation(s2):
            negation.append((s1, s2, score))
        elif has_numerical_difference(s1, s2):
            numerical.append((s1, s2, score))
        elif has_numerical_presence_absence(s1, s2):
            presence_absence.append((s1, s2, score))
        else:
            control.append((s1, s2, score))

    return negation, numerical, presence_absence, control