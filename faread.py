class sequence:
    #constructor method
    def __init__(self, seq):
        self.seq = seq
    def reverse(self):
        return self.seq[::-1]


    
def readsequences(data):
    data = data.splitlines()
    lisSequence = []
    
    
    #This is janky needs to be fixed
    for line in data:
        if line[0] != '>':
            lisSequence.append(line)
    
    
    #creates list of sequence objects
    lisSequenceObjects = []
    for seq in lisSequence:
        sequen = sequence(seq)
        lisSequenceObjects.append(sequen)
    
    return lisSequenceObjects
        
