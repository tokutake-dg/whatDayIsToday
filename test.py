from rocketchat.api import RocketChatAPI
from pprint import pprint

api = RocketChatAPI(settings={'username': 'test', 'password': 'tokutake',
                              'domain': 'http://localhost:3000'})

api.send_message('message', 'bot')
