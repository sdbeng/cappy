# cappy endpoints
` / and /coolkids`

## save dependencies

In order to save our package requirements we'll use the following command:
```
pip freeze > requirements.txt
```
Pip freezing is a process in which pip reads versions of all packages in the current virtual environment and saves them to a text file. In our case,this is the text file that Heroku will use to install dependencies.

Be advised: the requirements.txt file does not automatically update if you install a new library. It's like a snapshot - any changes after aren't reflected in a past snapshot. You'll want to ensure requirements.txt is up to date before pushing your app to Heroku.

If you want to learn more about pip, check out this segment of Websauna documentation.[https://websauna.org/docs/tutorials/deployment/freeze.html]
