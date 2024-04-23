### EcomMobile Web Application 

# Starting Server
Create .env file in root directory with below contents. 

DEBUG=True
Then, start the server with this command.

# install dependencies
pip install -r requirements.txt

# create database
python3 manage.py parse_csv

# run server
python3 manage.py runserver 8000

# run server in Codio
python3 manage.py runserver 0.0.0.0:8000

# create files for migration
python3 manage.py makemigrations

# execute migration
python3 manage.py migrate

## EcomMobile Web Application
