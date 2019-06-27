from builtins import range

from flask import Flask, render_template, request
import random
import string
import requests



app = Flask(__name__)

def randomString(stringLength):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(stringLength))

#set state as global string
state_constant = randomString(20)


@app.route('/')
def index():
    #Call URL to log user in via OAuth
    url = 'https://accounts.google.com/o/oauth2/v2/auth'
    response_type= 'code'
    client_id = 'client id goes here'
    redirect_uri = 'redirect uri goes here'
    scope = 'profile email'
    state = state_constant

    link = url + '?response_type=' + response_type +'&client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&scope=' + scope + '&state=' + state
    return render_template('index.html', link=link)

@app.route('/oauth')
def oauth_email():
    #check if the state matches the one given
    state_returned = request.args.get('state')
    code_returned = request.args.get('code')
    if state_returned == state_constant:
        #post request for token
        r = requests.post(
            'https://www.googleapis.com/oauth2/v4/token',
            data={'code': code_returned,
                  'client_id': 'client id goes here',
                  'client_secret': 'client secret goes here',
                  'redirect_uri': 'redirect uri goes here',
                  'grant_type': 'authorization_code',
                  'state': state_returned
                  })
        token = r.json()['access_token']

        #get request for person information
        headers = {'Authorization': 'Bearer '+token}
        r2 = requests.get('https://content-people.googleapis.com/v1/people/me?personFields=names', headers=headers)

        person = r2.json()

        #set variables for jinja template
        first = person['names'][0]['givenName']
        last = person['names'][0]['familyName']
        state = state_constant
    else:
        first = 'N/A'
        last = 'N/A'
        state = 'State does not match! go back to start page and refresh and try again'
    return render_template('oauth.html', first=first, last=last, state=state)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]