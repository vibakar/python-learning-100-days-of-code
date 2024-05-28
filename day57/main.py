from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!!!"

@app.route("/guess/<name>")
def guess_gender_age(name):
    gender_api = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(gender_api)
    gender = gender_response.json()["gender"]

    age_api = f"https://api.agify.io/?name={name}"
    age_response = requests.get(age_api)
    age = age_response.json()["age"]
    return render_template("index.html", name=name.title(), gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)