from datetime import datetime


class Throttler:

    def __init__(self, limit, interval):
        self.token_limit = limit
        self.interval = interval
        self.tokens = limit
        self.last_refill = datetime.now()

    def allowed(self):

        self.check_refill()

        if self.tokens == 0:
            return False
        return True

    def action_done(self):

        if not self.check_refill():
            # the bucket was not refilled, check if empty
            if self.tokens == 0:
                raise ActionNotAllowed

        self.tokens -= 1

    def check_refill(self):
        if (datetime.now() - self.last_refill).seconds > self.interval:
            self.last_refill = datetime.now()
            self.tokens = self.token_limit
            return True
        return False


class ActionNotAllowed(Exception):
    pass