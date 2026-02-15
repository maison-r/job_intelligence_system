import requests

API_URL = "http://localhost:8000/api/v1/search_jobs"
API_KEY = "mysecretkey"

def fetch_jobs():
    params = {
        "search_term": "data analyst",
        "location": "Australia",
        "site_name": "indeed,linkedin,google",
        "results_wanted": 20
    }

    headers = {
        "x-api-key": API_KEY
    }

    response = requests.get(API_URL, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    jobs = data.get("jobs", [])

    formatted_jobs = []

    for job in jobs:
        formatted_jobs.append({
            "job_title": job.get("title"),
            "company": job.get("company"),
            "location": job.get("location"),
            "description": job.get("description"),
            "source": job.get("site"),
            "url": job.get("job_url")
        })

    return formatted_jobs
