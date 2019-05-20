lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    # Implement your generator function here
    count = start
    for el in iterable:
        yield count, el
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

"""
If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large files), 
being able to take and use chunks of it at a time can be very valuable.
Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.
"""


def chunker(iterable, size):
    # Implement function here
    for el in range(0, len(iterable), size):
        yield iterable[el:el + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))


"""
Generator Expressions
Here's a cool concept that combines generators and list comprehensions! 
You can actually create a generator in the same way you'd normally write a list comprehension, 
except with parentheses instead of square brackets.
"""

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
