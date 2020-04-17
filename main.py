from extract import max_page_num, extract_indeed_jobs
from save_to_csv import save_csv

jobs = extract_indeed_jobs(max_page_num())
save_csv(jobs)
