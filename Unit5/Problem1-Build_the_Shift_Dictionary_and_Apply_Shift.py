import string
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
        dic = {}
        c = string.ascii_lowercase
        d = string.ascii_uppercase
        low = {}
        up = {}
        low_reverse = {}
        up_reverse = {}
        aa = [] # store low letter
        bb = [] # store up letter
        cd = c + d
        for i, j in enumerate(c):
            low[j] = i
            low_reverse[i] = j
        for i, j in enumerate(d):
            up[j] = i
            up_reverse[i] = j
        for z in cd:
                    if z in c:
                        if low[z]+shift > 25:
        #                    print(low_reverse[low[z]+shift-26])
                            aa.append(low_reverse[low[z]+shift-26])
                        else:
        #                    print(low_reverse[low[z]+shift])
                            aa.append(low_reverse[low[z]+shift])
                    else:
                        if up[z]+shift > 25:
         #                   print(up_reverse[up[z]+shift-26])
                            aa.append(up_reverse[up[z]+shift-26])
                        else:
        #                    print(up_reverse[up[z]+shift])
                            aa.append(up_reverse[up[z]+shift])
        return dict(zip(list(cd),aa))

        
        

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
        c = string.ascii_lowercase
        d = string.ascii_uppercase
        low = {}
        up = {}
        low_reverse = {}
        up_reverse = {}
        aa = [] # store low letter
        bb = [] # store up letter
        for i, j in enumerate(c):
            low[j] = i
            low_reverse[i] = j
        for i, j in enumerate(d):
            up[j] = i
            up_reverse[i] = j
        num = {n:n for n in range(26)}
        for z in self.message_text:
            if z in c:
                if low[z]+shift > 25:
#                    print(low_reverse[low[z]+shift-26])
                    aa.append(low_reverse[low[z]+shift-26])
                else:
#                    print(low_reverse[low[z]+shift])
                    aa.append(low_reverse[low[z]+shift])
            elif z in d:
                if up[z]+shift > 25:
 #                   print(up_reverse[up[z]+shift-26])
                    aa.append(up_reverse[up[z]+shift-26])
                else:
#                    print(up_reverse[up[z]+shift])
                    aa.append(up_reverse[up[z]+shift])
            else:
                aa += z
        return ''.join(aa)