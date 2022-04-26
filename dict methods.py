# get methods

# dict={'a':2,'b':3,'c':4,'d':7,'e':6}
# a=dict.get("b")
# print(a)

# romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5 }
# value = romanNums.get('I')
# print("I = ",value)


# romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5 }
# value = romanNums.get('VI')
# print("VI = ", value)


# agar vo kye usme nhi hai to none print karega

# dict={'a':2,'b':3,'c':4,'d':7,'e':6}
# a=dict.get("f")
# print(a)

# sum={"name":"[ooja","class":12,"father name":"ramadhar","mother name":"gayanwati"}
# a=sum.get("name")
# print(a)


# dict={1:1,2:2,3:"jaan",4:4,5:5}
# a=dict.get(3)
# print(a)


# specfic value

# friends={1:"pooja",2:"madhu",3:"shivani",4:"deepshikha"}
# a=friends.get(4)
# print(a)





# add methodes
# update
# zip
# counter




# add methods


# a={"shivani","deepshikha","madhu","pooja"}
# a.update({"miss you"})
# print(a)


# a={1:10,2:20,3:30,4:40,5:50,6:60}
# a.update({"name":"pooja"})
# print(a)


# a={"a":2.34,"b":11.21,23:"pooja",12.12:"rani"}
# a.update({"dad":"mom"})
# print(a)



# a={"soni":17,"madhu":23,"shivani":20,"pooja":20,"deepshikha":22}
# a.update({"jaan":21})
# print(a)


# thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
# thisdict.update({"color": "red"})
# print(thisdict)






# update methods

# car = {"brand": "Ford","model": "Mustang","year": 1964}

# x = car.values()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change



# a={"soni":17,"madhu":23,"shivani":20,"pooja":20,"deepshikha":22}
# a.update({"pooja":21})
# print(a)


# a={1:10,2:20,3:30,4:40,5:50,6:60}
# a.update({1:90})
# print(a)


# a={"a":2.34,"b":11.21,23:"pooja",12.12:"rani"}
# a.update({"b":"mom"})
# print(a)


# dict={"subha":"good morning","dupaihre":"good afternoon","saam":"good evning","raat":"good night"}
# dict.update({"subha":"love good morning"})
# print(dict)







# zip methods


# a={1,2,3,4,5}
# b={6,7,8,9,10}
# zip=dict(zip(a,b))
# print(zip)



# doubt
# a={"shivani","deepshikha","madhu","pooja"}
# b={"jaan","janu","jani","janeman"}
# zip=dict(zip(a,b))
# print(zip)

# a={"shivani","deepshikha","madhu","pooja"}
# b={"1","2","3","4"}
# zip=dict(zip(a,b))
# print(zip)


 

# counter methods


# dict1 = {'a':1,'b':2,'c':3}
# print(len(dict1.keys()))


# dict1 = {'a':1,'b':2,'c':3}
# print(len(dict1))


# dict1 = {'a':1,'b':2,'c':3}

# def count_keys(dict):
#     count = 0
#     for i in dict:
#         count += 1
#     return count

# print(count_keys(dict1))

# fruits = ['apple', 'banana', 'cherry',"cherry"]
# x = fruits.count("cherry") 
# print(x)


# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

# x = points.count(9)
# print(x)


# dict1 = {'a':1,'b':2,'c':3}

# def count_keys(dict):
#     count = 0
#     for i in dict:
#         count += 1
# #     return count

# print(count_keys(dict1))


## counter methods


# dict1 = {'a':1,'b':2,'c':3}
# print(len(dict1.keys()))


# dict1 = {'a':1,'b':2,'c':3}
# print(len(dict1))


# dict1 = {'a':1,'b':2,'c':3}

# def count_keys(dict):
#     count = 0
#     for i in dict:
#         count += 1
#     return count

# print(count_keys(dict1))

# fruits = ['apple', 'banana', 'cherry',"cherry"]
# x = fruits.count("cherry") 
# print(x)


# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

# x = points.count(9)
# print(x)


# dict1 = {'a':1,'b':2,'c':3}

# def count_keys(dict):
#     count = 0
#     for i in dict:
#         count += 1
# #     return count

# print(count_keys(dict1))



# copy methods


# num= {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5 }
# newnum=num.copy()
# print("Original dictionary: ",num)
# print("Copied dictionary: ",num,)




# a = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5 }
# b = a.copy()
# del a['V'] # deleting 'V'
# print("Original dictionary: ",b)
# print("Copied dictionary: ",a)



# fromkeys methods

# keys = {'Mumbai','Bangalore','Chicago','New York'}
# value = 'city'
# dictionary = dict.fromkeys(keys, value)
# print(dictionary)


# nums = (1, 2, 3, 4, 5) # tuple to dict
# val = 'Numbers'
# numDict = dict.fromkeys(nums, val)
# print(numDict)





# a= ['k:1','D:2','k:3']
# b={}
# for x in a:
#   key,value=x.split(':')
#   b[key]=int(value)
# print(b)


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
