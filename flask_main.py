from flask import Flask, render_template, request, redirect
import indeed_job_scrape

app = Flask("Indeed Scrapper")


@app.route("/")
def home():
    return render_template("flask_home.html")


@app.route("/result")
def result():
    word = request.args.get("job_name")
    if word:
        word.lower()
    else:
        return redirect("/contact")
    return render_template("flask_search_result.html", search_by=word)


app.run()
