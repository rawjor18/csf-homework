# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###
from hw2_test import n
print n

num = 0
i = 1 
while i < n + 1:
    num = num + i 
    i = i + 1
# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"
print num
###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"
for n in range (2,11):
    print 1.0/n
# ... write your code and comments here (and remove this line)


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"
n = 10
triangular = 0
for i in range (1,n+1):
    triangular = + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2
# ... write your code and comments here (and remove this line)

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"
n = 10
f = 1
for i in range (1,n+1):
    f = f * i
print f
# ... write your code and comments here (and remove this line)

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"
n = 10
f = 1
c = n

for j in range (1 , n + 1):
    for i in range (1 , c + 1):
        f = f * i
    print f
    f = 1
    c = c - 1
# ... write your code and comments here (and remove this line)

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"
n = 10
t = 1
c = n

for j in range (1 , 11):
    f = 1
    for i in range (1 , j + 1):
        f = f * i
    t = t + (1.0 / f)
print t
# ... write your code and comments here (and remove this line)

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
