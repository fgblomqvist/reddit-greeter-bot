import json
import os
from time import sleep


class GreeterBot:
    def __init__(self, reddit_api_client, greeted_authors_backup, greeting):
        self.rclient = reddit_api_client
        self.greeting = greeting
        self.greeted_authors_backup = greeted_authors_backup
        self.greeted_authors = []

        self.load_greeted_authors()

    def load_greeted_authors(self):
        if os.path.isfile(self.greeted_authors_backup):
            self.greeted_authors = json.load(open(self.greeted_authors_backup))

    def save_greeted_authors(self):
        json.dump(self.greeted_authors, open(self.greeted_authors_backup, 'w'))

    def watch(self, subreddit):
        """Watches the specified subreddit for posts by people that haven't been greeted yet"""

        while True:
            posts = self.rclient.get_posts(subreddit)

            for post in posts:
                if post['author'] not in self.greeted_authors:
                    if self.rclient.post_comment(post['name'], self.greeting.replace('{name}', post['author'])):
                        # the author has now been greeted
                        self.greeted_authors.append(post['author'])
                        self.save_greeted_authors()

            sleep(2)