
from models.datastore.participant import Participant as DataStoreParticipant
from models.participant import Participant
from models.model_mapper import ModelMapper

class ParticipantDAO:


    def get_weeks_list(self):
        '''
        Retrieves all the distinct weeks from the database
        '''
        query = DataStoreParticipant.query(projection=['week'], distinct=True)
        result = []
        for week in query.iter():
            result.append(week)
        return result

    def get_participants_by_week(self, week):
        '''
        Retrieves all the participants for the given week
        '''
        query = DataStoreParticipant.query(DataStoreParticipant.week == week)
        result = []
        for participant in query.iter():
            result.append(participant)
        return result

    def store_participant(self, participant):
        if type(participant) == Participant:
            to_store = ModelMapper.participantToDatastore(participant)
            to_store.put()
            return to_store
        if type(participant) == DataStoreParticipant:
            participant.put()
            return participant

        raise ValueError("The given participant is not of a valid type: " + 
            str(type(participant)) + 
            "\n allowed: " + 
            str(type(Participant("a", "a", "a"))))
