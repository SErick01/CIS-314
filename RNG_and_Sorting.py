"""
Author: Samantha Erickson
Date:   09-14-2024

QUESTION 1 (Max Range 16):"Based on the counts, does one method appear better than the other?" 
    Upon evaluating the frequency of each number, neither the random nor secrets appear to be superior to one another.
						
QUESTION 2 (Max Range 65535):"Based on the counts, does one method appear better than the other?"					
    Based on the outputted data, I can not tell if 'random' or 'secrets' is better.
    From what I read, I know that 'secrets' are better because 'random' is not cryptographically secure.
    I tried plugging the data into a pattern recognition calculator, and both data sets stumped it.

QUESTION 3 (Sample Size 100): "Does the sorting time change? Is one more efficient with larger numbers?"
    Yes, the built-in sort function fluctuated quite a bit with its time laps. 
    However, the insertion sort appeared more consistent. 
    The built-in sort function was always much faster than the insertion sort function.

QUESTION 4 (Sample Size 500): "Does the sorting time change? Is one more efficient with larger numbers?"
    Yes, the built-in sort function is still fluctuating with its time laps. 
    However, the insertion sort still appears more consistent. 
    The insertion sort function struggled with the increased size, while the built-in sort function handled it well.
"""
import random, secrets, timeit

randomSmall, secretsSmall, randomBig, sercretsBig, randomHuge = [], [], [], [], []
smallMax, bigMax, smallSize, bigSize = 16, 65535, 100, 500

"""
Number Generator Functions Here
"""
def Random_Sample(max, size, list):
    for i in range(0,size):
        first = random.randint(1,max)
        list.append(first)        
    # print("Random Sample...\n",randomList,"\n")                   # Line hashed out for convenience purposes.

def Secrets_Sample(max, size, list):
    for i in range(0,size):
        second = secrets.randbelow(max)
        list.append(second)
    # print("Secrets Sample...",secretsList,"\n")                   # Line hashed out for convenience purposes.

"""
Dictionary Counter Functions Here
"""
def Random_Dictionary(list):
    dictRandom = dict((i, list.count(i)) for i in list)
    
    print("Dictionary Random Keys:",dictRandom.keys(),"\n")
    print("Dictionary Random Values:",dictRandom.values(),"\n")

def Secrets_Dictionary(list):
    dictSecrets = dict((i, list.count(i)) for i in list)
    
    print("Dictionary Secrets Keys:",dictSecrets.keys(),"\n")
    print("Dictionary Secrets Values:",dictSecrets.values(),"\n")
"""
Sorting Functions Here
"""
def Insertion_Sort(list):
    start = timeit.default_timer()

    for i in range(1, len(list)):
        m = list[i]
        n = i - 1

        while n >= 0 and list[n] > m:
            list[n + 1] = list[n]
            n -= 1
        list[n + 1] = m
    
    stop = timeit.default_timer()
    dif = stop - start
    # print("Sorted Insertion Sample...\n",list)                    # Line hashed out for convenience purposes.
    print("Time laps in Insertion_Sort is: %.9f seconds\n" % dif)

    return list

def Sorting(list):
    start = timeit.default_timer()
    list.sort()
    stop = timeit.default_timer()
    dif = stop - start
    # print("Sorted Sample...\n",list)                              # Line hashed out for convenience purposes.
    print("Time laps in Sorting is: %.9f seconds\n" % dif)
"""
Calls - Small Number Generator Functions plus Counter Functions
"""
Random_Sample(smallMax, smallSize, randomSmall)
Secrets_Sample(smallMax, smallSize, secretsSmall)
Random_Dictionary(randomSmall)
Secrets_Dictionary(secretsSmall)
"""
Calls - Big Number Generator Functions plus Counter Functions
"""
Random_Sample(bigMax, smallSize, randomBig)
Secrets_Sample(bigMax,smallSize, sercretsBig)
Random_Dictionary(randomBig)
Secrets_Dictionary(sercretsBig)
"""
Calls - Small Sorting Functions
"""
Insertion_Sort(randomSmall)
Sorting(randomSmall)
"""
Calls - Big Sorting Functions
"""
Insertion_Sort(randomBig)
Sorting(randomBig)
"""
Calls - Big Number Generator Functions plus Sorting Functions (500 sample size)
"""
Random_Sample(bigMax, bigSize, randomHuge)
Insertion_Sort(randomHuge)
Sorting(randomHuge)