# Holiday Dreams

This is a Web App where a user can read about peoples adventures of holidays they have experienced and also comment,
or like the post as well as post there own Dream Holiday experience.

The goal is to make the user aware of prices in different locations and what baggage people have taken in the different seasons.

Also see what locations and experience you as a adventurer would like to experience

## [Click here to view website](https://holiday-dreams-c63c9b39c29f.herokuapp.com/)

![Am I Responsive]()

# About Holiday Dreams

1. Create a space where people with the same interest can share the experiences and opinions 
2. Create an environment that gives users some insight of planing there next holiday  
3. Share your holiday experience with others
4. A place that is created only for holiday bloggers


# UX

## User Stories

- First-time visitor

  - Clear visually appealing landing page that is descriptive
  - All posts have are displayed with a big image that will catch the attention of a user
  - Nav bar clearly showing how many pages there are
  - Can open a post and read it but can not comment or like it unless singed in

- Returning visitor

  - Will want to create an account 
  - Will post there own user posts 
  - Will comment and like other users post 
  - Will read a post or comment, like a blog on there spare time they have 

- Frequent user

  - Will want to sing up for the newsletter and competition
  - Will use the blogs info to make a informed decision of their next holiday
  - Will be a user that likes to blog regularly 

## Strategy

This Web App is created to provide a community of holiday bloggers sharing all there experiences of there travels,
other user will live some of these experiences trough reading other bloggers posts, as well create some of there own memories.

In the grand scheme of connecting people that share the same interest in traveling

## Scope

The Webb App Will :

- Have clear descriptive prompts and notifications 
- Allow a user to create an account
- Let a user log In or Log out
- Let a create a post 
- Let the user have full CRUD functionality of there own posts
- Let the user comment on like another user post
- Let the user have full CRUD functionality of there own comments
- The user will be able to sing up for a news letter as well be entered into a draw 

## Structure

The Webb App will be structured around full user experience in mind making posting simple and creating a community of holiday bloggers

## Wire Frames 

I have created a wire frame of what I expected the Webb app to look like, but as development was carried out I have made some changes to the design which was more practical and appropriate for what the web app 

<details>
<summary> Home Page
</summary>

![Home Page](assets/images/whome.png)
</details>

<details>
<summary> About Page
</summary>

![About Page](assets/images/wabout.png)
</details>

<details>
<summary> Login Page
</summary>

![Login Page](assets/images/wlogin.png)
</details>

<details>
<summary> Sing Up Page
</summary>

![Sing Up Page](assets/images/wsignup.png)
</details>

<details>
<summary> User Logged in Page
</summary>

![User Logged in Page](assets/images/wulogin.png)
</details>

<details>
<summary> User Logged in Reading Post Page
</summary>

![User Logged in Reading Post Page](assets/images/ulpost.PNG)
</details>

<details>
<summary> User Create a Post Page
</summary>

![User Create a Post Page](assets/images/ulcreatepost.png)
</details>

<details>
<summary> User Profile Posts Page
</summary>

![User Profile Posts Page](assets/images/ulmyposts.png)
</details>


## Database diagram

This is a diagram of the models it has been altered during development and not all models were implemented and others where created instead to create a more user friendly experience.
The recommendation model was removed and instead some of the fields was incorporated into the post field it made more sense to me at the time to do it this way after with full user UX in mind.
I have added a Like model after to create a user interaction with a post.


<details>
<summary> Database diagram
</summary>

![Database diagram](assets/images/db-diagram.png)
</details>


## Data Models

1. AllAuth user Model 
- It is a default model used by Django authentication
- It comes with Standard login user authentication promoting the user to log in or sign up
- Is is a one to many relationship with user post as the user can have many post but the post has only one author, each post will be authenticated to see if the user is logged in and singed up (checks if the user exists)

2. Post model
- Is is a one to many relationship with user post as the user can have many post but the post has only one author 
- the post model will prompt a user to populate some fields from the user's end but will also have a few auto filled fields 
- The author field will be used as a ForeingKey tht will be the main link to a user
- Fields the user can fill out are title, holiday_season, holiday_length, experience, bag_recommendation, excerpt cost_expected, featured_img
- Fields that will be auto generated author, slug, created_on, status, updated_on 

3. Comment model
- Will allow a verified log in user to comment on another user post
- This is a many to many relationship towards a post but a many to one relationship regards to a single user
- This model will use post and author as foreigner for verification of a user as well as linking the comment to the user that left the comment
- The body field will be populated by the user
- created_on Will be auto generated with a time and date of when a user made a comment

4. Like model
- The user and post field are ForeingKeys used to insure a user can only like a post once but a post can be liked by many users
- This is a many to many relationship towards a post but a many to one relationship regards to a single user

5. About Model 
- It has fields that can only be populated by a superuser to maintain a high standard of the Web app
- It will give the superuser the ability to add a custom about picture as well custom about description 

6. Subscribe model
- The fields of this model will be populated by a user 
- The information the user submits will only be accessible by the superuser as this may be sensitive data

## Agile Methodology

This the principal I used creating the Wbb App focussed on users stories and would only be marked as complete when t the user stories was met to a satisfactory standard 

### Epics

Epics where used to categorize the different user stories 
- Epic 1 : Visitor
- Epic 2 : User
- Epic 3 : Administrator and site management

The user stories would also have task that needs to completed and this is categorized by using
- Must have
- Should have 
- Could have

However I could have payed more attention to this board and update progress on it more frequently which I will do in the future

[Project Board](https://github.com/users/IainJackson90/projects/3)

<details>
<summary> User Stories Template
</summary>

![User Stories Template](assets/images/template.png)
</details>

<details>
<summary> User Stories Issues
</summary>

![User Stories Issues](assets/images/issues.png)
</details>

<details>
<summary> Project Board
</summary>

![Project Board](assets/images/project-board.png)
</details>



## Color pallet of the App
I created the Webb App with the mindset of creating a relaxing ambiance by using natural neutral colors that give you a feeling of having a holiday ith good weather and gets you not too overwhelmed and hopefully gets the user to blog or read some post.
I used three colors in this web App and tried sticking to the 60, 30, 10 rule of using colors.

- Ten percent more or less of the color #34A426
- Ten thirty more or less of the color #48817A
- Ten sixty more or less of the color #3C8CA7

<details>
<summary> Color pallet
</summary>

![Color pallet](assets/images/holiday-dreams-colors.png)
</details>

# Features

Each Feature was designed to be as user friendly as possible with a clear direction of what is expected from them trough use of visual notifications
All these feature ma differ dependant on the size of the device being used to view the web app

## Existing Features

<details>
<summary> Nav Bar
</summary>

![Nav Bar](assets/images/nav-bar.png)
</details>

- The Navbar will be displayed right at the top of each page
- Once  click on the Holiday Dreams logo it will redirect the user back to the home page 
-  The Nav bar at the top of the page has the logo as well as the navigation tabs as well as the slogan on the far right
- The Page tab you are on will be displayed in a darker font
- The slogan on the far right has no functionality 

<details>
<summary> Hero Image
</summary>

![Hero Image](assets/images/hero-image.png)
</details>

- The hero image is visually descriptive setting a ambience of adventure and relaxation as wel as traveling and holiday vibes
- At the top of the hero image on th far right will be a notification displayed in green to notify the user if they are logged in or not 
- In hte centre of the hero image is a short description of what to expect from the Web App
- The button on the hero image will let a signed in user add there own post but if you have not singed int the button will direct the user to the log in or sign up page

<details>
<summary> Notifications
</summary>

![Notifications](assets/images/notification.png)
</details>

- Whenever the user logs in, logs out perform any kind of CRUD functionality there will be a notification pop up informing them of any changes they have made 
- The message will be clear of the type of action that has been performed by the user 


<details>
<summary> Model
</summary>

![Model](assets/images/deletemodel.png)
</details>

- Whenever the user wants to delete any post or comment a model will pop up confirming the user with a message of the action they are doing and if they are sure they want to continue with this action 
- The buttons on the model change colors when you hover over them

<details>
<summary> Posts
</summary>

![posts](assets/images/posts.png)
</details>

- The Body of the page under the hero image is where all the post will displayed with captivating images in a libary style effect to draw a user attention to the posts
- The post will display from the latest to the oldest posts
- On each image will be a banner at the bottom left displaying the author of the post
- Under the image will be a title of of the post 
- Under the title will be as hort excerpt of what you could expect of reading the post
- Under the excerpt will be a line separating the time and date the post was published as wel as how many likes the post have got
- When you hover over the excerpt text it will change color to green  

<details>
<summary> Create a post
</summary>

![Create a post](assets/images/createapost.png)
</details>

- When the user clicks on the create a oust button it will direct them to the CREATE A POST page
- This page has field so be populated by the blogger and is created for a more serious blogger giving them all the tools they need to create the perfect blog 
- Some of the text field will have text editing tools
- The blogger can add a image for the home page 
- The submit and cancel button changes colors when hover over them

<details>
<summary> Reading a post
</summary>

![Reading a post](assets/images/postreadtop.png)
</details>

- At the top of each post when opened you will introduced by banner with the title and the author who created the post as well as a image the author has added


<details>
<summary> Reading a post At the bottom
</summary>

![Reading a post At the bottom](/assets/images/bottomofpost.png)
</details>

- At the bottom of a post created by the author will be two buttons that will give them a option to edit or delete the post they have created.
These buttons will ot be visible to any other user that is not the creator of the post, they also change color when you hover over them 
- There is a like icon that is not a full color red if the user did not click on it once it has been clicked on it will change color to a full red and the count next to it will increase by one this can only be done once on a post per user if it is clicked again it will remove one count on the counter as well change color back to a empty red color.
You can only use the like button if you are logged in as a user
- Next to the like icon there is a comment icon with a counter next to it displaying how many comment the post has
- Underneath the icon separated by a line are the comments posted by other users with the user name as well as the time and date it was created
- The delete and edit button will only be visible to the author of the comment giving them full Crud functionality of there comments, the buttons change color when you hover over them
- On the right is text area only visible if you are logged in as a user giving you the opportunity to submit a comment the submit button also changes color when you hover over it 
- Each comment posted will increase the comment counter and each comment deleted will remove a count off the comment counter 

<details>
<summary> Footer
</summary>

![Footer](assets/images/footer.png)
</details>

- At the bottom of the page above the footer will be a button that will help you navigate trough the pages to older posts that hse been created( A page will need nine post before it will create another page)
- When you hover over the button the text will to change color to green
- The footer has all the social media links that will direct you the social accounts of this Web App 
- When you hover over the social icons they will pop up with a zoom in effect

<details>
<summary> About Page
</summary>

![About Page](assets/images/aboutpage.png)
</details>

- The about page will have a description of what the Webb App is about also with a timestamp when last the about content last was updated 
- There are some fields that if the user wants to sign up for the news letter they could do so
- the submit button changes color when you hover over it

<details>
<summary> Sing Out Page
</summary>

![Sing Out Page](assets/images/signout.png)
</details>

- If the user wants to log out they will be directed to the Sign out page 
- The button changes color when you hover over it

<details>
<summary> Sing In Page
</summary>

![Sing In Page](assets/images/signin.png)
</details>

- When a user wants to sign up or log in they will be brought to this page
- The sing up displayed in a different color is a link to a sign up page 
- The color of the button changes color when you hover over it

<details>
<summary> Sing Up Page
</summary>

![Sing Up Page](assets/images/signup.png)
</details>

- When the user clicked on the sign up link on the Sing in form it will direct them to this page
- This page will prompt the user with clear information of what is required from the to create an account

<details>
<summary> 404 - Page not found page
</summary>

![404 - Page not found page](assets/images/pagenotfound.png)
</details>

- This is a custom 404 page not found page that will appear if the user request a page that can not be found
- It displays a clear message to the user of what just happened
- The button will redirect the user to the home page
- The button changes color when you hover over it 

<details>
<summary> 500 - Internal server error page
</summary>

![500 - Internal server error page](assets/images/internalservererror.png)
</details>

- This is a custom 500 internal server error page that will appear if there is a server error
- It displays a clear message to the user of what just happened
- The button will redirect the user to the home page
- The button changes color when you hover over it 

## Future Features

 

# Testing



## Known Bugs



## Fixed Bugs



## Manual Testing

| What was tested | Result | Outcome |
|:---:|:---:|:---:|
|------------|-----------|------------|
|------------|-----------|------------|
|------------|-----------|------------|
|------------|-----------|------------|
|------------|-----------|------------|
|------------|-----------|------------|
|------------|-----------|------------|
|------------|-----------|------------|

![Manual Testing]()

## Validator Testing



![Validator Testing]()

# Deployment

1. Login to Heroku
2. On the Heroku dashboard click on 'New'
3. Select 'Create New App'
4. Add an app name (Must be a unique name) and select your region
5. Click 'Create App'
6. On the next page at the top click 'Settings' then 'Config Vars'
7. Click 'Reveal Config Vars' ....................................
8. Scroll down and click 'Buildpack' ......................
9. 'Add'.............................
10. At the top of the page again, click 'Deploy'
11. Click on 'Github' as your deployment method
12. Search the relevant repo and link these
13. Once linked, select 'Automatic deploys from' or 'Manual Deploy'
14. The app will now be hosted on Heroku.

- ## _Cloning the GitHub repository_

This will download a full copy to your desktop

1. Log into GitHub
2. Find the repository you wish to clone
3. Find the green code button top right corner
4. Select "Local", copy the HTTPS URL
5. Go to Codeanywhere and navigate to "New Workspace"
6. Paste the URL into the space provided
7. Click "Create"

- ## _Forking the GitHub repository_

Will allow you to create a copy of the repository so changes can be made that will not affect the original repository.

1. Log into GitHub
2. Find the repository you wish to fork
3. Find the "Fork" drop down in the top right corner second from last
4. Select "Create"  

# Technologies Used

- []() to write the code
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) main language used
- [Git](https://git-scm.com/) Version control
- [Github](https://github.com/) storing files online and for deployment
- [Heroku](https://www.heroku.com/) to deploy the WebApp
- [CI Python Linter](https://pep8ci.herokuapp.com/) Validate the code
- [amiresponsive](https://ui.dev/amiresponsive) to check responsiveness
- []() for logo
- []() to create flow chart
- [Snipping Tool](https://freesnippingtool.com/download) to create sniped images

# Credits

- Code Institute for the learning content provided
- Harry Dhillon my assigned mentor to give advise on the project
- Nicole Jackson my wife a student at code institute for constructive criticism
- Slack community
- [stackoverflow](https://stackoverflow.com/questions/26260950/how-can-i-randomly-choose-a-maths-operator-and-ask-recurring-maths-questions-wit ) guidence of project 
- [w3schools](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_random_randint) -------------
- []() ----------------
- [stackoverflow](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal) ----------- 