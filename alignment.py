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
    def __init__(self, sequences, method, substitution):
        self.matrix = align(method, sequences)
        self.pathTracing = pathTracing(self.matrix)
        self.method = method
        self.substitution = substitution




    
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
    arr = nw(sequences)
    return arr

#Matrix is flipped over diagonal -> to fix
def nw(sequences) -> list:
    substitution = charMappingDefault(sequences[0], sequences[1])
    print(substitution)
    print("The lengths of sequences 0 and 1 respectively are: ",len(sequences[0]), len(sequences[1]))

    arr = np.zeros((len(sequences[1])+1,len(sequences[0])+1), dtype = int)
    gap = 1
    #mapping the first column and row of array
    #need to do separately in case strings are of different sizes
    #can't assume gap penalty
    for i in range(0, len(arr[0])):
        arr[0][i] = -i * gap
    for i in range(0, len(arr)):
        arr[i][0] = -i * gap

    #matrix filling
    #i is width of array
    for i in range(1, len(arr)):
            #j is the length of the array
            for j in range(1, len(arr[0])):
                print(i,j)
                #f_(i-1,j-1) + S
                diag = arr[i-1,j-1] + substitution[(sequences[0][j-1], sequences[1][i-1])]
                #f_(i-1,j) + gap
                horiz = arr[i-1,j] - gap
                #f_(i-1,j) + gap

                vert = arr[i,j-1] - gap

                arr[i][j] = max([diag, horiz, vert])
    print(arr)
    return arr

def pathTracing(arr) -> list:
    path = []
    i, j = len(arr)-1, len(arr[0])-1
    path.append((i,j))
    while (i, j) != (0, 0):
        if (i < 0 or j < 0):
            raise ValueError("Path Tracing Failed")
        print(i,j)
        #find the max value for diagonal, vertical, and horizontal and
        diag = (i-1, j-1)
        horiz = (i, j-1)
        vert = (i-1, j)
        
        diagValue = arr[diag[0], diag[1]]
        horizValue = arr[horiz[0], horiz[1]]
        vertValue = arr[vert[0], vert[1]]
        flagCheckZeros = (i == 0 or j == 0)
        print(flagCheckZeros)
        if not (flagCheckZeros):
            #if diagonal add i and j to the positions
            if diagValue >= horizValue and diagValue >= vertValue:
                path.append(diag)
                i, j = diag[0], diag[1]
            elif horizValue >= diagValue and horizValue >= vertValue:
                path.append(horiz) 
                i, j = horiz[0], horiz[1]
            else:
                path.append(vert)
                i, j = vert[0], vert[1]
        else:
            print("on edge")
            #need to check if on vertical or horizontal edge
            #vertical edge
            if j == 0:
                print("appended vertical on edge")
                path.append(vert)
                i,j = vert[0],vert[1]
            #horizontal edge
            else:
                print("horizontal edge")
                path.append(horiz)
                i,j = horiz[0], horiz[1]
    return path

def charMappingDefault(seq1, seq2) -> dict:
    listCharMaps = []
    substitution = {}
    #Complexity is O(len(seq1) * len(seq2)) minimum, could reduce by minimizing halving the number of chars to map
    #Characters can be done interchangably
    #Issue ticket
    for charSetOne in seq1:
        for charSetTwo in seq2:
            if charSetOne == charSetTwo: 
                substitution[(charSetOne, charSetTwo)] = 1
            else:
                substitution[(charSetOne, charSetTwo)] = -1
    return substitution

def customMapping(customMatrix) -> dict:
    #not implemented
    raise NotImplemented("custom matrix mapping is not implemented")
    return {}
