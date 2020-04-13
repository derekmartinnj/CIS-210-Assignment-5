'''
Author: Derek Martin

Project:
Testing and debugging
CIS 210 Project 5-2 Winter 2019

Credits: N/A

Description: Functions need to be tested.
'''
import doctest

def bigSalesBug(sales_list):
    '''(list) -> number

    Returns sum of all sales for amounts at or over $40,000.
    sales_list has the record of all the sales.

    >>> bigSalesBug([40000, 45.67, 19000.0, 25000, 100000])
    140000.0
    >>> bigSalesBug([])
    0.0
    >>> bigSalesBug([''])
    TypeError
    >>> bigSalesBug([1])
    0.0
    '''
    total = 0.00
    for sales in sales_list:
        if sales >= 40000: # changed '40_000' to '40000' , changed '>' to '>=', and added ':'
            total += sales # corrected spelling of 'sales'
    return total # fixed indent formatting of return statement

def ratsBug(weight, rate):
    '''(number, number) -> tuple

    Return number of weeks it will
    take for a rat to weigh 1.5 times
    as much as its original weight
    (weight > 0) if it gains at rate (rate > 0).

    >>> ratsBug(10, .1)
    (16.1, 5)
    >>> ratsBug(0)
    TypeError
    >>> ratsBug(0,0)
    (0, 0)
    >>> ratsBug(15, 90)
    (1365, 1)
    '''
    weeks = 0
    initialweight = weight # Initialized temporary variable to avoid infinite loop
    while weight < (1.5 * initialweight):
        weight += weight * rate
        weeks += 1
        
    weight = round(weight, 1)
    return (weight, weeks)

def my_averageBug(dataset):
    '''(list of numbers) -> float

    returns average of values in dataset,
    but zeros do not count at all
    
    >>> my_averageBug([2, 3])
    2.5
    >>> my_averageBug([2, 0, 3])
    2.5
    >>> my_averageBug([])
    ZeroDivisionError
    >>> my_averageBug([5])
    5.0
    >>> my_averageBug([-2,6,4])
    2.6666666666666665
    '''
    count = 0
    total = 0
    for value in dataset:
        if value != 0: # changed '0' from string to int
            total += value
            count += 1 # fixed indent formatting

    avg = total / count
    return avg

def countSeqBug(alist):
    '''(list) -> int

    Returns the length of the longest recurring
    sequence in alist, a list of strings.

    >>> countSeqBug(['a', 'b', 'c', 'c', 'd', 'e'])  	
    2
    >>> countSeqBug([])
    0
    >>> countSeqBug([7])
    1
    >>> countSeqBug([1,1,1,2,2,2])
    3
    >>> countSeqBug(['a',4])
    1
    '''
    if len(alist) != 0:
        prev_item = alist[0]
        dup_ct = 1
        high_ct = 1
    else:
        high_ct = 0
        dup_ct = 0
        
    for i in range(1, len(alist)):
        if alist[i] == prev_item:
            dup_ct += 1
        else:
            prev_item = alist[i]
			
            if dup_ct > high_ct:
                high_ct = dup_ct
            dup_ct = 1

    return high_ct

def salesReportBug(salesli):
    '''(list) --> None

    Prints report of sales totals for each day of week (salesli)
    and range of per-day sales. salesli is non-empty - 0 sales
    for any day are reported as 0.

    >>> salesReportBug([40000, 45.67, 19000.0, 25000, 100000])
    Weekly Range: $45.67 - $100,000.00
    
    Mon          Tue          Wed          Thu          Fri         
    $40,000.00   $45.67       $19,000.00   $25,000.00   $100,000.00
    '''
    copylist = salesli[:] # duplicate list to avoid aliasing with other function
    
    #calculate and report low and high sales
    low, high = findRangeBug(salesli)
    print(f'Weekly Range: ${low:,.2f} - ${high:,.2f}\n')

    #print daily report header
    fw = 12
    print(f"{'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} {'Thu':<{fw}} {'Fri':<{fw}}")

    #report on sales per day from list data
    for sales in copylist: # reference copy list
        print(f'${float(sales):<{fw},.2f}', end='')
        
    return None

def findRangeBug(salesli):
    '''(list) -> tuple

    Returns largest and smallest number in non-empty salesli.
    (Note that Python has built in funcs max and min
    to do this, but not using them here, so we can
    work with the list directly.)

    >>> findRangeBug([40000, 45.67, 19000.0, 25000, 100000])
    (45.67, 100000.0)
    >>> findRangeBug([])
    IndexError
    >>> findRangeBug([17])
    (17.0, 17.0)
    >>> findRangeBug(['abc'])
    ValueError
    '''
    salesli.sort() # Removed NoneType assignment
    low = float(salesli[0])
    high = float(salesli[-1])
    return low, high

print(doctest.testmod())
