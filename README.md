# TradersIn
## About
This is a blog post for traders where they can share their knowledge and expertise and also get to interact with one another in the platform.

## Installation
### Requirements
These should be installed in your system:
- Python
- MySQL

#### Create a virtual environment
* Windows
```
  pip install virtualenv
  virtualenv .venv
  .venv/Scripts/activate.bat
````
* Linux
```
  sudo apt install python3-virtualenv
  virtualenv .venv
  source .venv/bin/activate
```

#### Install site-packages
```
  pip install requirements.txt
```
To configure ```python-decouple```, reference this link: 
[Python Decouple](https://pypi.org/project/python-decouple/)


#### Clone the repository locally
```
git clone https://github.com/LionelMv/TradersIn.git
```

#### Start up the server
```
  python ./SI_RC/manage.py runserver
```
The application should be available at http://localhost:8000 through your browser.

## Author
* Lionel Mwangi, [LinkedIn](https://www.linkedin.com/in/lionelmwangi/)
