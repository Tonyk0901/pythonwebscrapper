import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python+developer&l=Seattle,+WA&sort=date&limit={LIMIT}&radius=25"
# https://www.indeed.com/jobs?q=python+developer&l=Seattle,+WA&sort=date&limit=50&radius=25


def max_page_num():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    lists = soup.find("div", class_={"pagination"}).find_all("span")
    page_num = []
    for p in lists[:-2]:
        page_num.append(int(p.string))
    return page_num[-1]


def extract_indeed_jobs(last_page_num):
    job = []
    job_list = []
    print("Extracting on process...")
    for p in range(last_page_num):
        response = requests.get(f"{URL}&start={p*LIMIT}")
        soup = BeautifulSoup(response.text, "html.parser")
        lists = soup.find_all("div", class_={"jobsearch-SerpJobCard"})
        for l in lists:
            try:
                title = l.find("a")["title"]
                location = l.find(class_={"recJobLoc"})["data-rc-loc"]
                id = l["data-jk"]
                url = f"{URL}&vjk={id}"
                job_list.append({"title": title, "location": location, "url": url})
            except Exception:
                pass
    print("Extracting done! Result:\n")
    print(job_list)
