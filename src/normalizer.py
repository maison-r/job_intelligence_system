import re 

def normalize_title(title):
  title = title.lower()
  title = re.sub(r'[^a-z ]', '', title )

if "junior" in title or "graduate" in title or "entry" in title:
  return "entry_ level"

if "buisness intelligence" in title:
  return "Bi_analyst"

if "data analyst" in title:
  return "data analyst"

return title.replace(" ", "_")

## this adjustes the title in the job postings when scrapping websites 
