# [START app]
import logging
import io
import csv

from flask import Flask, render_template, request, make_response
from models import Participant
from datetime import datetime
from google.appengine.ext import ndb

app = Flask(__name__)

AGED_TYPE = 1
MIXED_TYPE = 2


@app.route('/')
def hello():
    return 'Ciao Claudia!!! <3'

@app.route('/upload')
def upload_action():
   return render_template('upload.html')

@app.route('/weeks')
def list_weeks():
    query = Participant.query(projection=['week'], distinct=True)
    weeks = []
    for week in query.iter():
        weeks.append(week)

    return render_template('weeks.html', weeks=weeks)

@app.route('/transform', methods=["POST"])
def transform_action():
   f = request.files['csv_file']
   if not f:
      return "No file"
   week = request.form['week']
   stream = io.StringIO(f.stream.read().decode("UTF8", errors='ignore'), newline=None)
   csv_content = csv.reader(stream)
   result = transform(csv_content, 1, 4, week)
   response = make_response(str(result))
   return response

def transform(file_content, name_index, date_index, week):
   result = []
   for row in file_content:
      if row[0].isdigit():
         print(row[date_index])
         date = datetime.strptime(row[date_index], '%d/%M/%Y')
         participant = Participant(name=row[name_index], dob=date, week=week)
         participant.put()

   return result

@app.route('/groups/<week>/<type>/<n_groups>', methods=["GET"])
def create_groups(week, type, n_groups):
   query = Participant.query(Participant.week == week)

   participants = []

   for participant in query.iter():
      participants.append(participant)

   group_type = int(type)
   if group_type == AGED_TYPE:
      groups = aged_groups(participants, int(n_groups))
   elif group_type == MIXED_TYPE:
      groups = mixed_groups(participants, int(n_groups))
   else:
      logging.exception('The type '+ group_type +' is invalid')
      return 'The type is not valid', 400

   return render_template('groups.html', groups=groups)

def sort(participants):
   participants.sort(key=lambda participant: participant.dob, reverse = True)
    
def aged_groups(rows, n_groups):
    sort(rows)

    n_children = len(rows)/n_groups
    children_out = len(rows)%n_groups

    groups = []
 
    for index in range(n_groups):
        groups.append(rows[index*n_children:(index+1)*n_children])   
    for j in range(children_out):
        groups[-1-j].append(rows[-1-j])
    return groups
  
def mixed_groups(rows, n_groups):
    sort(rows)
    n_children = len(rows)/n_groups
    children_out = len(rows)%n_groups    
    groups = []
    for index in range(n_groups):
        groups.append([])
        for i in range(n_children):
            groups[index].append(rows[(i*n_groups)+ index])
    for j in range(children_out):
        groups[-1-j].append(rows[-1-j])
    return groups

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]