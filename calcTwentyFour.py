# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:34:07 2019
Find a solution that evaluates four numbers to 24
Each number can be used exactly once, no more than that.
Operations are + - * /, () can be added
@author: xinch
"""

from itertools import permutations
from itertools import product
import sys

#gloval variable
opr=["+", "-", "*", "/"]
plMn= ["+","-"]
prDv = ["*", "/"]
mnDv = ["-", "/"]
found=False
expression= ""

"""
Utility Function that generates a string by merging two tuples alternatively,
given that size of first tuple is greater than the second
"""
def alternateMerge(tp1, tp2):
 i = 0; j = 0
 n =len(tp1)
 res=""
     
 while (i<n):
  res += tp1[i]
  i += 1
  if j< len(tp2):
      res+=tp2[j]
      j+=1
 return res

"""
Utility Function that evalutes a string expression and handle divide by 0
"""
def calcExpression(expr):
  result=0
  try:
    result= eval(expr)
  except ZeroDivisionError:
    result=0
  return result

"""
Case A:
    a +-*/ b +-*/ c +-*/ d
lst: a list of permutations of input numbers
"""
def computeCaseA(lst):
    global expression
    global found
    for perm in lst:
      if found == True:
              break
      for operm in product (opr, repeat=3):
        if found == True:
              break  
        expression=alternateMerge(perm, operm)
        if calcExpression(expression)==24:
          found=True
          break

"""
Case B:
    (a +- b) */ c +-*/ d
lst: a list of permutations of numbers
"""
def computeCaseB(lst): 
    global expression
    global found
   
    for perm in lst: 
      if found == True:
              break
      part1 = "("+ perm[0]
      for tmpop in plMn:
        if found == True:
              break
        part2 = tmpop + perm[1]+ ")"
        for tpop in prDv:
          if found == True:
              break
          part3= tpop + perm[2]
          for ops in opr:
              part4= ops+ perm[3]
              expression=part1+part2+part3+part4           
              if calcExpression(expression)==24:
                found=True
                break
   
"""
Case C:
    a -/ (b +- c) +-*/ d
lst: a list of permutations of numbers
"""
def computeCaseC(lst): 
    global expression
    global found
   
    for perm in lst: 
      if found == True:
              break
      for tmpop in mnDv:
        if found == True:
              break
        part1 = perm[0]+ tmpop
        for tpop in plMn:
          if found == True:
              break
          part2 ="("+perm[1]+tpop+perm[2]+")"
          if tmpop == "-":         
              for ops in prDv:
                  part3= ops+ perm[3]
                  expression=part1+part2+part3
                  if calcExpression(expression)==24:
                    found=True
                    break
          elif tmpop == "/":
              for ops in opr:
                  part3 = ops+ perm[3]
                  expression=part1+part2+part3
                  if calcExpression(expression)==24:
                    found=True
                    break
   
"""
Case D:
    a - / b */ (c +- d)
lst: a list of permutations of numbers
"""
def computeCaseD(lst): 
    global expression
    global found
    
    for perm in lst: 
      if found == True:
              break
      for tmpop in mnDv:
        if found == True:
              break
        part1 = perm[0]+ tmpop 
        for tpop in prDv:
          if found == True:
              break
          part2=perm[1]+tpop+"("+perm[2]
          for ops in plMn:         
            part3= ops+ perm[3] +")"
            expression=part1+part2+part3
            if calcExpression(expression)==24:
                found=True
                break
  
"""
Case E:
    (a +-*/ b +-*/ c) */ d
lst: a list of permutations of numbers
"""
def computeCaseE(lst): 
    global expression
    global found
   
    for perm in lst: 
      if found == True:
              break
      part1 ="("+ perm[0]
      for tmpop in opr:
        if found == True:
              break
        part2 = tmpop + perm[1]
        if tmpop=="+" or tmpop=="-":
          for tpop in opr:
            if found == True:
              break
            part3 = tpop+perm[2]+")"
            for ops in prDv:
              part4 = ops+perm[3]
              expression=part1+part2+part3+part4
              if calcExpression(expression)==24:
                found=True
                break
        else:
          for tmpop in plMn:
            if found == True:
              break
            part3 =tpop+perm[2]+")"
            for ops in prDv:
              part4 = ops+perm[3]
              expression=part1+part2+part3+part4
              if calcExpression(expression)==24:
                found=True
                break

"""
Case F:
    a / (b +-*/ c +-*/ d)
lst: a list of permutations of numbers
"""
def computeCaseF(lst): 
    global expression
    global found

    for perm in lst:
      if found == True:
              break
      part1 = perm[0]+ "/"+"("+perm[1]
      for tmpop in opr:
        if found == True:
              break
        part2 = tmpop+perm[2]
        if tmpop=="+" or tmpop=="-":
          for tpop in opr:
            part3 = tpop+perm[3]+")"
            expression=part1+part2+part3
            if calcExpression(expression)==24:
                found=True
                break 
        else:
          for tmpop in plMn:         
            part3 = tpop+perm[3]+")"
            expression=part1+part2+part3
            if calcExpression(expression)==24:
              found=True
              break
           
"""
Case G:
    (a +- b) */ (c +-d)
lst: a list of permutations of numbers
"""
def computeCaseG(lst): 
    global expression
    global found
    
    for perm in lst:
      if found == True:
              break
      part1 = "("+perm[0]
      for tmpop in plMn:
        if found == True:
              break
        part2 = tmpop+perm[1]+")"
        for tpop in prDv:
          if found == True:
              break
          part3 = tpop+"("+perm[2]
          for ops in plMn:
            part4 = ops+perm[3]+")"
            expression=part1+part2+part3+part4
            if calcExpression(expression)==24:
              found=True
              break
          
def calcTwentyFour(numLst):
   perms = list(permutations(numLst))
   global found

   computeCaseA(perms)
   if found:
      return expression+"=24"
   else:
      computeCaseB(perms)
      if found:
        return expression+"=24"
      else:
        computeCaseC(perms)  
        if found:
         return expression+"=24"
        else:
         computeCaseD(perms)  
         if found:
          return expression+"=24"
         else:
          computeCaseE(perms)  
          if found:
            return expression+"=24"
          else:
            computeCaseF(perms)  
            if found:
             return expression+"=24"
            else:
             computeCaseG(perms)  
             if found:
              return expression+"=24"
             else:
              return "No solution exists."   
             
   
#perms = list(permutations(["9","2","2","5"]))
#computeCaseE(perms)

#print(calcTwentyFour(perms))

if len(sys.argv)!=5:
    print("Please enter exactly 4 numbers.")
else:
  nums= sys.argv[1:]
  print(calcTwentyFour(nums))