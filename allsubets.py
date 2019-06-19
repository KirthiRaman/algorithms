#!/usr/bin/env python3

def print_set(arr):
   s = set(arr)
   stre = "("
   for item in s:
       if item != "null":  stre += str(item)+","
       #else: stre += "{},"
   if stre[-1] == ",": stre = stre[:-1]
   print(stre+")")

def all_subsets(arr):
   subset = len(arr)*["null"]
   helper(arr,subset,0)

def helper(arr,subset,i):
   if i == len(arr):
      print_set(subset)
   else:
      subset[i] = "null"
      helper(arr,subset,i+1)
      subset[i] = arr[i]
      helper(arr,subset,i+1)

l = [1,2,3]
all_subsets(l)
# Results printed 
#()
#(3)
#(2)
#(3,2)
#(1)
#(1,3)
#(1,2)
#(1,2,3)
