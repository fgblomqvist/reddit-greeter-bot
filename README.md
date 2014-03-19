Reddit Greeter Bot
------------------
This is a simple example on how a "greeter bot" for Reddit could be coded. It was an assignment for my programming class.
Its task is to greet all of the post authors in a specified subreddit with a set greeting (by posting it as a comment on their latest post).

Core features:

* Only greets every author once
* Obeys the official [Reddit API rules](https://github.com/reddit/reddit/wiki/API)
* Stores the settings in a separate file

Usage
-----

1. Customize the settings in `settings.json`
2. Run `main.py`
3. The bot will now greet existing posts, as well as watch for new ones

### Greeting Formatting
The greeting is formatted in the same way as an [ordinary Reddit comment](http://www.reddit.com/wiki/commenting), which means it is formatted using [markdown](http://daringfireball.net/projects/markdown/syntax). Something worth noting is that Reddit requires __double__ newlines (\n\n) instead of just one.
To include the author's name in the greeting, use this: `{name}`