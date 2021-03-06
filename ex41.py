#!/usr/bin/python3

"""
class - tell Python to make a new type of thing
object - two meaning: the most basic type of thing, and any instance of thing
instance - what you get when you tell Python to create a class
def - how you define a function inside a class
self - inside the functions in class, self is a var for the instance/object
    being accessed
inheritance - concept that one class can inherit traits from another class
composition - concept that a class can be composed of other classes as parts
attribute - a property that classes have that are from composition and are
    usually variables
is-a - phrase to say that something inherits from another, as in:
    "salmon" is-a "fish"
has-a - phrase to say that something is composed of other things or has a trait
    "salmon" has-a "mouth"
"""

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** atribute and set it to '***'."
}

# do they want to drill phrases first?
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("***", word, 1)

        results.append(result)

    return results

# keep going until the hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer,  question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOError:
    print("\nBye!")
