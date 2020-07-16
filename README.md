## Django Rest API Skeleton

### Set The Database Engine & Name
	django_for_apis/
		django_for_apis/
			settings.py
			
				DATABASES = [...]
				/* Modify this with your needs */

### Make Sure The Database Exists

* For PostgreSQL

		$ createdb <database_name>
	

### Create Virtual Environment & Activate ( Optional )

	$ virtualenv venv -p python3
	$ source venv/bin/activate
	
### Install Required Modules

	$ pip3 install -r requirements.txt
	
				
### Migrate
	(django_for_apis/) $ python3 manage.py migrate
	

### Create Super User
	$ python3 manage.py createsuperuser
	$ python3 manage.py drf_create_token <superuser_username>
	
### Run The Server
	$ python3 manage.py runserver
	
### APIs

* User Creation

		POST http://localhost:8000/secure/users/
		
		{
			"username" : <username>,
			"password" : <password>,
			"email" : <email>
		}
		
* User Login

		POST http://localhost/secure/login/
		
		{
			"username" : <username>,
			"password" : <password>
		}