from TestClass_1 import MessageUser, some_random_func

obj = MessageUser()
obj.add_user("Justin", 123.32, user_email="hello@teamcfe.com")
# obj.add_user("Pranav", 458.235)
# obj.add_user("User3", 7894.258)
print(obj.get_details())
print(obj.make_messages())

# calling second function
some_random_func()


