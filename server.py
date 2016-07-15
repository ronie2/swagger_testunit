from flask import Flask, request
import flask
app = Flask(__name__, static_url_path="")
import importlib
import test_0001_main

@app.route("/report")
def report():
    q = flask.send_file("report.html")
    print(q)
    return q

@app.route("/report_xml")
def report_xml():
    q = flask.send_file("report_xml.xml")
    print(q)
    return q


@app.route("/")
def root():
    importlib.reload(test_0001_main)
    return "ok!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5556)
