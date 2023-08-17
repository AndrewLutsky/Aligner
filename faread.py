class sequence:
    #constructor method
    def __init__(self, seq):
        self.seq = seq
    def seqstring(self):
        return self.seq
    def reverse(self):
        return self.seq[::-1]


         
def main():
    
    #read in fasta file
    with open("samplefasta.fasta", "r") as r:
        text = r.read()
    r.closed

    text = text.splitlines()
    lisSequence = []
    for line in text:
        if line[0] != '>':
            lisSequence.append(line)

    lisSequenceObjects = []
    for seq in lisSequence:
        sequen = sequence(seq)
        lisSequenceObjects.append(sequen)

    print(lisSequenceObjects)
    
    for i in lisSequenceObjects:
        print(i.seqstring())

if __name__ == "__main__": 
    main()
