def calculate_score(coverage, noise_count, total):
    noise_ratio = noise_count / total
    score = int((coverage * 70) - (noise_ratio * 30))
    return max(score, 0), noise_ratio
