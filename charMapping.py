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

