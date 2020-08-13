# import string

# def buildShiftDict(shift):
#     shiftedDict = {}
#     ALPHABET_LENGTH = 26
#     for c in string.ascii_uppercase:
#         if ord(c) + shift > ord('Z'):
#             shiftedDict[c] = chr(ord(c) + shift -ALPHABET_LENGTH)
#         else:
#             shiftedDict[c] = chr(ord(c) + shift)
#     for c in string.ascii_lowercase:
#         if ord(c) + shift > ord('z'):
#             shiftedDict[c] = chr(ord(c) + shift -ALPHABET_LENGTH)
#         else:
#             shiftedDict[c] = chr(ord(c) + shift)
#     return shiftedDict

# def applyShift(text: str, shiftedDict: dict) -> str:
#     encryptedChars = []
#     for c in text:
#         if c in shiftedDict:
#             encryptedChars.append(shiftedDict[c])
#         else:
#             encryptedChars.append(c)
    
#     return ('').join(encryptedChars)

# d = buildShiftDict(2)
# a = applyShift('hi hi', d)
# print(a)
import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("ProblemSet5/story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'ProblemSet5/words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = None

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        self.shift = shift
        self.originalDict = {}
        ALPHABET_LENGTH = 26
        # make original dictionary {'a': 'c'} if shift 2
        for c in string.ascii_uppercase:
            if ord(c) + self.shift > ord('Z'):
                self.originalDict[c] = chr(ord(c) + self.shift - ALPHABET_LENGTH)
            else:
                self.originalDict[c] = chr(ord(c) + self.shift)

        for c in string.ascii_lowercase:
            if ord(c) + self.shift > ord('z'):
                self.originalDict[c] = chr(ord(c) + self.shift - ALPHABET_LENGTH)
            else:
                self.originalDict[c] = chr(ord(c) + self.shift)
        return self.originalDict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        self.shift = shift
        self.encryptedChars = []
        self.get_message_text()
        for c in self.get_message_text():
            if c in self.build_shift_dict(self.shift):
                newChar = self.build_shift_dict(self.shift)[c]
                self.encryptedChars.append(newChar)
            else:
                self.encryptedChars.append(c)
                
        return ('').join(self.encryptedChars)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift

    def get_shift(self):
        return self.shift

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        return Message.apply_shift(self, self.shift)

a = {'a': 1, 'b': 2}
b = a.copy()
a['c'] = 3
print(b)