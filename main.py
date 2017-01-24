# [START app]
import logging

from flask import Flask, render_template, request, make_response
from datetime import datetime
from google.appengine.ext import ndb

from services.groups_creator import GroupsCreator
from services.participant_service import ParticipantService
from daos.participant_dao import ParticipantDAO

participantDao = ParticipantDAO()
participantService = ParticipantService(participantDao)

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/giochi/<type>/<game>')
def showGame(game, type):
    return render_template('games/'+type+'/'+game)

@app.route('/upload')
def upload_action():
    return render_template('upload.html')

@app.route('/weeks')
def list_weeks():
    return render_template('weeks.html', weeks=participantService.get_weeks_list())

@app.route('/weeks/list/<week>')
def single_week(week):
    return render_template(
        'week_list.html',
        participants=participantService.get_participants_by_week(week),
        week=week)
        
@app.route('/transform', methods=["POST"])
def transform_action():
    file = request.files['csv_file']
    week = request.form['week']
    participants_imported = participantService.store_participants_from_file(file, week)
    return render_template('transform.html', count=participants_imported)

@app.route('/groups/<week>/<type>/<n_groups>', methods=["GET"])
def create_groups(week, type, n_groups):
    participants = participantService.get_participants_by_week(week)

    group_type = int(type)
    if group_type == GroupsCreator.AGED_TYPE:
        groups = GroupsCreator.by_age(participants, int(n_groups))
    elif group_type == GroupsCreator.MIXED_TYPE:
        groups = GroupsCreator.mixed(participants, int(n_groups))
    else:
        logging.exception('The type ' + group_type + ' is invalid')
        return 'The type is not valid', 400

    return render_template('groups.html', groups=groups)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
