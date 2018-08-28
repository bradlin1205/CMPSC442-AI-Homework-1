############################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Bradley Andi Lin"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """
Python is strongly typed, meaning a variable's type will not
change unless explicity converted. For example, a string
'12345' will not be interpreted as an integer unless it is
type casted with int("12345").
However, at the same time, Python is dynamically typed, meaning
a variable's typing can change during run time. For example,
x = 5 sets x to an integer, but a following line x = 'Hello, World!'
will compile and run with no issues and x will now be typed as a string. 
"""

python_concepts_question_2 = """
The problem with this is that the 2-dimensional points are given as lists, which are mutable.
A dictionary's keys must be immutable types. To solve this, you could use tuples instead of lists
to act as keys in the dictionary.
"""

python_concepts_question_3 = """
The faster function is concatenate2. This is because of how the memory
allocation works for these functions. Concatenate1 creates a new string and
must allocate new memory for the result of the += operation in each for loop iteration. The
.join call on the other hand calculates the necessary memory needed to allocate for
the final string up front and copies the substrings into then memory cutting out all the time
needed to deal with memory on each iteration. 
"""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    return [y for x in seqs for y in x]

def transpose(matrix):
    return [[matrix[x][y] for x in range(len(matrix))] for y in range(len(matrix[0]))]

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[0:-1]

def every_other(seq):
    return seq[0: :2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for x in range(0,len(seq)+1):
        yield seq[0:x]

def suffixes(seq):
    for x in range(len(seq), -1, -1):
        yield seq[0:x]

def slices(seq):
    for x in range(0, len(seq)+1):
        for y in range(x+1, len(seq)+1):
            yield seq[x:y]

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    return " ".join(text.lower().split())

def no_vowels(text):
    return "".join(x for x in text if x.lower() not in ('a','e','i','o','u'))

def digits_to_words(text):
    bigDict = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four","5":"five", "6":"six","7":"seven","8":"eight","9":"nine",}
    return " ".join(bigDict[x] for x in text if x.isdigit())

def to_mixed_case(name):
    string = "".join(x.capitalize() for x in name.lower().split('_'))
    string = string[0:1].lower() + string[1:] if string else ''
    return string

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.polynomial = tuple(polynomial)

    def get_polynomial(self):
        return self.polynomial

    def __neg__(self):
        return Polynomial(tuple([(list(x)[0] * -1, x[1]) for x in self.polynomial]))       

    def __add__(self, other):
        return Polynomial([x for x in self.polynomial] + [x for x in other.get_polynomial()])

    def __sub__(self, other):
        return Polynomial([x for x in self.polynomial] + [x for x in (-other).get_polynomial()])

    def __mul__(self, other):
        return Polynomial([(x[0]*y[0], x[1]+y[1]) for x in self.polynomial for y in other.get_polynomial()])

    def __call__(self, x):
        return sum([(y[0]*(x**y[1])) for y in self.polynomial])

    def simplify(self):
        bigDict = {}
        finalList = []
        for x in self.polynomial:
            if x[1] in bigDict:
                bigDict[x[1]].append(x[0])
            else:
                bigDict[x[1]]=[x[0]]
        finalList = [(sum(bigDict[x]),x) for x in bigDict]
        self.polynomial = tuple([x for x in reversed(finalList) if x[0] is not 0])

    def __str__(self):
        string = ((((" ".join(('+ '+str(x[0])[-1]+'x^'+str(x[1])) if x[0] >= 0 else ('- '+str(x[0])[-1]+'x^'+str(x[1])) for x in self.polynomial)).replace('x^0', '')).replace('x^1', 'x')).replace('1x', 'x'))
        if string[0] == '-':
            return '-'+string[2:]
        else: return string[2:]

############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
I spent about 2 afternoons on this
"""

feedback_question_2 = """
I had never done anything like list comprehension before and having things appear on one line
was really weird for me.
"""

feedback_question_3 = """
I like how it touched on a lot of different topics. If I were to change it, I'd add a few more open
ended questions because it went more into how python actually works and gave a clearer picture into
how better to construct a program.
"""
