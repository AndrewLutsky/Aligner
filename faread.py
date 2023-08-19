import numpy as np
class sequence:
    #constructor method
    def __init__(self, seq):
        self.seq = seq
    def reverse(self):
        return self.seq[::-1]
    def getSequence(self):
        return self.seq

class alignment:
    def __init__(self, sequences, method):
        self.alignment = align(method, sequences)
    


###Predefined substitution Matrix
substitution = {("A","A") : 1, 
        ("A","C"):-1, 
        ("A","G"):-1, 
        ("A","T"):-1, 
        ("C","C"):1, 
        ("C","A"):-1, 
        ("C","T"):-1, 
        ("C","G"):-1, 
        ("T","T"):1, 
        ("T","A"):-1, 
        ("T","G"):-1, 
        ("T","C"):-1, 
        ("G","G"):1, 
        ("G","C"):-1, 
        ("G","A"):-1, 
        ("G","T"):-1 }
    
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
        
def align(method, sequences) -> list:
    if method == None  or sequences == None:
        raise AttributeError("None type passed into aligning function")
    dictMethods = {"SW":0, "NW":1}
    methodNumber = dictMethods[method]
    print(sequences)
    arr = nw(sequences)
    return arr

#Matrix is flipped over diagonal -> to fix
def nw(sequences) -> list: 
    arr = np.zeros((len(sequences[0])+1,len(sequences[1])+1), dtype = int)
    gap = 1
    #mapping the first column and row of array
    #need to do separately in case strings are of different sizes
    #can't assume gap penalty
    for i in range(0, len(arr[0])):
        arr[0][i] = -i * gap
    for i in range(0, len(arr)):
        arr[i][0] = -i * gap
    print(arr)

    print("length of sequence 0: ",len(sequences[0]))
    print("length of sequence 1: ",len(sequences[1]))
    #matrix filling
    #i is width of array
    for i in range(1, len(arr)):
            #j is the length of the array
            for j in range(1, len(arr[0])):
                print(i,j)

                #f_(i-1,j-1) + S
                diag = arr[i-1,j-1] + substitution[(str(sequences[0][i-1]), str(sequences[1][j-1]))]
                #f_(i-1,j) + gap
                horiz = arr[i-1,j] - gap
                #f_(i-1,j) + gap

                vert = arr[i,j-1] - gap

                arr[i][j] = max([diag, horiz, vert])

    print(arr)
    return arr

