import random


UpperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
LowerCaseLetters = UpperCaseLetters.lower()
digits ="0123456789"
symbols = "()[]{}!#¤%&/?-.,:;_*+"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += UpperCaseLetters
if lower:
    all += LowerCaseLetters
if nums:
    all += digits
if syms:
    all += symbols

length = 32
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))

    print(password)