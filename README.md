# Milestone Project 3 - GoBooks

# Table of Contents

 - [**Introduction**](#introduction)

 - [**User Experience**](#user-experience)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Site Design](#site-design)
    - [Database Design](#database-design)

 - [**Features**](#features)
    - [Existing Features](#existing-features)
    - [Future Features To implement](#future-features-to-implement)

 - [**Technologies Used**](#technologies-used)
    - [Languages](#languages)
    - [APIS and Frameworks](#apis-and-frameworks)
    - [Hosting, Databases and Version Control](#hosting,-databases-and-version-control)
    - [Websites](#websites)

 - [**Testing**](#testing)
    - [Bug Fixes](#bug-fixes)
    - [Performance](#performance)
    - [Validator Tests](#validator-tests)

 - [**Deployment**](#deployment)

 - [**Credits**](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

---

# Introduction
In order to showcase an understanding of Data Centric Development, this project has been created. GoBooks utilises information stored in an external database with data that is populated
within the project website. Users have utilise CRUD functionality to create profiles, books and user reviews, all within a stylish and straightforward interface. This project also uses 
secure frameworks and validation tools to deter users from manipulating the site outside of its intended capabilities.

---

# User Experience

## Project Goals
GoBooks is a web application that allows users to build a digital library, review books they have read, and discover new reads that may interest them. 
Once the user has signed up to the site, they will have the ability to build out their profile and create their own personal library of books they have read and reviewed.
This site is aimed at people of all ages, races and genders who share a common interest: a love of books, and as such the site has been specifically designed to 
encourage engagement through a user-friendly aesthetic. 


## User Stories

**As a First Time Visitor I want to:**
* Understand the purpose of the website.
* Navigate easily through the website.
* Locate books using the search functionality, read reviews left by members and be able to click through to the book’s Amazon page.
* Use the website’s Book Lucky Dip to find a new book to read.
* Understand the benefits of becoming a member and locate the Register page.

**As a Member I want to:**
* Be able to write, edit and delete my own reviews.
* Benefit from the incentives of membership.
* View my personalised Member Profile page.
* View other members on the site and see what books they have read and reviewed.

**As an Admin I want to:**
* Have the ability to delete reviews that may be deemed rude or offensive.
* Have the ability to remove members who abuse the service.

**As Site Owner I want to:**
* Incentivise people to become members and grow the platform.
* Provide Affiliate links to Amazon book pages in order to earn money from sales made through the site.


## Wireframes


## Site Design

### Colour Scheme
GoBooks uses a simple yet effective colour palette. The use of Green illicit thoughts of harmony and health, relaxing and encouraging a positive mindset to the user.

### Typography
GoBooks uses the font [Quicksand](https://fonts.google.com/specimen/Quicksand?query=quicksand&preview.text_type=custom), sourced from **Google Fonts**. This font was chosen to work in
conjunction with the colour palette to instill a calm and comforting sense across the entire website.

### Artwork



## Database Design


---

# Features

## Existing Features
To realise the goals of the project, the following features were implemented:

### Home page 

A warm and welcoming home page was created to inspire the all-inclusive nature of the site and encourage new users to discover what GoBooks has to offer.

### Log In 

### Register

### Member Profile

### Member List

### Book search (by name / genre / author)

### Book Lucky Dip

### Book page


## Future Features To Implement

* Add functionality to connect with other members.
* Expand user library to add books they intend to read to go along with the books they have read and reviewed.
* Add a storefront that will provide exclusive discounts to members who have built up their membership level.
* Add a social platform for users to host book club meetings and author events.

---

# Technologies Used

## Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

* [CSS3](https://en.wikipedia.org/wiki/CSS)

* [JavaScript](https://www.javascript.com/)

* [JQuery](https://jquery.com/)

* [Python](https://www.python.org/)

## APIS and Frameworks

* [Pip3](https://pypi.org/project/pip/)

* [Flask](https://flask.palletsprojects.com/)

* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)

* [Jinja](https://jinja.palletsprojects.com/)

* [PyMongo](https://pymongo.readthedocs.io/en/stable/)

* [DNSPython](https://www.dnspython.org/)

* [Request](https://requests.readthedocs.io/)

* [Functools](https://docs.python.org/3/library/functools.html)

* [Datetime](https://docs.python.org/3/library/datetime.html)

* [Random](https://docs.python.org/3/library/random.html)

* [OS](https://docs.python.org/3/library/os.html)

* [Bson](https://docs.mongodb.com/manual/reference/bson-types/)

## Hosting, Databases and Version Control

* [MongoDB](https://www.mongodb.com/)

* [Git](https://git-scm.com/)

* [GitHub](https://github.com/)
   
* [Heroku](https://www.heroku.com/)

## Websites

* [Materialize](https://materializecss.com/)

* [RandomKeygen](https://randomkeygen.com/)

* [Google Fonts](https://fonts.google.com/specimen/Quicksand?query=quicksand&preview.text_type=custom)

---

# Testing

## Bug Fixes

### GoBooks Logo

While implementing the new profile page, an issue arose in which the gobooks logo wouldn't load on the page. On further investigation it appeared that this page causes issues with all loading 
concluding in a 404 error. This issue was caused because Flask was unable to load the image, so a static url path was required. This was as simple as changing the image source from:
 ```
img src="static/images/logo_mini.png "
```
to
```
img src="{{ url_for('static', filename='/images/logo_mini.png') }}"
```


### Autopopulating Database Entry Data

In order to ensure that the database functioned as intended, three collections were made: **Members**, **Library** and **Reviews**. Despite holding much of the same data in each, the
Library and Review collections were split into two separate collections so that an admin could delete a review without removing the connected book, and vice versa. The intention was that the 
user would select the **Add Review** option from the page of the book they wished to review, which would then populate the necessary data into the database entry so that the user didn't have to. 
This would leave them needing only to review and rate the book. 

However, this developed some issues when trying to implement the necessary data into the review form. Initial attempts resulted in these entries returning Null as a response, especially when 
the user edited their review, or not updating the entry if edited or deleted. This was eventually fixed when it was discovered that the complication of book_id and review_id had been misunderstood.
After some time spent better understanding this complication, the code was updated and the function worked as intended.


### Search bar

In order to allow users to search for their favourite books, this project follows the tutorial outlined in Code Institute's mini task project. However, upon completion of the tutorial,
the search function didn't work. It would return a 200 status, and even when adding a print function, it would not print the query to the terminal. Extensive searching online could not 
return any solutions as the search bar was submitting a GET request, not a POST request.

Finally, CI tutor **Igor_CI** discovered that the form was actually nested inside another form tag, which was causing the issue. Once this outer form was deleted, the form worked exactly as intended.

---

### Admin Implementation

---

### Login Decorator

Following a review by **Precious_Mentor** a security issue was highlighted that allowed non-members to access areas of the project that should be exlusive to members (such as the library).
To fix this, a Login Required Decorator was created to accompany each member-exclusive page, that was sourced from **[PalletsProjects](https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator)**, 
via **Igor_CI** on Slack. 


### Expanding Functionality Beyond Amazon

One issue that was raised by a project tester was that the add_book function only allowed inputs from Amazon, and not other pages. This was due to the inclusion of a required input of the
Amazon Serial Identifier Number (ASIN), which is only found on Amazon products. If someone wanted to add a book via a different platform, they would be unable to proceed past this point.
The reason this was initially included was to ensure that the same book could not be added twice, but if two books with the same name existed they could be included. Further research into this
showed that books have their own unique identifier, known as an ISBN (International Standard Book Number) which is unified across all physical and digital books no matter their storefront.
Therefore the database was updated to allow the inclusion of the ISBN, along with the ASIN, as this will provide the groundwork for a future feature, which will generate a sales link that
scrapes the user's location by country and searches for the ISBN or ASIN with a unique affiliate link included at the end.


## Performance

USE LIGHTHOUSE HERE


## Validator Testing

### W3 HTML Validator 
https://validator.w3.org/

### W3 CSS Validator
https://jigsaw.w3.org/css-validator/

# JSHint JS Validator
https://jshint.com/

# PEP8 Python Validator 
http://pep8online.com/

# Google Chrome Lighthouse 
https://developers.google.com/web/tools/lighthouse

---

# Deployment

---

# Credits

### Content

- Book covers and descriptions provided by individual authors / publishers via Amazon.

### Media

- Background artwork and Project Logo created by the developer, [Robert Clark](https://github.com/Robert-Clark-1990).

### Code

- Login Required Decorator by [PalletsProjects](https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator)

### Acknowledgements

- Thanks to **Igor Basuga** for his assistance in locating the Login Required Decorator and help with the Search Bar function.

- Thanks to **Precious Igene** for his continued assistance as mentor.