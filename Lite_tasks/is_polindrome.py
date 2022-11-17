# TODO А роза упала на лапу Азора
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


def format_text(text):
    new_text = ""
    for i in text:
        if i.isalpha():
            new_text += i
    return new_text.lower()


some_text = input("Введите текст:")

if is_palindrome(format_text(some_text)):
    print("Да это палиндром")
else:
    print("Нет, не палиндром")

