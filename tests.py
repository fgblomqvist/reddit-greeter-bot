import unittest
from datetime import datetime, timedelta
from lib.throttler import Throttler, ActionNotAllowed


class ThrottlerTest(unittest.TestCase):
    def setUp(self):
        self.limit = 5
        self.interval = 60
        self.throttler = Throttler(self.limit, self.interval)


    def test_throttler_fail(self):

        for i in range(self.limit):
            self.throttler.action_done()

        self.assertRaises(ActionNotAllowed, self.throttler.action_done)


    def test_throttler_limit(self):

        for i in range(self.limit):
            self.throttler.action_done()

        self.assertEqual(False, self.throttler.allowed())


    def test_refill(self):

        self.throttler.last_refill = datetime.now() - timedelta(seconds=self.interval + 1)
        self.assertEqual(True, self.throttler.allowed())