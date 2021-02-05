import os
import random
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from functools import wraps
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("Get full access to GoBooks by signing up!")
            return redirect(url_for("homepage"))
        return f(*args, **kwargs)
    return decorated_function


# 404 redirect
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Route for entry point of app
@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("index.html")


###########################################################################


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
        today_date = date.today()
        current_date = today_date.strftime("%d %b %y")
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "member_image": request.form.get("member_image"),
            "fav_book": request.form.get("fav_book"),
            "member_level": request.form.get("member_level"),
            "register_date": current_date,
            "is_admin": False
        }
        mongo.db.members.insert_one(register)

        # put the new user into the session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Route for editing user profile
@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
@login_required
def edit_profile(user_id):

    if request.method == "POST":
        update_profile = {
            "username": mongo.db.members.find_one(
                {"_id": ObjectId(user_id)})["username"],
            "password": mongo.db.members.find_one(
                {"_id": ObjectId(user_id)})["password"],
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "member_image": request.form.get("member_image"),
            "fav_book": request.form.get("fav_book"),
            "member_level": request.form.get("member_level"),
            "register_date": mongo.db.members.find_one(
                {"_id": ObjectId(user_id)})["register_date"],
            "is_admin": mongo.db.members.find_one(
                {"_id": ObjectId(user_id)})["is_admin"],
        }
        mongo.db.members.update({"_id": ObjectId(user_id)}, update_profile)

        flash("Profile Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))

    username = mongo.db.members.find_one({"_id": ObjectId(user_id)})
    return render_template("edit_profile.html", username=username)


# Route for deleting user profile
@app.route("/delete_profile/<user_id>")
@login_required
def delete_profile(user_id):

    mongo.db.members.remove({"_id": ObjectId(user_id)})
    # removes the  user from the session cookie
    session.pop("user")
    flash("Profile Successfully Deleted")
    return redirect(url_for("homepage"))


###########################################################################


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
@login_required
def profile(username):

    # finds session users info from the database and retrieves the username
    username = mongo.db.members.find_one(
        {"username": session["user"]})

    if session["user"]:
        user_reviews = list(mongo.db.reviews.find(
            {"username": session["user"]}))
        return render_template(
            "profile.html", username=username, user_reviews=user_reviews)

    return redirect(url_for("login"))


# Route for user logout
@app.route("/logout")
def logout():

    # logs user out and removes session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("homepage"))


###########################################################################


# Route for member list page
@app.route("/members")
@login_required
def members():

    # views a list of registered members
    members = mongo.db.members.find()
    return render_template("members.html", members=members)


###########################################################################


# Route for library page
@app.route("/library")
@login_required
def library():

    # views a list of books added
    books = list(mongo.db.library.find())
    return render_template("library.html", books=books)


# Route for book search functionality  <-- NEEDS WORK
@app.route("/search", methods=["GET", "POST"])
@login_required
def search():

    if request.method == "POST":
        query = request.form.get("query")
        books = list(mongo.db.library.find({"$text": {"$search": query}}))

    return render_template("library.html", books=books)


###########################################################################


# Route for returning a book at random
@app.route("/lucky_dip", methods=["GET", "POST"])
@login_required
def lucky_dip():

    books = list(mongo.db.library.find())
    random_book = random.choice(books)
    if request.method == "POST":
        return redirect(url_for("library"))

    return render_template("lucky_dip.html", random_book=random_book)


###########################################################################


# Route for adding a new book to the library
@app.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():

    if request.method == "POST":
        # checks if book exists in the database
        existing_book = mongo.db.library.find_one(
            {"book_name": request.form.get("book_name").lower()})

        if existing_book:
            flash("This book already exists")
            return redirect(url_for("add_book"))

        add_book = {
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_asin": request.form.get("book_asin"),
            "book_genre": request.form.get("book_genre"),
            "book_description": request.form.get("book_description"),
            "book_cover": request.form.get("book_cover"),
            "book_url": request.form.get("book_url")
        }
        mongo.db.library.insert_one(add_book)

        flash("Book Successfully Added")
        return redirect(url_for("library"))

    return render_template("add_book.html")


# Route for editing a book in the library <-- NEEDS WORK
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
@login_required
def edit_book(book_id):

    # ADD IF STATEMENT TO CHECK IF SESSION USER IS ADMIN
    if request.method == "POST":
        edit_book = {
            "book_name": request.form.get("book_name"),
            "book_author": request.form.get("book_author"),
            "book_asin": request.form.get("book_asin"),
            "book_genre": request.form.get("book_genre"),
            "book_description": request.form.get("book_description"),
            "book_cover": request.form.get("book_cover"),
            "book_url": request.form.get("book_url")
        }
        mongo.db.library.update(edit_book)
        flash("Book Successfully Updated")
        return redirect(url_for("book", book_id=book_id))

    book_id = mongo.db.library.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book_id=book_id)


# Route for individual book page
@app.route("/book/<book_id>", methods=["GET", "POST"])
@login_required
def book(book_id):

    book_id = mongo.db.library.find_one({"_id": ObjectId(book_id)})
    if book_id["book_name"]:
        user_reviews = list(mongo.db.reviews.find(
            {"book_name": book_id["book_name"]}))

    return render_template(
        "book.html", book_id=book_id, user_reviews=user_reviews)


###########################################################################


# Route for adding a new review
@app.route("/add_review/<book_id>", methods=["GET", "POST"])
@login_required
def add_review(book_id):

    if request.method == "POST":
        # adds book and user data to review database
        today_date = date.today()
        current_date = today_date.strftime("%d %b %y")
        add_review = {
            "book_name": mongo.db.library.find_one(
                {"_id": ObjectId(book_id)})["book_name"],
            "book_author": mongo.db.library.find_one(
                {"_id": ObjectId(book_id)})["book_author"],
            "book_asin": mongo.db.library.find_one(
                {"_id": ObjectId(book_id)})["book_asin"],
            "book_genre": mongo.db.library.find_one(
                {"_id": ObjectId(book_id)})["book_genre"],
            "book_cover": mongo.db.library.find_one(
                {"_id": ObjectId(book_id)})["book_cover"],
            "book_url": mongo.db.library.find_one(
                {"_id": ObjectId(book_id)})["book_url"],
            "username": session["user"],
            "book_review": request.form.get("book_review"),
            "book_rating": request.form.get("book_rating"),
            "review_date": current_date
        }
        mongo.db.reviews.insert_one(add_review)

        flash("Book Review Added")
        return redirect(url_for("book", book_id=book_id))

    book_id = mongo.db.library.find_one({"_id": ObjectId(book_id)})
    return render_template("add_review.html", book_id=book_id)


# Route to edit a review
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
@login_required
def edit_review(review_id):

    if request.method == "POST":
        today_date = date.today()
        current_date = today_date.strftime("%d %b %y")
        edit = {
            "book_name": mongo.db.reviews.find_one(
                {"_id": ObjectId(review_id)})["book_name"],
            "book_author": mongo.db.reviews.find_one(
                {"_id": ObjectId(review_id)})["book_author"],
            "book_asin": mongo.db.reviews.find_one(
                {"_id": ObjectId(review_id)})["book_asin"],
            "book_genre": mongo.db.reviews.find_one(
                {"_id": ObjectId(review_id)})["book_genre"],
            "book_cover": mongo.db.reviews.find_one(
                {"_id": ObjectId(review_id)})["book_cover"],
            "book_url": mongo.db.reviews.find_one(
                {"_id": ObjectId(review_id)})["book_url"],
            "username": session["user"],
            "book_review": request.form.get("book_review"),
            "book_rating": request.form.get("book_rating"),
            "review_date": current_date
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, edit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", review=review)


# Route to delete a review
@app.route("/delete_review/<review_id>")
@login_required
def delete_review(review_id):

    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("library"))


###########################################################################


# don't forget to turn debug=false before launch
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
