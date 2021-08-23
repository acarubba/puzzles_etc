import string

poem = '''a narrow fellow in the grass
occasionally rides;
you may have met him, did you not,
his notice sudden is.

the grass divides as with a comb,
a spotted shaft is seen;
and then it closes at your feet
and opens further on.

he likes a boggy acre,
a floor too cool for corn.
yet when a child, and barefoot,
i more than once, at morn,

have passed, i thought, a whip-lash
unbraiding in the sun,
when, stooping to secure it,
it wrinkled, and was gone.

several of nature's people
i know, and they know me;
i feel for them a transport
of cordiality;

but never met this fellow,
attended or alone,
without a tighter breathing,
and zero at the bone.'''


class Solver:
    '''this does NOT account for duplicate frequency counts'''

    def __init__(self, text):
        '''tallies each letter in given text and returns a dictionary of the count'''
        self.text = text
        self.histogram = {c: text.count(c) for c in string.ascii_lowercase}

    def say(self, nums):
        '''takes in a list of numbers and returns their key values from histogram'''
        letter_list = list(self.histogram.keys())
        count_list = list(self.histogram.values())
        return ''.join([letter_list[count_list.index(num)] for num in nums])


puzzle = Solver(poem)
print(puzzle.histogram)
print(puzzle.say([1, 56, 7, 29, 42]))
