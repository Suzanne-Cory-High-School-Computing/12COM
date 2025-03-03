# This is the code in Practice booklet 3 OOP in python
# The comments below explain how inheritance works (see comments on Parent class)

from string import punctuation # the method punctuation in module string just looks for the common punctuations in a string

class Analyser: # declaring a class called Analyser
    def __init__(self,s): # constructor is automatically called whenever an object of class Analyser is created
        for c in punctuation: # finds the punctuations in the string s passed as an argument when we create a new object
            s = s.replace(c,'') # just replace each punctuation with nothing
            s = s.lower() # change to all lower case
            self.words = s.split() # and then assign to words which is a list of all the words split up

    def number_of_words(self): # class Analyser has a method called number_of_words
        return len(self.words) # just find the length of the list words
    
    def starts_with(self,s): # class Analyser has a method called starts_with, we are passing an argument containing the letter s argument
        return len([w for w in self.words if w[:len(s)]==s]) # just return the length of w, where w contains all words beginning with the s argument
    
    def number_with_length(self,n): # class Analyser has a method called number_with_length
        return len([w for w in self.words if len(w)==n]) # just return the length of w, where w contains all words with a length equal to the n argument
    
s = 'This is a test of the class.' # we are declaring the contents of the string s
analyser = Analyser(s) # create an object belonging to class Analyser and pass on the string argument 'This is a test of the class.' Call the object analyser
print(analyser.words)
print('Number of words:',analyser.number_of_words()) # call the method number_of_words in the object analyser
print('Number of words starting with "t":',analyser.starts_with('t')) # call the method starts_with in the object analyser and pass on the argument 't'
print('Number of 2-letter words:',analyser.number_with_length(2)) # call the method number_with_length in the object analyser and pass on the argument 2