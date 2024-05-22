# Metacognition Selection Web App

**Feature(s):**
Django based web application which allows experts to examine student responses and provide annotations on metacognition

**Notes for Me** <br>
*Work Flow*
* Opens web-app to login page
* User logs in
* User is brought to instruction page 
* User is brought to most current student response (save progress somewhere)
* User completes form 
* User logs out and progress is updated 

*Features*
* Login page
* Instruction Page
* Tagging page
    * Retrieve student response from database
        * Parse by sentence and make each sentence selectable 
            * Upon selection open up new form 
    * Return to instruction button : href
    * Submit button 
        * Saves report to database 
        * Updates progress 
        * Retrieves next student response 
    * Logout button
        * Posts progress to profile 