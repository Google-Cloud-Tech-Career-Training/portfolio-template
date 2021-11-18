from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

name="Lenz Paul"
role="Software Engineer"
phone="+1-778-268-1456"
email="info@lenzpaul.dev"
location="Vancouver, BC, Canada"


@app.route("/")
def index():
    return render_template("index.html", 
    name=name,
    role=role,
    phone=phone,
    email=email
    )

if __name__ == "__main__":
    app.run(debug=True)