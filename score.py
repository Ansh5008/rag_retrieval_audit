def calculate_score(coverage, noise_count, total_docs):
    noise_ratio = noise_count / total_docs

    score = int((coverage * 70) - (noise_ratio * 30))
    score = max(score, 0)

    return score, noise_ratio
