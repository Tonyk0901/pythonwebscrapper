import csv
import requests
from bs4 import BeautifulSoup

WORD = "python"
URL = f"https://www.indeed.com/jobs?q={WORD}}%20developer&l=Seattle%2C%20WA&limit=50"
# https://www.indeed.com/jobs?q=python%20developer&l=Seattle%2C%20WA&limit=50


def max_page_num():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    lists = soup.find("div", class_={"pagination"}).find_all("span")
    return int(lists[-3].string)


def extract_indeed_jobs(last_page_num):
    job_list = []
    print(f"Total pages to scrape: {last_page_num}")
    for p in range(last_page_num):
        print(f"Scraping [{p+1}/{last_page_num}]")
        response = requests.get(f"{URL}&start={p*50}")
        soup = BeautifulSoup(response.text, "html.parser")
        lists = soup.find_all("div", class_={"jobsearch-SerpJobCard"})
        for l in lists:
            try:
                company = l.find("span", class_="company").string.replace("\n", "")
                title = l.find("a")["title"]
                location = l.find(class_={"recJobLoc"})["data-rc-loc"]
                jk = l["data-jk"]
                url = f"https://www.indeed.com/viewjob?jk={jk}"
                job_list.append(
                    {
                        "company": company,
                        "title": title,
                        "location": location,
                        "url": url,
                    }
                )
            except Exception:
                pass
    return job_list


def save_csv(lists):
    with open("indeed_jobs/jobs.csv", mode="w") as jobs_file:
        jobs_writer = csv.writer(jobs_file, quoting=csv.QUOTE_ALL)
        jobs_writer.writerow(["Company", "Title", "Location", "Link"])
        for l in lists:
            jobs_writer.writerow(list(l.values()))
