from models.datastore.participant import Participant

class ModelMapper:


    @staticmethod
    def participantToDatastore(source):
        return Participant(name=source.name, dob=source.dob, week=source.week)
