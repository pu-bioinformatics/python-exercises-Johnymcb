#!/bin/bash
def validSequence(sequence):
        valid = 'ACTG'
        for base in sequence:
            if base   not in valid:
                return("is not a valid DNA sequence")
            
DNA_test = validSequence(input("paste here your sequence: "))
print ("my sequence  %s" % (DNA_test))

#CK: The idea is to use this function to test if the DNA is valid before calculating the GC content -2
## In that case, it should return true of false