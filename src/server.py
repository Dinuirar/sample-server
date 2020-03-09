from flask import render_template, flash, redirect
from src import app
from src.forms import TelecommandForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main')


@app.route('/telecommands', methods=['GET', 'POST'])
def telecommands():
    form = TelecommandForm()
    if form.validate_on_submit():
        flash('telecommand: {}'.format(form.telecommand.data))
        return redirect('/telecommands')
    return render_template('telecommands.html', title='telecommands', form=form)


@app.route('/telemetry')
def readings():
    return render_template('telemetry.html', title='telemetry')
