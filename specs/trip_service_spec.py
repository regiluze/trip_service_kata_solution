# -*- coding: utf-8 -*-

from expects import *
from doublex import *
from trip_service_kata import tripservice

def _build_fake_user():
    user = tripservice.User()
    user.getFriends = lambda : ['Geoge', 'Patxi'] 
    return user

IRRELEVANT_USER= 'user'
IRRELEVANT_TRIPS = ['amazing trip', 'cultural trip']

with describe('trip service specs'):
    with context('trips by user'):
        with before.each:
            self.user = _build_fake_user()
        with context('when logger user is None'):
            with it('throws an error'):
               tripservice._getLoggedUser = lambda : None 

               expect(lambda: tripservice.getTripsByUser(self.user)).\
               to(raise_error(tripservice.UserNotLoggedInException))
        
        with context('when the user is logged'):
            with context('when the user is logged'):

                with context('logged user is not in the user friend list'):
                    with it('returns an empty trips list'):
                        tripservice._getLoggedUser = lambda : "Bob" 

                        expect(tripservice.getTripsByUser(self.user)).to(be_empty)
                
                with context('logged user is in the user friend list'):
                    with it('returns user trips list'):
                        tripservice._getLoggedUser = lambda : "Patxi" 
                        tripservice._findTripsByUser = lambda user: IRRELEVANT_TRIPS

                        expect(tripservice.getTripsByUser(self.user)).to(equal(IRRELEVANT_TRIPS))


