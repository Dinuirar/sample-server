from flask import render_template, send_file, request
from flask_restplus import Resource
from src import app, api
from src.database import Database
from time import sleep


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main')


@app.route('/error_log')
def error_log():
    return render_template('error_log.html', title='error log')


@app.route('/photo')
def photo():
    print("photo requested")
    db = Database()
    db.add_telecommand("TAKE PHOTO")
    sleep(3)
    img_path = f"static/{db.get_last_photo_name()}"

    return send_file(img_path, mimetype='image/gif')


@api.route('/get_telemetry')
class GetTelemetry(Resource):
    def get(self):
        db = Database()
        tm = db.get_telemetry()
        return tm.serialize()


@api.route('/post_telecommand')
class PostTelecommand(Resource):
    def post(self):
        received = request.get_json()
        if received is None:
            return {'status': 'JSON payload is empty!'}
        else:
            tc = received['telecommand']
            if tc is None:
                return {'status': 'telecommand field empty!'}
            print(tc)
            db = Database()
            db.add_telecommand(tc)
            return {'status': f'telecommand ({tc}) added'}
