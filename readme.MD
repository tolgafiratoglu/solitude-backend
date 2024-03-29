<b>Solitude</b> is a practice project, an open source Kafka GUI based on Django and React/Hooks. Please refer <a href="https://github.com/tolgafiratoglu/solitude">main package</a> for more.
Solitude is a practice project, developed for educational purposes. Solitude doesn't support brokers and topics with authentication and not intented to be used in production environment. 

<h1>Installation</h1>
After clonning the repository:

1. We suggest you to create a virtual environment
2. Install reqiurements:

```
pip install -r requirements.txt
```

3. Create a super user:
You need to create first super user, which will be able to access admin panel.

```
python3 manage.py createsuperuser
```

4. Run server:
When you run server, admin and api will be up, if migrations are ready.

```
python3 manage.py runserver
```

5. Add clusters and brokers from admin:
In solutide, you'll need to define clusters and brokers from admin panel. 

After this step, you'll be able to view topics, create topics, partitions and/or create additional partitions for topics. 

Note that: Creating topics and adding new partitions are limited with the admin user.

6. Creating application secret.
Copy paste .env.local as .env. You will need to add a new secret has to your application. 

```
python3 -c 'import secrets; print(secrets.token_hex(100))'
```

Get the output string and add it to your .env file. 