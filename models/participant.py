
class Participant(object):
    
    def __init__(self, name, dob, week):
        self.name = name
        self.dob = dob
        self.week = week

    def __str__(self):
        return "[{} - {} - {}]".format(self.dob.strftime("%Y-%m-%d"), self.name, self.week)