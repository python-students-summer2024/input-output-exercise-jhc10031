"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    fav_veggie = input("What is your favourite vegetable?")
    print(f'Interesting! I also love {fav_veggie}!')


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    fav_num = input("What is your favourite number?")
    print(f'Interesting! I also love {fav_num}!')


def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    name = input('What is your name?')
    zodiac = input('What is your zodiac sign?')
    print(f"Interesting! My name is also {name}, and I'm also a {zodiac}!")


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    name = input('What is your name?')
    age = input('How old are you?')
    print(f"Interesting! My name is also {name}, and I'm also {age} years old")
    
