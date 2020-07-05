# Go Playground - Milestone Project 3

This is a web application primarily targeted for people with young families. The website provides a simple easy-to-use 
method for locating and creating a playground location nearest to you. 

UX


Mockups

![Index page](/static/images/wireframes/AddPlayground.png)
<!-- <img src="/static/images/wireframes/AddPlayground.png"> -->
<img src="/static/images/wireframes/BrowsePlayground.png">
<img src="/static/images/wireframes/EditPlayground.png">
<img src="/static/images/wireframes/Home.png">
<img src="/static/images/wireframes/ShowPlayground.png">


Existing Features

playground.html


* Company logo
  Playful and simple in colours and font. Positioned on the top left of the banner where it greets the 
  website visitor.


* Footer
  The bottom of the site has an uncomplicated footer with links to the company's social media networks for interested users


addplayground.html


showplayground.html
  

editplyground.html


browseallplaygrouns.html


Features to be implemented


Technologies Used
* HTML
  Used for the markup

* CSS
  Variant_office/styles.css
  This was used to style the elements of the HTML code

* Bootstrap
  https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css
  Used to assist with styling the website and to build the grid

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




