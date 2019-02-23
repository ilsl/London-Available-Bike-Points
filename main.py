from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests

# App config.
DEBUG = True
app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
bike_occupancy_url_template = 'https://api.tfl.gov.uk/Occupancy/BikePoints/{BikePoints_id}'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    print(form.errors)

    if request.method == 'POST':
        userinput = request.form['name']
        try:
            resp = requests.get('https://api.tfl.gov.uk/Occupancy/BikePoints/{}'.format(userinput))
            bikesPoints = resp.json()
        except Exception as inst:
            print(inst)
            print(resp.reason)
            return

        print(bikesPoints[0]['emptyDocks'])
        emptyDock = bikesPoints[0]['emptyDocks']
        location = bikesPoints[0]['name']

    if form.validate():
        # Save the comment here.
        flash('Currently theis is' + str(emptyDock) + " available bikes in " + location)
    else:
        flash('Error: no id entered. ')

    return render_template('bike_point_map.html', form=form)

if __name__ == "__main__":
    app.run()







