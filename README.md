# Neighborhood

## Description
NeighborHoodApp allows you to be in the loop about everything happening in your neighborhood.
A user can:

Sign in with the application to start using.\
Set up a profile about you, a general location and your neighborhood name.\
Find a list of different businesses in your neighborhood.\
Find Contact Information for the health department and Police authorities near my neighborhood.\
Create Posts that will be visible to everyone in your neighborhood.\
Change your neighborhood when you decide to move out.
## BDD
#### Given
A user living in a neighborhood
#### When
They require an emergency contact,details of firms in the proximity and other neighborhood information or wish to post certain information to the residents of the area
#### Then 
They can use neighborhood app to pass or find such information
## Author
Sheila N.K.

## Set up instructions
### Requirements
##### 1. Clone the repository
Clone the the repository by running

###### git clone https://github.com/SheilaKamotho/Neighborhood.git
or download a zip file of the project from github

Navigate to the project directory

###### cd Neighborhood
##### 2. Create a virtual environment
Install Virtualenv

###### pip install virtualenv
To create a virtual environment named virtual, run

###### virtualenv virtual
To activate the virtual environment we just created, run

###### source virtual/bin/activate
##### 3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress

###### $ psql
Then run the following query to create a new database named Neighborhood

###### Create database Neighborhood
##### 4.Install dependencies
To install the requirements from requirements.txt file,

###### pip install -r requirements.txt
##### 5.Create Database migrations
Making migrations on postgres using django

###### python3 manage.py makemigrations myapp
then run the command below;

###### python3 manage.py migrate
##### 6.Run the app
To run the application on your development machine,

###### python3 manage.py runserver
##### 7. Running Tests
To run tests;

###### python3 manage.py test

## Technologies Used
Django\
Python\
Html\
Css\
Bootstrap

## Bugs
There are no know bugs at the moment

## License and Copyright information.
*{MIT License Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.}* Copyright (c) {2020} {Sheila Kamotho}

## Collaboration Information
Clone the repository\
Make changes and write tests\
Push changes to github\
Create a pull request

## Contact Details
kamothosheila@gmail.com


