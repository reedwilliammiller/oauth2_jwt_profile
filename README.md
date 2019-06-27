# oauth2_jwt_profile
Uses OAuth2 to sign in user via Google, then calls the Google People API to display the user's first and last name using a JWT for authentication.
Deploys via Google Cloud App Engine

In order to test this out yourself, use the following instructions.

1. Set up a Google Cloud Project following the instructions here: https://cloud.google.com/appengine/docs/standard/python3/quickstart

Except instead of cloning the repository listed, clone this repository

2. Login to your Google Cloud Platform console and choose the project you created from the dropdown at the top. 

3. Click on the menu in the upper left and scroll down to choose APIs & Services

4. Click on Credentials in the left-hand menu and then click the Create credentials button and click OAuth client ID

5. Choose web application and type in a name for it.  In the Authorized JavaScript origins field, add the base url for the app (it will be something like https://yourprojecturl.appspot.com).  Add your base url with /oauth to the Authorized redirect URIs field.  (also add http://localhost:8080/oauth if you want to test locally).  Click Create

6. Copy your client ID and secret.  Open up the main.py file and add in the client ID and secret to the appropriate variables in the / and /oauth routes.

7. If you are deploying the app to App Engine, add your appspot.com redirect URI to the variables in the / and /oauth routes.  If you are testing locally, use the localhost/8080 url.  Or you can create a url variable that you update accordingly.

8. To test locally, follow the 'Run Hello World on your local machine' section of the quickstart guide referenced above. Remember to update your redirect uri!

9. To deploy to Google App Engine, follow the 'Deploy and run Hello World on App Engine' section of the quickstart guide referenced above.  Remember to update your redirect uri!
 
