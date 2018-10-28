import datetime


class MessageUser:
    user_details = []
    messages = []
    base_message = """Hi {name}!
    Thank you for your purchase on {date}
    We Hope you are excited about using it.
    Just as a reminder the purchase total was ${total}
    Thank you,
    Team CFE!"""

    def add_user(self, user_name, user_amount, user_email=None):
        user_name = user_name[0].upper() + user_name[1:].lower()
        user_amount = "%.2f" % user_amount
        # detail is a dictionary that handles name, amount, date & email
        # you necessarily don;t need to pass date as a parameter to the method. Because it is -
        # - self generated. Email, name and amount needs to be passed.
        detail = {
            "name": user_name,
            "amount": user_amount
        }

        today = datetime.date.today()
        date_text = "{today.month}/{today.day}/{today.year}".format(today=today)
        detail["date"] = date_text
        if user_email is not None:
                detail["email"] = user_email

        # user_details is the empty list variable that we created when we defined class
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.messages.append(new_msg)
            return self.messages
        return[]


obj = MessageUser()
obj.add_user("Justin", 123.32, user_email="hello@teamcfe.com")
# obj.add_user("Pranav", 458.235)
# obj.add_user("User3", 7894.258)
print(obj.get_details())
print(obj.make_messages())


def some_random_func():
    return print("\n Testing 123")


