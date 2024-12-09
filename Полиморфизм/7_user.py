from fake_subscription import FakeSubscription


class User():
    def __init__(self, email, current_subscription=None):
        self.email = email
        # BEGIN
        self.current_subscription = current_subscription or FakeSubscription(self)  # noqa: E501
        # END

    def get_current_subscription(self):
        return self.current_subscription

    def is_admin(self):
        return self.email == 'rakhim@hexlet.io'
