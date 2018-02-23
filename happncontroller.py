#!/usr/bin/env python
# -*- coding: utf-8 -*-
import happn
import pprint #For dictionary printing

# acessar https://www.facebook.com/dialog/oauth?client_id=247294518656661&redirect_uri=https://www.happn.fr&scope=basic_info&response_type=token
# para obter token
token = ""



# Generate the Happn User object
myUser = happn.User(token)

def getRecommendations():
    myUser = happn.User(token)
    myUser.set_position(-19.937707, -43.935240)
    # Get recommendations
    recs = []
    for i in range(1):
        recs += myUser.get_recommendations(100, i * 100)
    recs = list(reversed(recs))

    crushes = []

    for rec in recs:
        happn_user_profile = rec['notifier']
        if happn_user_profile[u'is_accepted']:
            crushes.append(rec)

    for crushe in crushes:
        happn_user_profile = crushe['notifier']
        target_info = getTargetinfo(happn_user_profile['id'])
        social_sync = target_info['social_synchronization']
        instagram = social_sync['instagram']
        if instagram is not None:
            instagram_pictures = instagram['pictures']
            crushe.update({'instagram_pictures':instagram_pictures})
            crushe.update({'instagram_number_of_pictures': len(instagram_pictures)})

    return crushes

def declineUser(id):
    myUser = happn.User(token)
    # Decline User
    myUser.decline_user(id)

def likeUser(id):
    myUser = happn.User(token)
    # Like User
    myUser.like_user(id)

def getTargetinfo(id):
    myUser = happn.User(token)
    # Target User Info
    return myUser.get_targetinfo(id)
