from src.database import check_similarity_job

def check_6_month_similirity( company, normalised_title):
  count = check_similairity_job(company, normalised_title) 
  return count
