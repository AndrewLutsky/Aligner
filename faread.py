import numpy as np
class sequence:
    #constructor method
    def __init__(self, seq):
        self.seq = seq
    def reverse(self):
        return self.seq[::-1]
    def getSequence(self):
        return self.seq

#class alignment:
#    def __init__(self, seq1, seq2):
#        self.alignment = align(method, seq1, seq2)
#    def getAlignment(self):
#        return self.alignment

    
def readsequences(data) -> list:
    #error handling
    if data == None:
        raise AttributeError("None data type passed in as data")


    data = data.splitlines()
    lisSequence = [""]
    
    
    #Enumerate out to check if not on line 0, and adds to string until encounters next '>'
    ####WIP######
    i = 0
    for count, line in enumerate(data):
        line = str(line.strip())
        if line[0] != '>': 
            lisSequence[i] += line
        elif (line[0] == '>'):
            if count > 0:
                i += 1
                lisSequence.insert(i, "")
            else:
                continue
        else:
            raise TypeError("Can't read sequence file")
    

    #creates list of sequence objects

    lisSequenceObjects = []

    for seq in lisSequence:
        sequen = sequence(seq)
        lisSequenceObjects.append(sequen)
    
    #length checker
    if len(lisSequenceObjects) <= 1:
        raise ValueError("Number of sequences is less than two")
    return lisSequenceObjects
        
def align(method, seq1, seq2):
    dictMethods = {"SW":0, "NW":1}
    methodNumber = dictMethods[method]
    arr = np.zeros(len(seq1), len(seq2))
    return arr




