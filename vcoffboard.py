import sys
import requests
import argparse
import logging
import json
import datetime

from veracode_api_py import VeracodeAPI as vapi

def creds_expire_days_warning():
    creds = vapi().get_creds()
    exp = datetime.datetime.strptime(creds['expiration_ts'], "%Y-%m-%dT%H:%M:%S.%f%z")
    delta = exp - datetime.datetime.now().astimezone() #we get a datetime with timezone...
    if (delta.days < 7):
        print('These API credentials expire ', creds['expiration_ts'])

def get_user_list(usernames):
    #get list of guids
    user_list = []
    for name in usernames:
        userinfo = vapi().get_user_by_name(name) # note that this call always returns a list of 1, or 0
        if len(userinfo) == 0:
            errorstring = "No user found with name {}".format(name)
            print(errorstring)
            logging.info(errorstring)
            #log
            continue
        userguid = userinfo[0]["user_id"]
        user_list.append(userguid)
    return user_list

def deactivate_user(userguid):
    vapi().disable_user(userguid)
    notification = "Deactivated user {}".format(userguid)
    logging.info(notification)

    return 1

def main():
    parser = argparse.ArgumentParser(
        description='This script deactivates a list of users in Veracode.')
    parser.add_argument('-u', '--usernames',nargs="+", required=False, help='List of usernames to deactivate.')
    args = parser.parse_args()

    usernames = args.usernames

    logging.basicConfig(filename='vcoffboard.log',
                        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S%p',
                        level=logging.INFO)

    # CHECK FOR CREDENTIALS EXPIRATION
    creds_expire_days_warning()

    count=0

    userguids = get_user_list(usernames)

    for guid in userguids:
        count += deactivate_user(guid)

    print("Deactivated",count,"users")

if __name__ == '__main__':
    main()