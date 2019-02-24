from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import requests
import get_credentials
import json
from ast import literal_eval


# App config.
DEBUG = True
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# Entry point for TFL API
bike_occupancy_url_template = 'https://api.tfl.gov.uk/Occupancy/BikePoints/{BikePoints_id}'


# Using Flask WTF forms to provide functionality between client end code and server send code
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


# This is the logging in page
@app.route('/login', methods=['POST'])
def do_admin_login():
    # Get credentials from GCP bucket
    # credentials.get()
    cred = get_credentials.read_file('credentials.py')
    cred = literal_eval(cred.decode())
    print(type(cred))
    print(cred)
    #Check whether username and password is valid
    if request.form['password'] == cred['password'] and request.form['username'] == cred['username']:

        session['logged_in'] = True

    else:
        flash('wrong password!')

    return redirect(url_for('bike'))

# This is the page which returns the Bike Point information
@app.route("/", methods=['GET', 'POST'])
def bike():
    # Redirect to the login page when first loading the app
    if not session.get('logged_in'):
        return render_template('login.html')

    else:
        # Once succeded in loggin in to the app then the bike_point_map.html can be rendered
        form = ReusableForm(request.form)
        print(form.errors)
        # When the button is clicked perform the following
        if request.method == 'POST':
            #Get Bike Point id from user
            userinput = request.form['name']
            try:
                # Make a request to the TFL API
                resp = requests.get('https://api.tfl.gov.uk/Occupancy/BikePoints/{}'.format(userinput))
                bikesPoints = resp.json()
            except Exception as inst:
                print(inst)
                print(resp.reason)
                return

            # Get the number of abailable bikes
            emptyDock = bikesPoints[0]['emptyDocks']
            location = bikesPoints[0]['name']

        if form.validate():
            # Save the comment here.
            flash('Currently there are' + str(emptyDock) + " available bikes in " + location)
        else:
            flash('Error: no id entered. ')

        return render_template('bike_point_map.html', form=form)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True, host='0.0.0.0', port=5005)