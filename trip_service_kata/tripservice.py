#!/usr/bin/env python


#
# Exceptions
#
class DependendClassCallDuringUnitTestException(Exception):
  pass

class UserNotLoggedInException(Exception):
  pass

#
# Classes
#
class Trip:
  pass

class User:
  def __init__(self):
    self.trips = []
    self.friend = []
  
  def addFriend(self, user):
    self.friends.add(user)
  
  def addTrip(self, trip):
    self.trips.add(trip)

  def isMyFriend(self, loggedUser):
      if loggedUser in self.getFriends():
          return True
      return False

  
#
# Functions
#
def _isUserLoggedIn(user):
  raise DependendClassCallDuringUnitTestException(
    "UserSession.isUserLoggedIn() should not be called in an unit test"
  )

def _getLoggedUser():
  raise DependendClassCallDuringUnitTestException(
    "UserSession.getLoggedUser() should not be called in an unit test"
  )

def _findTripsByUser(user):
  raise DependendClassCallDuringUnitTestException(
    "TripDAO should not be invoked on an unit test."
  )

def retrieveLoggedUser():
    loggedUser = _getLoggedUser()
    if loggedUser is None:
        raise UserNotLoggedInException()
    return loggedUser

def getTripsByUser(user):
  if user.isMyFriend(retrieveLoggedUser()):
    return _findTripsByUser(user)
  return []

if __name__ == "__main__":
  pass
