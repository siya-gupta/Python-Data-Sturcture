#!/usr/bin/env python
# coding: utf-8

# # Python Importatnt Notes By Siya Gupta

# # Types of Data Types
# - Boolean
# - Boolean and Logical Operators
# - Lists
# - Dictionaries
# - Tuples
# - Sets

# ## 1.Boolean
# - Boolean values are the two constant objects False and True.
# - They are used to represent truth values (other values can also be considered false or true).
# - In numeric contexts (for example, when used as the argument to an arithmetic operator), they behave like the integers 0 and 1, respectively.
# - The built-in function bool() can be used to cast any value to a Boolean, if the value can be interpreted as a truth value
# - They are written as False and True, respectively.

# In[1]:


#print(true)
#print(false)
#both statement will Give Error Beacuse Python is Case Sensentive and Boolean Should be Captital False, True.


# In[3]:


print(True,False)


# In[4]:


#Cheking Data Type
type(True)
type(False)


# In[46]:


my_str='SiyaaG123'


# In[53]:


print("This is My String",my_str)
print(my_str.isalnum()) #check if all char are numbers
print(my_str.isalpha()) #check if all char in the string are alphabetic
print(my_str.isdigit()) #test if string contains digits
print(my_str.istitle()) #test if string contains title words
print(my_str.isupper()) #test if string contains upper case
print(my_str.islower()) #test if string contains lower case
print(my_str.isspace()) #test if string contains spaces
print(my_str.isprintable())#test if String is Printable and returns True if all the characters are printable
print(my_str.isidentifier())#returns True if the string is a valid identifier, otherwise False
print(my_str.isascii())#returns True if the string is empty or all characters in the string are ASCII(American Standard Code for Information Interchange)
print(my_str.isnumeric())#test if string is Numeric
print(my_str.isdecimal())#test if string is Decimal
print(my_str.endswith('3')) #test if string endswith a d
print(my_str.startswith('S')) #test if string startswith H
print("All Are Boolean")


# In[50]:


print(my_str.upper())
print(my_str.lower())
print(my_str.format())#give Original Format 
print(my_str.translate(my_str))#Question 
print(my_str.casefold())#The casefold() method returns a string where all the characters are lower case.
print(my_str.replace('G','Gupta'))# Replace
print(my_str.capitalize())#The capitalize() method returns a string where the first character is upper case.
print('Retruns -1 Because G should be Captital',my_str.find('Siyag123'))
print(my_str.index('S'))
#The find() method finds the first occurrence of the specified value and returns -1 if the value is not found.
#The find() method is almost the same as the index() method
#the only difference is that the index() method raises an exception if the value is not found.
print(my_str.swapcase())#The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
print(my_str.find('S'))#first occurrence of the specified value and returns -1 if the value is not found.
print(my_str.count('a'))# Counts  


# ## Boolean and Logical Operators

# In[56]:


True and True


# In[57]:


True or True


# In[58]:


False and False


# In[59]:


False or False


# In[69]:


True or False


# In[70]:


True and False


# In[71]:


False and True 


# In[72]:


False or True


# In[68]:


my_str1='Siya'
my_str2='Gupta'
my_str1.isalpha() or my_str2.isnumeric()# Return True Beacuse True or False  = True


# # List

# - A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ]

# In[6]:


my_lst=[]#This is Empty List


# In[7]:


type(my_lst)


# In[8]:


my_lst = ["Bangalore","Hyderabad",{1,4},(1,2),{"Name":"Siya gupta","Age":22,'Designation':"DS and Python Enthisiatic"}]


# In[9]:


my_lst


# In[10]:


len(my_lst)


# In[11]:


my_lst[1]


# In[12]:


#Question how we can take key of dic 
my_lst[4]


# In[13]:


len(my_lst)


# In[14]:


type(my_lst)


# In[15]:


lst1=[1,2,3]
lst2=[3,4,5]
lst1+lst2#here (+) operator work as Concatenation 


# ### Append method
# - The append() method Appends an element to the end of the list.
# ### Syntax:
# - list.append(elmnt)
# 
# 

# In[16]:


my_lst.append(" Experience ")


# In[17]:


my_lst


# In[18]:


my_lst.append({'Data Analyst':'Python Developer'})#Adds its argument as a single element to the end of a list.The length of the list increases by one.
#if we want to add Any Data Type values or Single Element we can go with Append
my_lst# it adds it 3 times Beacuse i run it three times now we need to delete last element for this we will use pop method


# ### pop
# - The pop() method removes the element at the specified position.
# ### Syntax:
# - list.pop(pos)
# 

# In[19]:


my_lst.pop()


# In[150]:


my_lst


# In[20]:


my_lst.append({'Data Analyst':'Python Developer'})


# In[21]:


my_lst


# In[22]:


#my_lst.pop()#index which element we want to remove


# In[23]:


my_lst #now we want to insert a Element, wherever we want to insert. will use insert method


# ### insert
# - The insert() method inserts the specified value at the specified position.
# ### Syntax:
# - list.insert(pos, elmnt)

# In[24]:


my_lst.insert(6,{"Hometown":"Maharastra"})


# my_lst

# In[25]:


my_lst


# In[189]:


my_lst[4]


# ### Extend
# - The extend() method adds the specified list elements (or any iterable) to the end of the current list.
# ### Syntax:
# - list.extend(iterable)
# 
# 

# In[208]:


my_lst.extend(["What i am ",'I am Python Product'])


# my_lst

# In[222]:


my_lst


# ### Various Operations that we can perform in List¶
# 

# In[223]:



'''
my_lst.copy()
my_lst.remove()
my_lst.reverse()
my_lst.clear()
'''


# In[233]:


my_lst1=[4,9,100,1,2,3,4,5,5]


# In[234]:


my_lst1.sort()


# In[235]:


my_lst1


# In[239]:


my_lst1.sort()# sorting Lsit


# In[257]:


my_lst1


# In[241]:


max(my_lst1)# max number in list


# In[259]:


my_lst1[-2]#2nd Greatest  numbers in list


# In[261]:


my_lst1[-2:]# two Greatest numbers in list


# In[255]:


my_lst1.reverse()


# In[256]:


my_lst1


# In[249]:


sum(my_lst1)


# In[250]:


min(my_lst1)#smallest Number in list


# # Set
# - A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. Python's set class represents the mathematical notion of a set.This is based on a data structure known as a hash table
# - However, a set itself is mutable. We can add or remove items from it.
# - Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# In[26]:


my_st={1,2,3}


# In[27]:


my_st


# In[29]:


print(type(my_st))


# In[30]:


my_st={"Oranges","Apples","Grapes","Sapota"}


# In[35]:


type(my_st)


# In[36]:


my_st #set is unordered 


# In[41]:


my_st.add("Watermelon")# Adds an element to the set


# In[45]:


my_st.remove("Sapota")# Remove the elements from the set


# In[88]:


my_st.copy()


# In[101]:


st1={"Avengers","IronMan",'Hitman'}
st2={"Avengers","IronMan",'Hitman','Hulk2'}


# In[107]:


st2.intersection_update(st1)#Removes the items in this set that are not present in other, specified set(s)


# In[105]:


st2


# In[108]:


st1={"Avengers","IronMan",'Hitman'}
st2={"Avengers","IronMan",'Hitman','Hulk2'}


# In[109]:


st2.difference(st1)#Returns a set containing the difference between two or more sets


# In[110]:


print(st2)


# In[111]:


st2.difference_update(st1)#Removes the items in this set that are also included in another, specified set


# In[114]:


print(st2)


# In[117]:


st1={"Avengers","IronMan",'Hitman'}
st2={"Avengers","IronMan",'Hitman','Hulk2'}


# In[120]:


st2.intersection(st1)


# In[121]:


st2.issubset(st1)


# In[122]:


st2.issuperset(st1)


# In[123]:


st2.isdisjoint(st1)


# In[124]:


st2.symmetric_difference(st1)


# In[125]:


st2.symmetric_difference_update(st1)


# In[126]:


print(st2)


# In[127]:


print(st1)


# In[128]:


st1={"Avengers","IronMan",'Hitman'}
st2={"Avengers","IronMan",'Hitman','Hulk2'}


# In[129]:


st2.union(st1)


# In[130]:


st2.update()


# In[131]:


st2


# In[132]:


st2.update(st1)


# In[133]:


st2


# In[134]:


'''add() #Adds an element to the set
clear() #Removes all the elements from the set
copy() #Returns a copy of the set
difference() #Returns a set containing the difference between two or more sets
difference_update() #Removes the items in this set that are also included in another, specified set
discard() #Remove the specified item
intersection() #Returns a set, that is the intersection of two other sets
intersection_update() #Removes the items in this set that are not present in other, specified set(s)
isdisjoint() #Returns whether two sets have a intersection or not
issubset() #Returns whether another set contains this set or not
issuperset() #Returns whether this set contains another set or not
pop() #Removes an element from the set
remove() #Removes the specified element
symmetric_difference() #Returns a set with the symmetric differences of two sets
symmetric_difference_update() #inserts the symmetric differences from this set and another
union() #Return a set containing the union of sets
update() #Update the set with the union of this set and others'''


# ## Dictionaries
# - A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# - Dictionaries are used to store data values in key:value pairs.

# In[141]:


my_dic={}


# In[142]:


type(my_dic)


# In[152]:


my_dic={"Mahindra":"Scorpio ","Hyundai":"Venue","Toyota":"Inova","Lamborghini":"Aventador"}


# In[153]:


my_dic


# In[154]:


my_dic['Mahindra']


# In[155]:


for x in my_dic:
    print(x)


# In[156]:


for x in my_dic.values():
    print(x)


# In[157]:


for x in my_dic.keys():
    print(x)


# In[158]:


for x in my_dic.items():
    print(x)


# In[172]:


my_dic["Mercedes_Benz"]="E-Class"


# In[173]:


my_dic


# In[174]:


my_dic['Mahindra']="SUV"


# In[175]:


my_dic


# ## Nested Dictionary

# In[176]:


Mahindra_model= {'Mahindra':1945}
Hyundai_model= {'Hyundai':1967}
Toyota_model= {'Toyota':1937}
Lamborghini_model= {'Lamborghini':1963}
Mercedes_Benz_model= {'Mercedes-Benz':1926}


# In[187]:


Car_type={'Mahindra':Mahindra_model,'Hyundai':Hyundai_model,'Toyota':Toyota_model,'Lamborghini':Lamborghini_model,
          'Mercedes_Benz':Mercedes_Benz_model}


# In[188]:


Car_type


# In[197]:


print(Car_type['Mahindra']['Mahindra'])


# In[202]:


print(Car_type['Hyundai'])


# In[203]:


'''clear() #Removes all the elements from the dictionary
copy() #Returns a copy of the dictionary
fromkeys() #Returns a dictionary with the specified keys and value
get() #Returns the value of the specified key
items() #Returns a list containing a tuple for each key value pair
keys() #Returns a list containing the dictionary's keys
pop() #Removes the element with the specified key
popitem() #Removes the last inserted key-value pair
setdefault() #Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update() #Updates the dictionary with the specified key-value pairs
values() #Returns a list of all the values in the dictionary'''


# ## Tuple
# - A tuple is a collection which is ordered and unchangeable.
# - Tuples are written with round brackets.

# In[204]:


my_tpl=()


# In[205]:


type(my_tpl)


# In[208]:


my_tpl=tuple()


# In[210]:


type(my_tpl)


# In[213]:


my_tpl=("s","i","y","a")


# In[214]:


my_tpl


# In[216]:


my_tpl=('g','u','p','t','a')


# In[218]:


print(my_tpl)
print(type(my_tpl))


# In[223]:


my_tpl.index('a')


# In[224]:


my_tpl.count('u')

