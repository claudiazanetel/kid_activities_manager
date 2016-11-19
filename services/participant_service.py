
from datetime import datetime
from models.participant import Participant
import io
import csv

class ParticipantService:

    def __init__(self, participant_dao):
        self.participant_dao = participant_dao

    def get_weeks_list(self):
        return self.participant_dao.get_weeks_list()

    def get_participants_by_week(self, week):
        return self.participant_dao.get_participants_by_week(week)

    def store_participants_from_file(self, file, week):
        if not file:
            raise ValueError("No file provided")

        stream = io.StringIO(file.stream.read().decode("UTF8", errors='ignore'), newline=None)
        csv_content = csv.reader(stream)
        count = 0
        for row in csv_content:
            count +=self.store_participant(row, 1, 4, week)

        return count

    def store_participant(self, file_row, name_index, date_index, week):
        if file_row[0].isdigit():
            date = datetime.strptime(file_row[date_index], '%d/%M/%Y')
            participant = Participant(name=file_row[name_index], dob=date, week=week)
            self.participant_dao.store_participant(participant)
            return 1
        else:
            return 0