## I completed these 4 Qs in ~35 mins during onsite interview

## Question 1

## Write a program to check if a number is prime or not?

import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n/i == n//i):
            return -1
    return 1

print(isPrime(5))

## Question 2

## Given a rotated Array and a number, return the index of that number
##
## Input:
## list_number=[7,8,9,10,2,3,4,5,6], 9
##
## Output:
## 2

def index2(x,b):
    for i in range(0,len(x)):
        if (x[i] == b):
            return i
            
    return -1

A=[7,8,9,10,2,3,4,5,6]
print(index2(A,9))

## Second Approach

def index2b(shiftArr,num):
  start = 0
  end = len(shiftArr) - 1 
  while start <= end:
    mid = (start + end)//2
    if shiftArr[mid] == num:
      return mid
    elif shiftArr[start] <= num < shiftArr[mid] or (shiftArr[start] > shiftArr[mid] and not shiftArr[mid]<num<=shiftArr[end]):
	# We choose left half if either : 
	#    * left half is sorted and B in this range
	#    * left half is not sorted, 
	#      but B isn't in the sorted right half.
      end = mid-1
    else:
      start = mid +1
  return -1

print(index2b(A,9))

## Question 3

## Find Duplicate Characters 
## input = 'earniforlearn'
## 
## Output = 'rearn'

def findDuplicates(input):
    s = set()
    res = set()
    for a in input:
        if a in s:
            res.add(a)
        s.add(a)
    return list(res)  

print(findDuplicates('earniforlearn'))

## Question 4

## Given this data
##
## product_id,name,price
## 101,AMZN,100
## 101,ebay,200
## 101,target,300
## 101,walmart,400
## 102,amzn,200

## Find if Amazon has the Cheapest Price of a particular Product_id

def mini_index(A):
    for i in range(0,len(A)):
        if A[i] == min(A):
            return i

def isCheapestAMZ(product_id, name, price, input_product_id):
    refined_data_name = []
    refined_data_price = []
    for i in range(0,len(product_id)):
        if product_id[i] == input_product_id:
            refined_data_name.append(name[i])
            refined_data_price.append(price[i])
            
    mini_price_index = mini_index(refined_data_price)
    
    for i in range(0,len(refined_data_name)):
        if refined_data_name[i] == 'AMZN' and i == mini_price_index:
            return 1
    return 0

product_id = [101,101,101,101,102]
name = ['AMZN','ebay','target','walmart','AMZN']
price = [400,200,300,400,200]
print(isCheapestAMZ(product_id,name,price,102))

