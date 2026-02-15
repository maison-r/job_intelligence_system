import os
from datetime import datetime
import pandas as pd

from src.database import initialize_database, insert_job
from src.normalizer import normalize_title
from src.similarity import check_6_month_similarity
from src.scorer import calculate_legitimacy_score
from src.scraper import fetch_jobs


def main():
    if not os.path.exists("data"):
        os.makedirs("data")

    initialize_database()

    jobs = fetch_jobs()
    verified_jobs = []

    for job in jobs:
        normalized_title = normalize_title(job["job_title"])
        repost_count = check_6_month_similarity(job["company"], normalized_title)

        score = calculate_legitimacy_score(job, repost_count)

        job_record = {
            "job_title": job["job_title"],
            "normalized_title": normalized_title,
            "company": job["company"],
            "location": job["location"],
            "description": job["description"],
            "date_posted": datetime.now().strftime("%Y-%m-%d"),
            "source": job["source"],
            "url": job["url"],
            "legitimacy_score": score,
            "similar_in_6_months": repost_count
        }

        insert_job(job_record)

        if score >= 3:
            verified_jobs.append(job_record)

    df = pd.DataFrame(verified_jobs)
    df.to_csv("weekly_verified_jobs.csv", index=False)

    print("Scan complete. Verified jobs saved.")


if __name__ == "__main__":
    main()
