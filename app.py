import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# 404 redirect
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Route for entry point of app
@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("index.html")


# Route for registering a new user
@app.route("/register", methods=["GET", "POST"])
def register():

    if session.get('user'):
        return redirect(url_for("login"))

    if request.method == "POST":
        # checks if username exists in the database
        existing_user = mongo.db.members.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "member_image": request.form.get("member_image"),
            "fav_book": request.form.get("fav_book").lower(),
            "member_level": request.form.get("member_level"),
            "register_date": request.form.get("register_date"),
            "is_admin": False
        }
        mongo.db.members.insert_one(register)

        # put the new user into the session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Route for member login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # checks if username exists in the database
        existing_user = mongo.db.members.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # invalid username
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Route for user's profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # finds session users info from the database and retrives just the username
    username = mongo.db.members.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Route for user logout
@app.route("/logout")
def logout():
    # logs user out and removes session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("homepage"))


# Route for member list page
@app.route("/members")
def members():
    # views a list of registered members
    members = mongo.db.members.find()
    return render_template("members.html", members=members)


# Route for library page
@app.route("/library")
def library():
    # views a list of books added
    books = mongo.db.library.find()
    return render_template("library.html", books=books)


# Route for individual book page
@app.route("/book/<book_name>", methods=["GET", "POST"])
def book():
    return render_template("book.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
