To start the network builder project, you need to do the following steps

1. Clone the repository using the git clone command
2. In the terminal of your IDE, create a virtual environment using the python -m venv env command
3. activate the virtual environment using the command env/Scripts/activate(for Windows), source env/bin/activate(for Linux)
4. Download the necessary libraries for successful operation of the project using the pip install -r requirements.txt command 
5. Don't forget to migrate using the commands python manage.py makemigrations, python manage.py migrate
6. Don't forget to create a superuser using the python manage.py createsuperuser command 
7. Run the project with the python manage.py runserver command
