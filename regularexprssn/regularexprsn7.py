# replace a string
import re
string ='''Computer science is
the study of  the theory,
experimentation and engineering
that form the basis for the design
and use of computers.'''
regex = re.compile('\n') # newline replaced by space printing on a single line
substring = regex.sub(" ", string)
print(substring)