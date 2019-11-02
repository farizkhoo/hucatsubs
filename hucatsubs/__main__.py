from flask import Flask, render_template, send_from_directory
import csv
import json

app = Flask(__name__, static_url_path="/static/")


@app.route("/")
def root():
    subs = []
    with open("subs.csv", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            subs.append(row)

    return render_template("index.html", data=json.dumps(subs))


if __name__ == "__main__":
    app.run(debug=True)