# Emoji_Converter.py and Functions.py

def emoji_converter(anything):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "☹",
        ":'(": "😥"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input('>>> ')
print(emoji_converter(message))


def greet_user(firstname, lastname):  # The (name) holder is a parameter
    print(f'Hi {firstname} {lastname}!')
    print('Welcome aboard!')


print("Start")
greet_user('Shaikh Ayman', lastname="Abdul-Majid")  # The name 'Ayman' in (name) is an argument.
print("Finish")


def square(number):
    return number * number


number_choice = int(input('Please enter a number to square: '))
print('This is your number squared: ', square(number_choice))


try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero!')
except ValueError:
    print('Invalid Value!!')
