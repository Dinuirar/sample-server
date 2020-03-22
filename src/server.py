from flask import render_template, flash, redirect
from src import app
from src.forms import TelecommandForm
from src.db_connection import Database
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main')


@app.route('/telecommands', methods=['GET', 'POST'])
def telecommands():
    form = TelecommandForm()
    if form.validate_on_submit():
        db = Database()
        db.add_telecommand(form.telecommand.data)
        flash(f'telecommand: {form.telecommand.data}')
        return redirect('/telecommands')
    return render_template('telecommands.html', title='telecommands', form=form)


@app.route('/telemetry')
def telemetry():
    db = Database()
    (gathered_time, humidity, temperature, pressure, luminosity, lamps, airfan, heater) = db.get_telemetry()
    return render_template('telemetry.html', title='telemetry',
                           gathered_time=gathered_time, humidity=humidity, temperature=temperature, pressure=pressure,
                           luminosity=luminosity, lamps=lamps, airfan=airfan, heater=heater)


@app.route('/photo')
def photo():
    gathered_time = datetime.now()
    # TODO: take a photo
    # TODO: take a proper filename
    img_path = '/static/example.png'
    return render_template('photo.html',
                           title='photo',
                           gathered_time=gathered_time,
                           img_path=img_path)

