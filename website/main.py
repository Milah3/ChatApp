from flask import Flask, render_template, request, session, redirect, url_for

# from client import Client

NAME_KEY = 'name'

app = Flask(__name__)
app.secret_key = "TryToGuessMe"


# session[NAME_KEY] = "Miles"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        print(request.form)
        session[NAME_KEY]: request.form["name"]
        return redirect(url_for("home"))
    return render_template("/login.html")


@app.route("/")
@app.route("/home")
def home():
    if NAME_KEY not in session:
        return redirect(url_for("login"))
    name = session[NAME_KEY]
    return render_template("index.html")


@app.route("/logout")
def logout():
    session.pop(NAME_KEY, None)
    return render_template("/logout.html")


@app.route("/run")
def run():
    print('ran...')
    return "something"


if __name__ == "__main__":
    app.run(debug=True)
