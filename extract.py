import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python+developer&l=Seattle,+WA&sort=date&limit={LIMIT}&radius=25"


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
    for p in range(last_page_num):
        response = requests.get(f"{URL}&start={p*LIMIT}").status_code
        print(response)
