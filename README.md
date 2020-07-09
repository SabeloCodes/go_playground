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

A live version of the site can be found [here](https://go-playground.herokuapp.com/find_playground). 
Version control was done using git.


* Font Awesome
  https://use.fontawesome.com/releases/v5.3.1/css/all.css
  Used to create uniform fonts for the website social media footer

* Validators
  Used an HTML [validator](https://validator.w3.org/) to check the code for syntax errors
  CSS [checker](http://csslint.net/) used to check the styling

* Formatter
  An HTML[formatter](https://htmlformatter.com/) was used


Testing:

1. Spelling, Grammar, Punctuation
   Checked for typos, grammar, and proper punctuation throughout all site pages. 

2. Fonts
   Went through the copy checking to see that the formatting is consistent, checked for odd blips in the copy.

3. Live URLs
   All links to external websites, other webpages within the site and links to images have been checked and verified that 
   they work properly. Clicked on every link to make sure it is going to the correct page, also made sure that links that are 
   meant to open in another page have the target="_blank"


4. Title Tags/Meta Data
   Made sure that every page has a unique and HTML corresponding title tag. 

5. Compatibility
   Tested the website on Google Chrome, Firefox Mozilla and Safari for compatibility.

6. Images
   The images do not display text renders when hovered over, but all the alt attributes are there. Every image displays 
   correctly. All images posted are formatted as jpg with only one exception for the ARB link image which is a PNG. 
   All photographs are stored as JPG, and the ARB logo is a simple image/icon and stored as a PNG.

   The photographs on the projects.html page load slightly slower depending on the browser used. I think it is because of the 
   size but I haven’t worked out how to solve that issue.

7. Social Media Integration
   All social media icons on the site go to the correct pages. Social Media buttons are easily identifiable and located on 
   the footer of every page.

8. Site Loading Speed & Responsive
   Using Google Test My Site I was able to test the loading speed on mobile 3G devices and it is good - within 2 seconds. 
   I also tested the responsiveness of my site with the toggle device bar on the Google inspect page.


9. Tested my CSS with CSS [Lint validator](http://csslint.net/) for any syntax errors or unnecessary code DRY. 
   Did the same for the HTML, using [HTML](https://htmlformatter.com/) checker. Using Google Chrome Developer Tools I was 
   able to look and play around with different aspects of my code, like the grid spacing. In doing so I eventually can 
   settle on a design feature. I also used the tools to make sure my Mobile first approach worked, ie. testing on different 
   devices.


Deployment
Having started working on the website skeleton locally on my computer, using Atom code editor. I then created a repository on 
GitHub, this is where I have deployed my code. Once all my code is on the GitHub repository, I went on editing the project. 
Every time I make a change, I follow up by staging the changes and then committing them.

Social-Links & Nav-Titles:
Used the same CSS hover styling for both in order to have a recognizable theme.

Bugs/Problems Encountered
My footer kept on twitching to the right every time I clicked on one of the grid items. Solved by making the img logo position: 
relative.

Had an issue where the video would continue playing the sound even after its been closed. Wrote a JavaScript function to make 
sure the video (including sound) completely stops when video is closed.  

Credits
Content
T

Media:
Some photos were obtained from www.unsplash.com but most have been web links from different sources
online.

Acknowledgements




