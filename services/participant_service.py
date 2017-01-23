from datetime import datetime
import io
import csv
import logging
from models.participant import Participant

class ParticipantService(object):
    '''
    Service class to manage participants
    '''

    def __init__(self, participant_dao):
        self.participant_dao = participant_dao

    def get_weeks_list(self):
        '''
        Retrieves the list of weeks the participants are registered to
        '''
        return self.participant_dao.get_weeks_list()

    def get_participants_by_week(self, week):
        '''
        Retrieves the list of participants registeres to the given week
        '''
        return self.participant_dao.get_participants_by_week(week)

    def store_participants_from_file(self, participants_file, week):
        '''
        Stores the participants on the given file into the database
        '''
        if not participants_file:
            raise ValueError("No file provided")
        stream = io.StringIO(participants_file.stream.read().decode("UTF8", errors='ignore'), newline=None)
        csv_content = csv.reader(stream)
        count = 0
        for row in csv_content:
            count += self.store_participant(row, 1, 4, week)

        return count

    def store_participant(self, file_row, name_index, date_index, week):
        '''
        Stores a signle participant's registration for week into the database
        '''
        if file_row[0].isdigit():
            try:
                date = datetime.strptime(file_row[date_index], '%d/%M/%Y')
                participant = Participant(name=file_row[name_index], dob=date, week=week)
                self.participant_dao.store_participant(participant)
                return 1
            except ValueError as exception:
                logging.warning(exception)
                return 0
        else:
            return 0
