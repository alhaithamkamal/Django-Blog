## Django Blog Project

<img src="https://i.ibb.co/SwsT9sK/bg-1.jpg" alt="bg-1" border="0">
- This is a small django blog application created by OS40 ITI Alexandria students.
- The project consists of 3 apps [Users , Posts , Manager] each of which handles some required functionalities for instance handling users registration and login , posts creation , comments , likes and dislikes and much more.

### Contributers

#####1. Al Haitham Kamal [categories , tags ] + admin app
#####2. Hagar Abdou [posts , likes , dislikes] + admin app
#####3. Jihad Samir [comments , replies] + admin app
#####4. Abd Allah Zidan [users app ] + admin app

### what can users do

- Anyone can visit the blog without logging in and see the posts but can't like or comment on any of them.
- logged in normal user can view posts , comment on them , like or dislike
- logged in admin user can do crud operations on normal users , post and the other project parts except controlling other admins
- logged in super user can control anything in the blog even admins but can't control other super users

### [ Users app ]

#### Users app handles all the following:

1. provide an easy and secure way to register new users.
   ![](https://i.ibb.co/LzdStDy/sinup1.png) ![](https://i.ibb.co/fNyFKDW/sinup2.png)
2. handles users login , logout and authentication and check if user is registered but blocked and redirects him to another page tells him he is blocked and shall contact one of the admins listed for him and provide admins names and emails.
   ![](https://i.ibb.co/mBCKx0v/login.png) ![](https://i.ibb.co/F06MHsP/logout.png)
3. a blocked user cannot login but he is registered and still exist in users table for to be unblocked by admins any time they need.
   ![](https://i.ibb.co/DWZg80J/blocked.png) ![](https://i.ibb.co/sRG3zGK/lock-confirm.png)
   ![](https://i.ibb.co/6H9rw7x/unlock.png)
4. user with wrong credinitial or unregistered will not login and error message will appear telling him the provided login data is incorrect.
   <img src="https://i.ibb.co/McPJYh9/incorrect.png" alt="unique-mail" border="0">
5. if a user is already logged in and tries to navigate to login page or registration page manually through url he will be redirected to home page again .. not to authenticate the same user twice.
6. login uses django authentniation system {username and password} but as long as the default django behaviour is to check only for username uniqueness .. another validation was added to prevent duplicate emails in different accounts [ unique email for each user]
   <img src="https://i.ibb.co/vZgBQGZ/unique-mail.png" alt="unique-mail" border="0">
7. whenever a new user resgisters himself with valid data he logs in automatically and a message is sent to his email welcomes him to the blog.
   <img src="https://i.ibb.co/x2CS60N/registeremail.png" alt="registeremail" border="0">

8. each time a user subscribes to a new category an email message will be sent to his email address to tell him that he subscribed to that category.
   <img src="https://i.ibb.co/sVw5hYp/subscribe.png" alt="subscribe" border="0">
9. if user forgets his password he can easily write his email address and an email message will be sent to him with a link to reset his password.
   ![](https://i.ibb.co/Tt5BFJK/reset1.png) ![](https://i.ibb.co/fq5hpjr/reset2.png) ![](https://i.ibb.co/6t99kDL/email-reset.png)
   ![](https://i.ibb.co/gdzbdRB/reset4.png) ![](https://i.ibb.co/Ht6MPFr/reset5.png)
10. normal users can't see links to manage blog app but even if they know the url and write it manually .. they get redirected to the homepage again as they aren't authorized to visit that app.
11. admin users are 2 types ( super user with the highest privileges (except on another super user) and normal admin user who can control only posts and normal users.
    ![](https://i.ibb.co/qysHM66/login-admin.png) ![](https://i.ibb.co/SmZp4Nb/admin-panel.png)
    ![](https://i.ibb.co/hYqTpp7/admins.png) ![](https://i.ibb.co/4fTswCq/normal-admin.png)
12. many more feature you can find when running the project.

## Setting things up before running the project

1. you need to set up your prefered database system in the settings.py file .
2. python3 manage.py makemigrations [each app]
3. python3 manage.py migrate
4. create a super user usin [pytthon3 manage.py createsuperuser]
5. run the app using [python3 manage.py runserver]
6. you need to create a folder called media in the project folder to upload images to it and recommended to add a default image with that name [defaultImage.png] to be given as a profile pic for users who don't upload profile pics.
