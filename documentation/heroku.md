# How to Deploy on Heroku
Deploying a Django application on Heroku is very easy. This page will walk you through hosting this site on Heroku, as well as updating the hosted site. 

## Starting from Scratch
In this example, we are going to imagine you are starting the hosting process from ground zero. The only material you currently have in-hand is the source code in this repository. <br>
 
1. ___Prerequisites___: <br> 
- Make sure you have [python + pip](https://www.python.org/downloads/) installed
    * You can check this by entering `$ python --version` into the command line
- Make sure you have [git for the command line](https://git-scm.com/downloads) installed
    * You can check this by entering `$ git --version` into the command line
2. __Clone this repository to your local machine__ 
- `$ git clone https://github.com/ShaneCost/metacognitive-tagger.git`
    * Once cloned, open the command line and change directories until you are inside this new directory <br>
3. __Set up Heroku__
- Create/Login to a [Heroku](https://signup.heroku.com/?utm_source=google&utm_medium=paid_search&utm_campaign=amer_heraw&utm_content=general-branded-search-rsa&utm_term=heroku&gad_source=1&gclid=EAIaIQobChMIpu3BzpOshgMVxiWtBh1irQIuEAAYASABEgJ4Q_D_BwE) account
    * Make sure you add a payment method to your account. You are not allowed to host sites without having payment attached to your account
- Install [Heroku command line client](https://devcenter.heroku.com/articles/heroku-cli)
    * You may already have this installed, use the command ` $ heroku --version` to check
- Login to Heroku on the command line
    * Enter `$ heroku login` to the command line and follow the prompts to sync your command line with your Heroku account.
4. __Create new app inside Heroku__
- Enter `$ heroku create __app-name__` to the command line
    * This prompt will create a new application inside your Heroku account. Replace __app-name__ with whatever you want the app to be called. This name will also be used as the default domain for the hosted website.
5. __Sync Git with Heroku__
- By connecting our cloned repository with our Heroku application we can easily push new changes to the application. In step 4, when we created the Heroku app, you should've received output similar to this: <br>
    ````
    Creating __app-name__ ... done
    https://__app-name__.herokuapp.com || https://git.heroku.com/__app-name__.git
    ````
- Enter `$ git add remote heroku https://git.heroku.com/__app-name__.git` to the command line
    * This command will allow you to make remote pushes to our Heroku application using git
6. __Deploy to Heroku__
- Set Python Build Pack
    * `$ heroku buildpacks:set heroku/python`
        * This command makes sure Heroku knows we are deploying a python application during build.
- Stage files
    * `$ git add .`
- Commit changes
    * `$ git commit -m "V1"`
- Push changes to Heroku
    * `$ git push heroku main`
- If everything is proceed correctly, your output should contain the URL of the site you just hosted!
    ````
    remote:        Released v1
    remote:        https://__app-name__.herokuapp.com/ deployed to Heroku
    ````

### Important Things to Note
The above instructions allow you to clone this repository as it is, and get it hosted. There are two files in the repository that are pivotal to hosting that I have already provided for you. I wanted to give a quick overview of them for increased clarity.
#### requirements.txt
This file lists all the installed packages this application uses. In other words, anything you had to `pip install ___` is included in this file. This ensures that Heroku will make all the required installs to ensure the program run the same as it does on your localhost. The file in the repository is currently up-to-date with the application as it is. <br><br>
Should you change the application by adding or removing any packages you will have to generate a new file. Entering the following to the command line will generate a new requirements file: <br>
`$ pip freeze > requirements.txt` <br><br>
_notes:_ 
<br>(1) Make sure you install all packages using a virtual environment [[venv for python](https://docs.python.org/3/library/venv.html)]. This will ensure your requirements file contains only the packages required for this application. If you do not use a virtual environment, the file will include every python application you've ever installed on your machine. While this inherently is not an issue, it is messy and poor practice. 
<br>(2) Make sure you include an 's' at the end of requirements. Heroku will not know how to identify the file if it is not named properly. 

#### Procfile
The Procfile informs Heroku how the application should be built. Our Procfile is set so that Heroku knows we are deploying a Django application. This file should never need to be changed.

## Updating the Hosted Site
Once you have the site hosted, making changes is very easy since we connected our project to git. 
1. Make changes on your local machine. Run the project on localhost to ensure they are functioning how you intended.
    * `$ python manage.py runserver`
2. Stage the changes
    * `$ git add .`
3. Commit the changes
    * `$ git commit -m "_message about the changes_"`
4. Push changes to Heroku
    * `$ git push heroku main` 

You should now see an updated version of the site at the URl provided in the last commands output. 

_notes:_ 
<br>(1) Only the owner of the application is allowed to push changes to the hosted site. If you created the Heroku application, by default you are the owner. You can change ownership by going to https://dashboard.heroku.com/apps/app-name/settings, and scrolling until you see the subheader 'Transfer Ownership'. 



