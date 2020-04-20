from indeed_job_scrape import max_page_num, extract_indeed_jobs, save_csv

jobs = extract_indeed_jobs(max_page_num())
save_csv(jobs)
