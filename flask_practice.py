from flask import Flask, render_template, request, redirect

app = Flask("Super Scrapper")


@app.route("/")
def home():
    return render_template("flask_home.html")


@app.route("/contact")
def contact():
    return "haha! ya found me!"


@app.route("/result")
def result():
    word = request.args.get("job_name")
    if word:
        word.lower()
    else:
        return redirect("/contact")
    return render_template("flask_search_result.html", search_by=word)


app.run()
