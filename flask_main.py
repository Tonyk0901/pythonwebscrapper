from flask import Flask, render_template, request, redirect, send_file
import indeed_job_scrape


app = Flask("Indeed Scrapper")
db = {}


@app.route("/")
def home():
    return render_template("flask_home.html")


@app.route("/result")
def result():
    word = request.args.get("job_name")
    if word:
        word.lower()
    else:
        return redirect("/")

    if word not in db.keys():
        job = indeed_job_scrape.get_jobs(word)
        db[word] = job

    jobs = db.get(word)

    return render_template(
        "flask_search_result.html", search_by=word, length=len(jobs), job=jobs
    )


@app.route("/download")
def download():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception
        word = word.lower()
        if word not in db.keys():
            raise Exception
        print("It got here!!")
        indeed_job_scrape.save_csv(db.get(word))
        send_file(
            "/indeed_jobs/jobs.csv", as_attachment=True, attachment_filename="hehe.csv"
        )
        print("Did it got here?")
        return redirect("/result?job_name={word}")
    except Exception:
        return redirect("/")


app.run()
