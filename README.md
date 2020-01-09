# cappy endpoints
` / and /coolkids`

## Save/freeze dependencies to requirements.txt

In order to save our package requirements we'll use the following command:
```
pip freeze > requirements.txt
```
Pip freezing is a process in which pip reads versions of all packages in the current virtual environment and saves them to a text file. In our case,this is the text file that Heroku will use to install dependencies.

Be advised: the requirements.txt file does not automatically update if you install a new library. It's like a snapshot - any changes after aren't reflected in a past snapshot. You'll want to ensure requirements.txt is up to date before pushing your app to Heroku.

If you want to learn more about pip, check out this segment of Websauna documentation.[https://websauna.org/docs/tutorials/deployment/freeze.html]

** Make sure you run `pip freeze > requirements.txt` after each time you install or update a package.**

## Environment Configuration
In previous projects, you used a bash file to set up local environment variables. You'll do the same here. We want them all contained in the same kind of file for easier transfer later to the Heroku interface.

If you're following along in the project, use `touch setup.sh` and set up all of your environment variables in that file.

Most of the work we do for Heroku will be in our application files or the command line. In order to give you some familiarity with the web interface, we'll set up the environment variables there, after we deploy our application. For now, check out the screenshot below to get used to the interface. Once you're in a project's settings, you'll see an option to Reveal Config Vars. Once you click on that, a table similar to that you see below will appear. Here, you define your variables just as you did in the setup.sh file, just without the equals signs!

## Gunicorn
Gunicorn is a pure-Python HTTP server for WSGI applications. We'll be deploying our applications using the Gunicorn webserver.

First, we need to install gunicorn using `pip install gunicorn`. Next touch Procfile to create the file.

Procfile is exceedingly simple. It only needs to include one line to instruct Heroku correctly for us: `web: gunicorn app:app`. Just make sure your app is housed in app.py as it is in the project.

## Database Manage & Migrations on Heroku
In the data modeling course, you learned how to use migrations to manage your database schema and changes that you make to it. Heroku can run all your migrations to the database you have hosted on the platform, but in order to do so, your application needs to include a manage.py file.

We'll need three new packages in the file. Run the following commands to install them:
```
pip install flask_script
pip install flask_migrate
pip install psycopg2-binary
```

## run migrations
local migrations once
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

then:
```
heroku run python manage.py db upgrade --app name_of_your_application
```