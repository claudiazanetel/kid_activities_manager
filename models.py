from google.appengine.ext import ndb

class Participant(ndb.Model):
   name = ndb.StringProperty(indexed=False)
   dob = ndb.DateProperty(indexed=False)
   week = ndb.StringProperty(indexed=True)