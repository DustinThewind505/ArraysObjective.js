# x = 321
# y = 154323

# if x == y:
#     print(f'{x} and {y} are equal')
# else:
#     if x < y:
#         print(f'{x} is less than {y}')
#     else:
#         print(f'{x} is greater than {y}')


def do_twice(function):
    function()
    function()


def spam():
    print("SPAM")

do_twice(spam)