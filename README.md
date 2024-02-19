# SoftDesk API

## To install and use SoftDesk API, please follow these steps :

- Clone this repo into the location of your choice.
- Create a virtual environment into the folder of your project `python -m venv env`. 'env' can be replaced by the name of your choice.
- Activate it.
- Run `pip install poetry`.
- Run `poetry install`. These packages will appear :
  ![packages](media/packages.PNG)
- Run `python manage.py migrate`. These migrations will appear :
  ![migrations](media/migrations.PNG)
- Run `python manage.py runserver`