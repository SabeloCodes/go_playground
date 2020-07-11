# Go Playground - Milestone Project 3
This is a web application primarily targeted to people with young families, or anyone looking 
after children. The website provides a simple easy-to-use method for locating and finding out in-depth 
informationabout a children's playground or park, before going there. All the content will be created 
by other users, this will widen the database and ensure that a wide range of playgrounds is covered. 

# UX
As a parent of young children under the age of 12 years old, I am constantly looking for ways to 
entertain them. Playing in the garden can quickly become boring and unadventurous for both the parent 
and the child. So going out to local parks and playgrounds is an essential part of parenting when you 
live in the city or an urban location. 

One of the most frustrating occurrences when going to a new playground that you have not visited before 
is not knowing what to expect when you get there. When travelling with two or three children of varying 
ages, one would need to know if they are working toilets, if there is a cafe where they can buy food if 
need be. Even to know when the playground was last renovated and if the equipment is operating properly. 
All of these questions go through a parent's mind as they are leaving the house to go to a playground 
they have never been before. 

The availability of all this information would be hugely beneficial to parents, and so will make that 
trip to a new playground more interesting for the children because mum and dad will know what to expect 
when they get to their destination. Also, this web application can act as a resource for ensuring that 
different local authorities held accountable for making sure that play spaces are maintained properly 
and kept in good working order. If everything is kept to a decent standard then the reviews will be 
positive from parents and children. 

## Mockups
<img src="/static/images/wireframes/AddPlayground.png" width="900px">
<img src="/static/images/wireframes/BrowsePlayground.png" width="900px">
<img src="/static/images/wireframes/EditPlayground.png" width="900px">
<img src="/static/images/wireframes/Home.png" width="900px">
<img src="/static/images/wireframes/ShowPlayground.png" width="900px">

# Features
### Existing Features
* Index Page
    * This is the home page of the site where users are greeted by a carousel displaying various
       playground images and relevant news related to children's play-spaces. Also, the user can select
       *from a dropdown menu* a particular borough in order to display only the playgrounds from 
       that area. 
    
* Playgrounds
    * Users can view the entirety of the playgrounds database, but only in a minimised format. From there
       a user can then choose a playground profile they want to examine in detail.

* Add Playground
    * Form for adding a new playground.

* Show Playgrounds
    * Displays in detail all the features of an individual playground. Includes a map, review, pictures 
       and two options for editing and deleting a playground entry.

* Edit Playground
    * This is a feature found within *Show Playground* and gives the user the ability to amend any 
       information they might have mistakenly entered incorrectely.

* Delete Playground
    * Also found in *Show Playground* and gives the ability to delete the entire entry.

* Footer
    * The bottom of each page has a footer with links to the social media networks for interested 
       users to find more up-to-date information.

## Features Left to Implement
The homepage caurosel will display a variety of featured articles, video links and other material
related to parks and playgrounds in London. 

# Technologies Used
This application was developed initially using an [AWS](https://aws.amazon.com/) IDE called 
[Cloud9](https://aws.amazon.com/cloud9/), and then moved to the [Microsoft Visual Studio](https://visualstudio.microsoft.com/vs/whatsnew/) 
based [GitPod](https://www.gitpod.io/) where it was completed. 

* __[HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)__
    Using the latest specification markup language to fill the the web application templates with 
    useful and meaningful content.

* __[CSS 3](https://developer.mozilla.org/en-US/docs/Web/CSS)__
    The language that describes how HTML elements should be displayed on a web application.

* __[JQuery](https://jqueryui.com/)__
    Easy to use JS library for manipulating DOM elements.    

* __[JavaScript](https://developer.mozilla.org/en-US/docs/Web/Javascript)__
    Running with the HTML strucrure of the website, JS performs dynamic functions to update, 
    change and manipulate DOM.

* __[Bootstrap](https://getbootstrap.com/)__
     Applied this collection of reusable pieces of HTML, CSS, and JavaScript code framework in 
     order to create a fully responsive web application. 

* __[Flask](https://flask.palletsprojects.com/en/1.1.x/)__
    In order to run Python server-side code, I used a Python web lightweight framework called Flask.

* __[Python](https://developer.mozilla.org/en-US/docs/Glossary/Python)__
    Used this flexible programming language for my application development.

* __[MongoDB](https://www.mongodb.com/)__
    For data schemas I used this document-oriented database program.

* __[Google API's](https://developers.google.com/docs/api/)__
    In order to gain programmatic access to Google Maps and Geocode mapping, I used Google API Services.

* __[Google API's](https://developers.google.com/docs/api/)__
    In order to gain programmatic access to Google Maps and Geocode mapping, I used Google API Services.

* __[Font Awesome](https://fontawesome.com/icons/)__
    All the fonts used on the application is from Font Awesome.

# Deployment

A live version of the site can be found [here](https://go-playground.herokuapp.com/find_playground). 
Used [Git](https://github.com/) for version control. For deploying my project to a hosting platform, 
I used Heroku. After creating an account with Heroku, I then created an app/dyno using a unique name 
that has not already been used by someone else. With evey code amendment, I would add and then commit those 
changes to my GitHub repository. In turn, I would push my amended code to Git and also to Heruku. 

If I add or update an existing library for a specific functionality, I would then use the command: 
pip3 freeze > requirements.txt which updates the requirements.txt file with all changes made. This is 
so Heroku knows which modules to use when running the application. On Heroku settings, I set the IP and PORT 
variables to link my app with Heroku.

My code can also be run locally using the GitPod IDE. On the _gitpod /workspace/go_playground terminal, I type 
the command: python3 app.py in order to run my app locally.


# Testing:

* Developed, tested and debugged the app on [Google Chrome](https://www.google.co.uk/intl/en_uk/chrome/) browser. 
  Kept responsiveness tests regular, on creating a new functionality I would ensure app works well on different 
  devices by changing viewport on Dev Tools.

* Spelling, Grammar, Punctuation
  Checked for typos, grammar, and proper punctuation throughout all site pages. 

* Fonts
  Went through the copy checking to see that the formatting is consistent, checked for odd blips in the copy.

* Title Tags
   Every page has a unique and HTML corresponding title tag. 

* Social Media Integration
   All social media icons on the site go to the correct pages. Social Media buttons are easily identifiable and 
   located on the footer of every page.

* Site Loading Speed 
   Using Google [Test My Site](https://www.thinkwithgoogle.com/intl/en-gb/feature/testmysite/) I was able to 
   test the loading speed on mobile 4G devices and it is average, within 2 seconds. 

* Used [Code Beautify ](https://codebeautify.org/) to validate and format my code. 

* Bugs/Problems Encountered
  When I was still using AWS Cloud9, sometimes the IDE would run a line of code even though that bit of
  syntax was commented out. That was only happening on the app.py file.

# Credits

### Content
T

### Media:
Some photos were obtained from www.unsplash.com but most have been web links from different sources
online.

### Acknowledgements




