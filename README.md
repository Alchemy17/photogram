# APP NAME

### Not Instagram Clone

## AUTHOR

Abdulrahman Mohamed

## DESCRIPTION

This is an application that is just nothing like the popular social media platform Instagram where users can sign up, post pictures,
view pictures posted by others, comment on them and like/dislike the pictures.


## User stories
As a user can do the following:
* Sign in to the application to start using
* Upload pictures to the application.
* View their profiles containing all their pictures
* A user can Follow other users and see their the users  timeline.
* Like a picture and leave a comment on it.

## Set Up and Installation

#### Prerequisites

* Python 3.6.3
* Virtual environment
* Postgres Database
* Reliable Internet Connection

## Installation Process

* Copy repolink

in your terminal run the following commands

* $ git clone REPO-URL in your terminal
* $ cd Instagram_clone
* $ python3.6 -m venv virtual
* $ touch .env ( to the file add :
        SECRET_KEY=<your secret key>
        DEBUG=True)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt
* $ psql ; CREATE DATABASE instagram;

In the settings.py module of the project make the following changes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'instagram',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}

* $ python3.6 manage.py runserver (this command runs the application of port http://127.0.0.1/8000 or http://localhost:8000 )
 
## Known Bugs

No known bugs

## CREDITS

Moringa School,Python Documentation, StackOverflow.com, PrettyPrinted, Learning Website Development with Django by A Hourieh and W3 schools

## Technologies Used

This project uses major technologies which are:

* HTML5/CSS
* Bootstrap4
* Python3.6
* Django Frame Work
* Postgress Database

## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me mail maanoatu17@gmail.com.

## License 

Copyright MIT [LiCENSE](./LICENSE) (c) 2017 [Abdulrahman Mohamed](https://github.com/Alchemy17)

