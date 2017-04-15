# Dynamic programming implementation of LCS problem

import re

def verify(s):
    return (re.match("^[ATCG ]*$",s)) 
    #verify(),regex is used to compare the given string has 'A','T','C','G',' ' only and nothing else.

# Returns length of LCS for X[0..m-1], Y[0..n-1] 
def lcs(X, Y, m, n):
    L = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
 
    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] 
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # Following code is used to print LCS
    index = L[m][n]
 
    # Create a character array to store the lcs string
    lcs = [""] * (index+1)
    lcs[index] = "\0"
 
    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
 
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
 
        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
 
    print "\n\nLCS of " + X + " and " + Y + " is " + "".join(lcs) + " \nand length of it is : " + str(len("".join(lcs))-1)
 
s1,s2=input("Enter the First Sequence\n").upper(),input("\nEnter the Querying Sequence\n").upper()

if (verify(s1) and verify(s2)) and (len(s1)>=len(s2)):
    print(s1,s2)
    m=len(s1)
    n=len(s2)
    lcs(s1,s2,m,n)

elif (not(len(s1)>=len(s2))):
    #the length of the Querying string should be smaller in order to perfom the search over the First String.
    print("Querying Sequence should be smaller than First Sequence")

else:
    print("The Sequences should contain 'A','T','C','G',' ' only")