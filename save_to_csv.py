import csv
import os

os.remove("jobs.csv")


def save_csv(lists):
    with open("jobs.csv", mode="w") as jobs_file:
        jobs_writer = csv.writer(jobs_file)
        jobs_writer.writerow(["Title", "Location", "Link"])
        for l in lists:
            jobs_writer.writerow(list(l.values()))
