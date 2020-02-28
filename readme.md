## Django Blog Project

<img  src="https://i.ibb.co/SwsT9sK/bg-1.jpg"  alt="bg-1"  border="0">

- This is a small django blog application created by OS40 ITI Alexandria students.

* The project consists of 3 apps [Users , Posts , Manager] each of which handles some required functionalities for instance handling users registration and login , posts creation , comments , likes and dislikes and much more.

### Contributers

##### 1. Al Haitham Kamal [categories , tags ] + admin app

##### 2. Hagar Abdou [posts , likes , dislikes] + admin app

##### 3. Jihad Samir [comments , replies] + admin app

##### 4. Abd Allah Zidan [users app ] + admin app

### what can users do

- Anyone can visit the blog without logging in and see the posts but can't like or comment on any of them.

* logged in normal user can view posts , comment on them , like or dislike

- logged in admin user can do crud operations on normal users , post and the other project parts except controlling other admins

* logged in super user can control anything in the blog even admins but can't control other super users

### [ Users app ]

#### Users app handles all the following:

1. provide an easy and secure way to register new users.

<img  src="https://i.ibb.co/8DgM5nw/sinup1.png"  alt="sinup1"  border="0"> <img  src="https://i.ibb.co/941gfZ0/sinup2.png"  alt="sinup2"  border="0">

2. handles users login , logout and authentication and check if user is registered but blocked and redirects him to another page tells him he is blocked and shall contact one of the admins listed for him and provide admins names and emails.

###### login and logout

<img  src="https://i.ibb.co/8BDwhbz/login.png"  alt="login"  border="0">
<img  src="https://i.ibb.co/gPyp4vn/logout.png"  alt="logout"  border="0">

3. a blocked user cannot login but he is registered and still exist in users table for to be unblocked by admins any time they need.

###### blocked users

<img  src="https://i.ibb.co/NCPYbP9/lock-confirm.png"  alt="lock-confirm"  border="0">

<img  src="https://i.ibb.co/MSm5GFv/blocked.png"  alt="blocked"  border="0">

<img  src="https://i.ibb.co/x19XLt0/unlock.png"  alt="unlock"  border="0">

4. user with wrong credinitial or unregistered will not login and error message will appear telling him the provided login data is incorrect.

###### incorrect

<img  src="https://i.ibb.co/1rR4Dnb/incorrect.png"  alt="incorrect"  border="0">

5. if a user is already logged in and tries to navigate to login page or registration page manually through url he will be redirected to home page again .. not to authenticate the same user twice.

6) login uses django authentniation system {username and password} but as long as the default django behaviour is to check only for username uniqueness .. another validation was added to prevent duplicate emails in different accounts [ unique email for each user]

###### unique email

<img  src="https://i.ibb.co/vZgBQGZ/unique-mail.png"  alt="unique-mail"  border="0">

7. whenever a new user resgisters himself with valid data he logs in automatically and a message is sent to his email welcomes him to the blog.

###### registration email

<img  src="https://i.ibb.co/x2CS60N/registeremail.png"  alt="registeremail"  border="0">

8. each time a user subscribes to a new category an email message will be sent to his email address to tell him that he subscribed to that category.

###### subscribe email

<img  src="https://i.ibb.co/sVw5hYp/subscribe.png"  alt="subscribe"  border="0">

9. if user forgets his password he can easily write his email address and an email message will be sent to him with a link to reset his password.

###### forgot password

<img  src="https://i.ibb.co/4pxZ5Cs/reset1.png"  alt="reset1"  border="0"><img  src="https://i.ibb.co/34qDNgS/reset2.png"  alt="reset2"  border="0"> <img  src="https://i.ibb.co/NNDDMWb/email-reset.png"  alt="email-reset"  border="0">

<img  src="https://i.ibb.co/C6hp6HT/reset4.png"  alt="reset4"  border="0"> <img  src="https://i.ibb.co/qNK4gyR/reset5.png"  alt="reset5"  border="0">

10. normal users can't see links to manage blog app but even if they know the url and write it manually .. they get redirected to the homepage again as they aren't authorized to visit that app.

11) admin users are 2 types ( super user with the highest privileges (except on another super user) and normal admin user who can control only posts and normal users.

##### adminstration

<img  src="https://i.ibb.co/FxwQbpp/login-admin.png"  alt="login-admin"  border="0"> <img  src="https://i.ibb.co/DMjnH4h/admin-panel.png"  alt="admin-panel"  border="0">

<img  src="https://i.ibb.co/1zS4HHv/admins.png"  alt="admins"  border="0"> <img  src="https://i.ibb.co/c6GWYNK/demote.png"  alt="demote"  border="0">

<img  src="https://i.ibb.co/5LdyNMJ/promotesuper.png"  alt="promotesuper"  border="0"> 
<img  src="https://i.ibb.co/XtV0xvh/cannot-manage.png"  alt="cannot-manage"  border="0">
 <img  src="https://i.ibb.co/Jd7xW81/normal-admin.png"  alt="normal-admin"  border="0">  <img  src="https://i.ibb.co/qRxmt8b/show-user.png"  alt="show-user"  border="0">

11. a logged in user can edit his profile data , change his name , bio , profile picture and also if he knows the old password can change it to a new one.

<img  src="https://i.ibb.co/0ZhgVpp/profile.png"  alt="profile"  border="0">

<img  src="https://i.ibb.co/dW3jSC9/edit-profile.png"  alt="edit-profile"  border="0">

<img  src="https://i.ibb.co/HHDNwLH/change-pass.png"  alt="change-pass"  border="0">

12. many more feature you can find when running the project.

## Setting things up before running the project

1. you need to set up your prefered database system in the settings.py file .

2) python3 manage.py makemigrations [each app]

3. python3 manage.py migrate

4) create a super user usin [pytthon3 manage.py createsuperuser]

5. run the app using [python3 manage.py runserver]

6) you need to create a folder called media in the project folder to upload images to it and recommended to add a default image with that name [defaultImage.png] to be given as a profile pic for users who don't upload profile pics.
