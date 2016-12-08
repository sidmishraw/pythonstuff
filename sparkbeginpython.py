# Trying out Python basics
# Part 1 - Self study
# techniques covered in this -- unpacking(varargs), classes
# spark related
# modules - os, subprocess, sys
# shutil

import os
import sys
import subprocess
import shutil

# trying out unpacking of lists and dicts

# My observations--
# *listobj refers to the varargs style of specifying
# variable number of parameters are passed to the function
# and listobj refers to the tuple of those parameters
# in this example:
# I call unpack() from the main() by
# unpack(*listobj) where listobj = [1,2,3]
# so *listobj will unpack the list object listobj
# into a tuple having all the elements of
# listobj - (1,2,3) -- Note - tuples are immutable in Python
# this tuple is assigned to the unpack() as parameters.
# So, when I do type(listobj) - it will say that listobj is a tuple
# which is correct, but it fails when I do type(*listobj).
# This is because, *listobj represents the passes the arguments one at a time,
# *listobj means passing 1, then passing 2 and then passing 3
# instead of the tuple (1,2,3) - *listobj is the varargs
def unpack(*listobj):
  print('--- Implementation 1, just *listobj as parameter')
  list(map(lambda x: print("listobj mapping for %d" % x), listobj))
  print(type(listobj)) # will output <class 'tuple'>
  # print(type(*listobj)) will fail since *listobj is the representation of
  # varargs when they are not a tuple, it is same as passing 1, 2, 3 to the
  # type() each is an independent formal parameter on its own

# *listobj - just a tuple of values
# **dictobj - this is a dictionary unpacked - formally
# **dictobj is used to represent named parameters of form
# for eg:  unpack(element=value)
# so when I pass unpack(*listobj, **dictobj), it will unpack the
# (key,value) pairs of the dictobj and pass them as named arguments
# with the key as the name of the argument and value as the value for that
# named argument.
# Note - The keys need to be a string. They cannot be int or float or whatever
# IT MUST BE A STRING.
# Note - *dictobj will just unpack the keys of the dict and pass it to the method/function
# **dictobj will unpack the entire (key,value) pair and this is not a tuple
# In Python, a tuple is an immutable list (somewhat).
def unpack(*listobj, **dictobj):
    print('--- Implementation 2, *listobj and **dictobj as parameters')
    print('printing *listobj ', *listobj)
    print('printing listobj', listobj)
    # print(**dictobj) - fails since the keywords passed do not match
    # the keyword args needed by print()
    # though if they matched, it would have succeeded.
    print('printing dictobj', dictobj) # this will print out the dict, since that is what
    # namedparameters basically are, {parameter:value}

# self notes for python variadic arguments(varargs)
# one can unpack the contents of a list as multiple arguments
# to a function/method.
# in the example code below, I'm unpacking the listobj and dictobj
# and passing them to the unpack() that seems to be overloaded.
# Note - python does not offer explicit method overloading
# it is achieved using just one method, only Implementation 2
# will be called. Hence, use of default arguments and varargs(*vargs, **kwargs)
# achieves this scenario. *vargs - translates to the scenario when just a
# values are passed to the function/method
# **kwargs - translates to key-word varargs, we pass variable number of keyword
# arguments to the function/method.
def main():
  print('boilerplate code ready!')
  listobj = [1,2,3]
  dictobj = {1:0.5,2:0.75}
  unpack(*listobj) # in Implementation 2 - the **dictobj will be an empty dict {}
  # since I'm not passing a 2nd parameter to the unpack()
  # unpack(*listobj,**dictobj) - fails since dictobj doesn't
  # have string keys, so the named parameters fail
  # changing the dictobj to be a dict with string keys
  dictobj = {'namedParameter1': 0.5, 'namedParameter2': -0.75}
  unpack(*listobj,**dictobj)
  # passing *listobj and *dictobj to unpack()
  # now, I'm just passing vargs version, *dictobj will just pass the
  # keys of the dictobj as arguments to the method/function,
  # the keyset is unpacked and passed to the unpack().
  # both are appended to the *listobj argument of the method
  # since they are both *vargs and not **kwargs.
  # the **dictobj part is empty {}.
  unpack(*listobj,*dictobj)
  # list comprehension
  listcomprehended = [i for i in range(10) if i%2 == 0]
  # set comprehension
  setcomprehended = {i for i in range(101) if i%2 != 0}
  # dict comprehension
  dictcomprehended = {i:j for i,j in zip(range(10),range(20)) if i == j}
  print(listcomprehended,'\n' ,setcomprehended, '\n', dictcomprehended) 

# boiler-plate code for calling main()
# execute the main() only if the __name__ of the module is '__main__'
# Note - I need more clarification about this part.
if __name__ == '__main__':
  main()
