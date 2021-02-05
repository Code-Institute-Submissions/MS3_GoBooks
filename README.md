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
* Add books to my “To Read” list on the profile page.

**As an Admin I want to:**
* Have the ability to delete reviews that may be deemed rude or offensive.
* Have the ability to remove members who abuse the service.

**As Site Owner I want to:**
* Incentivise people to become members and grow the platform.
* Provide Affiliate links to Amazon book pages in order to earn money from sales made through the site.

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

### Book search (by name / genre / keywords)

### Book Lucky Dip

### Book page


## Future Features To Implement

* Add functionality to connect with other members.
* Expand user library to add books they intend to read to go along with the books they have read and reviewed.
* Add a storefront that will provide exclusive discounts to members who have built up their membership level.
* Add a social platform for users to host book club meetings and author events.

---

# Technologies Used

1. [HTML5](https://en.wikipedia.org/wiki/HTML5)

   This project uses HTML5 to display and format content on the front-end.

2. [CSS3](https://en.wikipedia.org/wiki/CSS)

   This project uses CSS3 to add styles and responsiveness to content.

3. [JavaScript](https://www.javascript.com/)

   This project uses JavaScript to add responsiveness to content.

4. [Python](https://www.python.org/)

   This project uses Python to integrate systems.

   Pip3
   Flask
   Werkzeug
   Jinja
   MongoDB
   PyMongo
   DNSPython
   Request
   Git
   GitHub
   Materialize
   RandomKeygen

---

# Testing

## Bug Fixes

While implementing the new profile page, an issue arose in which the gobooks logo wouldn't load on the page. On further investigation it appeared 
that this page causes issues with all loading concluding in a 404 error. This issue was caused because Flask was unable to load the image, 
so a static url path was required. This was as simple as changing the image source from:

img src="static/images/logo_mini.png "

to

img src="{{ url_for('static', filename='/images/logo_mini.png') }}"

---

Difficulties inputting data from library database to populate review database


---

Search bar

---

admin implementation

---

Edit and delete reviews not working like it does for edit and delete members

---

Following a review by Precious_Mentor a security issue was highlighted that allowed non-members to access areas of the project that should be exlusive to members (such as the library).
To fix this, a Login Required Decorator was created to accompany each member-exclusive page, that was sourced from PalletsProjects, via Igor_CI on Slack. 
https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator




https://validator.w3.org/
https://jigsaw.w3.org/css-validator/
https://jshint.com/
http://pep8online.com/
https://developers.google.com/web/tools/lighthouse

---

# Deployment

---

# Credits

### Content

### Media

### Code

Thanks to Pallets Projects for the Login Required Decorator
https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator

### Acknowledgements

Thanks to Igor Basuga for his assistance in locating the Login Required Decorator.