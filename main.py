import json
from greeter_bot import GreeterBot
from throttler import Throttler
from reddit_api_client import RedditAPIClient


# get the login details from settings.json
data = json.load(open('settings.json'))

throttler = Throttler(30, 60)
rclient = RedditAPIClient(throttler, data['user_agent'])
rclient.login(data['user']['name'], data['user']['password'])

greeter_bot = GreeterBot(rclient, data['greeted_authors_backup'], data['greeting'])

print('Watching for new authors to greet...')
greeter_bot.watch('itggreeter')