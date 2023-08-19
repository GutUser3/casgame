# The first message to be displayed in repo

class Example:
    def __init__(self, message):
        self.my_message = message

    def __str__(self):
        return self.my_message

text1 = Example('Hello')
text2 = Example('this')
text3 = Example('is an example')

print(text1, text2, text3)