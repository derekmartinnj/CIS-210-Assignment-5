'''
Author: Derek Martin
Assignment: Project 5.1 Data Analysis CIS 210 Winter 2019
Credits: N/A
Description: Implement functions that organize and display data sets into frequency tables, and calculate key values such as mean, median, and mode.
'''
import doctest

def mean(alist):
    '''
    (list) -> float

    Return the mean (average) numeric value in a given list.

    >>> mean([1,2,4,9])
    4.0
    >>> mean([])
    ZeroDivisionError
    '''
    #doctest.testmod
    mean = sum(alist) / len(alist)
    return mean

def median(alist):
    '''
    (list) -> number

    Sort the given list and return the median (middle) numeric value.

    >>> median([6,12,49,17,14,3,9])
    12
    >>> median([])
    IndexError
    '''
    #doctest.testmod
    copylist = alist[:] # make a copy using slice operator
    copylist.sort()
    copylen = len(copylist)
    if isEven(copylen): # even length
        rightmid = copylen // 2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid]) / 2
    else:   # odd length
        mid = copylen // 2
        median= copylist[mid]
    return median

def mode(alist):
    '''
    (list) -> list

    Return a list of modes (most common numeric values) in a given list.

    >>> mode([3,1,4,5,4,6,2,4,3,6])
    [4]
    >>> mode([])
    ValueError
    '''
    #doctest.testmod
    countdict = genFrequencyTable(alist)
    countlist = countdict.values() # retrieve values of countdict
    maxcount = max(countlist) # find max value in countlist
    modelist = [ ]
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item) # add items in countdict with the 'maxvalue' to the mode list
    return modelist

def frequencyTable(alist):
    '''
    (list) -> None

    Print a frequency table that displays data from the given list

    > frequencyTable([1, 3, 3, 2])
    ITEM FREQUENCY
    1     1
    2     1
    3     2 
    > frequencyTable([])
    ITEM FREQUENCY
    '''
    #doctest.testmod
    countdict = genFrequencyTable(alist)
    itemlist = list(countdict.keys())
    itemlist.sort() # must sort list in order to display organized frequency table
    print("ITEM","FREQUENCY")
    for item in itemlist:
        print(item, "   ",countdict[item])

def isEven(n):
    '''
    (number) -> boolean

    Determine if 'n' is even or odd, and return True or False accordingly

    >>> isEven(4)
    True
    >>> isEven()
    TypeError
    '''
    #doctest.testmod
    isEven = False
    if (n % 2) == 0:
        isEven = True
    return isEven

def genFrequencyTable(alist):
    '''
    (list) -> dict
    
    Generate a dictionary using given values from 'alist' as keys

    >>> genFrequencyTable([6,4,14,9])
    {6: 1, 4: 1, 14: 1, 9: 1}
    >>> genFrequencyTable([])
    {}
    '''
    #doctest.testmod
    countdict = {}
    for item in alist:
        if item in countdict:
            countdict[item] = countdict.get(item,0)+1 # use 'get' to display 0 as error message (if needed)
        else:
            countdict[item] = 1
    return countdict

def main():
    ''' Used to call all functions in the file and display results '''
    equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
    2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
    4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
    4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
    2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
    4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
    3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
    2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
    2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
    6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
    2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
    2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
    4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
    4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
    2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
    2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
    2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
    4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
    4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
    2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
    3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
    2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
    2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
    2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
    2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
    2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
    3.1, 4.6, 2.8, 3.1, 6.3]
    frequencyTable(equakes)
    print("Mean:", mean(equakes))
    print("Median:", median(equakes))    
    print("Mode:", mode(equakes))
    
main()

