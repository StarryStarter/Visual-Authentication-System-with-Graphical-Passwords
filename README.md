# A Visual Authentication System with Graphical Passwords
### During the registration process, users are prompted to upload nine distinct images and arrange them through a drag-and-drop interface to create a unique graphical password. Subsequently, the login mechanism necessitates arranging these images in the correct order. To enhance security, an account will be automatically blocked after four unsuccessful login attempts, thereby ensuring a secure environment while maintaining a user-friendly interface..
# Features :-
## • Image-based Authentication:
### User will upload nine images during registration and then create a unique graphical password by arranging them in a particular order.
## • Randomized images:
### During login, the system presents the user's images in a randomized order, requiring the correct arrangement for authentication.
## • Use of database:
### Use of SQLite through SQLalchemy to store user , user images and their correct order for authentication.
## • Security Measures:
### Account gets blocked after four unsuccessful login attempts.
## • User-Friendly Interface:
### a well designed user friendly interface for the user to use in easily way.
## Technology stack :-
## o Python(for backend)
## o Framework-: flask
## o SQLite,SQLalchemy for database
## o HTML,CSS,JavaScript (frontend)
# How to Use:
## Registration:
### • enter email.
### • Upload nine images.
### • Arrange the images in a specific order.
### • click on submit to save the user.
## Login:
### • Enter the registered email.
### • Arrange the displayed images in the correct order to authenticate by drag and drop.
## Account Security:
### • Images are shown in random order and after every incorrect arrangement they get randomized.
### • Account blocking after four consecutive unsuccessful login attempts.
### • User can not acces dashoboard without getting authenticated.
## Installation
### • from form click on the link https://github.com/StarryStarter/A-Visual-Authentication-System-with-Graphical-Passwords
### • Make sure to install python,flask and Flask_SQLAlchemy.
### • Run app.py and go to http://localhost:5000.
