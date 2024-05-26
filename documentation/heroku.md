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
    * `Creating __app-name__ ... done` <br>
    `https://__app-name__.herokuapp.com || https://git.heroku.com/__app-name__.git`
- Enter `$ git add remote heroku https://git.heroku.com/__app-name__.git` to the command line
    * This command will allow you to make remote pushes to our Heroku application using git
6. __Deploy to Heroku__
- Stage files
    * `$ git add .`
- Commit changes
    * `$ git commit -m "V1"`
- Push changes to Heroku
    * `git push heroku main`
- If everything is proceed correctly, 

