def calculate_legitimacy_score(job, repost_count):
    score = 0

    # Cross board validation simulation
    if job["source"] in ["company_site", "seek", "indeed"]:
        score += 2

    # Recent posting
    score += 1

    # 6 month repost logic
    if repost_count == 0:
        score += 2
    elif 1 <= repost_count <= 3:
        score -= 1
    elif repost_count >= 4:
        score -= 3

    # Basic scam filters
    if "telegram" in job["description"].lower():
        score -= 5

    if "gmail.com" in job["description"].lower():
        score -= 3

    return score
