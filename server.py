from flask import Flask
import flask

app = Flask(__name__, static_url_path="")
import importlib
import test_0001_main

host = "0.0.0.0"
port = 5556
report_html = "report.html"
report_xml = "report_xml.xml"

@app.route("/report")
def report():
    html_report = flask.send_file(report_html)
    return html_report


@app.route("/report_xml")
def report_xml():
    xml_report = flask.send_file(report_xml)
    return xml_report


@app.route("/")
def root():
    importlib.reload(test_0001_main)
    return "Tests Done! Please visit {host}:{port}{report} " \
           "and {host}:{port}{xml_report}".format(host=host,
                                                  port=port,
                                                  report=report_html,
                                                  xml_report=report_xml)


if __name__ == "__main__":
    app.run(host=host, port=port)
