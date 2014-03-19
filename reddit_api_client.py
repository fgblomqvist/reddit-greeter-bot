import requests


class RedditAPIClient:
    def __init__(self, throttler, user_agent):
        self.throttler = throttler
        self.reddit_url = 'http://www.reddit.com'
        self.reddit_ssl_url = 'https://ssl.reddit.com'

        # initialize the request client
        client = requests.session()
        client.headers.update({'User-agent': user_agent})

        self.client = client

    def login(self, username, password):
        """Logs in the user to the Reddit API"""

        # this will set the correct cookie and get the required modhash
        parameters = {'api_type': 'json', 'user': username, 'passwd': password}
        result = self.client.post(self.reddit_ssl_url + '/api/login', params=parameters)

        # set the custom header
        self.client.headers['X-Modhash'] = result.json()['json']['data']['modhash']

    def get_posts(self, subreddit=None):
        """Returns the latest posts in the specified subreddit"""

        if not self.throttler.allowed():
            raise RequestLimitReached

        self.throttler.action_done()

        api_url = self.reddit_url

        # specifying a subreddit is optional
        if subreddit is not None:
            api_url += '/r/' + subreddit

        api_url += '/search.json?'

        # call the api
        parameters = {'sort': 'new', 'restrict_sr': 0}
        result = self.client.get(api_url, params=parameters)

        return [p['data'] for p in result.json()['data']['children']]

    def post_comment(self, thing_id, text):
        """Posts a comment as the currently logged in user to the specified thing"""

        if not self.throttler.allowed():
            raise RequestLimitReached

        self.throttler.action_done()

        # the user must be logged in to perform this action
        if not 'X-Modhash' in self.client.headers and 'reddit_session' in self.client.cookies:
            raise UserNotLoggedIn

        # post the comment
        parameters = {'api_type': 'json', 'thing_id': thing_id, 'text': text}
        result = self.client.post('http://www.reddit.com/api/comment', params=parameters)

        return True


class RequestLimitReached(Exception):
    pass


class UserNotLoggedIn(Exception):
    pass