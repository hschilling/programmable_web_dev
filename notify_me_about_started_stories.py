'''
Let me know if there are any of my Pivotal OpenMDAO stories at are
in the unfinished state
'''
import requests

import api_keys

pivotal_project_id = 1885757
pivotal_my_id = 575787

slack_my_im_channel_id = 'D1A386U0H'


# get a list of my stories that are in the started state
url = 'https://www.pivotaltracker.com/services/v5/projects/{}/stories'.format(pivotal_project_id)
pivotal_payload = {'with_state': 'started'}
r = requests.get(url,
                 headers={'X-TrackerToken':api_keys.pivotal_token},
                 params=pivotal_payload
                 )
my_unfinished_stories = [story['url'] for story in r.json() if story['owned_by_id'] == pivotal_my_id]
# If there are any, post that to my Slack channel
if my_unfinished_stories:
    msg = 'My stories in started state are:\n'
    for mus in my_unfinished_stories:
        msg += '  {}\n'.format(mus)

    url = 'https://slack.com/api/reminders.add'
    headers = {'content-type': 'x-www-form-urlencoded'}
    data = [
     ('token', api_keys.slack_token),
     ('user', 'U02BR50EE'),
     ('time', 'in 1 minutes'),
     ('text', msg),
    ]
    r = requests.post(url, data, headers)

    #
    # url = 'https://slack.com/api/chat.meMessage'
    # headers = {'content-type': 'x-www-form-urlencoded'}
    # data = [
    #  ('token', slack_token),
    #  ('channel', slack_my_im_channel_id),
    #  ('text', msg),
    # ]
    # r = requests.post(url, data, headers)



    # https: // slack.com / api / reminders.add?token = xoxp - 2395158932 - 2399170490 - 281861541063 - 539
    # fa99afdfeff436887da86d9d62142 & text = my % 20
    # reminder & time = 10 % 3
    # A55AM & user = U02BR50EE & pretty = 1(open
    # ra

# Maybe set reminder ? https://api.slack.com/methods/reminders.add
# Try here https://api.slack.com/methods/reminders.add/test