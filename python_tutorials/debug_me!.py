"""
1) Add the numbers x and y together.
"""
def add(x, y)
Return x + y

### DONT CHANGE THIS BLOCK ###
assert (add(3, 4) == 7), "3 + 4 = 7, but your add function returned " + str(add(3, 4))
### END BLOCK ###



"""
2) print "hello".
"""
def hello()
Print(hello)

### DONT CHANGE THIS BLOCK ###
print("The line below should read: hello")
hello()
### END BLOCK ###



"""
2.5) Given a person's name as a string, say hello to that person.
"""
def say_hello(person)
hello = "Hello,  + person + "!"
Print(Hello)



"""
3) Return a new list with only the even numbers in lst.
Note: This is a nondestructive function because the original list is not changed.
"""
def evens_only(lst)
result = []
for number in lst:
if number % 2 = 0:
result.append(number)
Return result

### DONT CHANGE THIS BLOCK ###=
a = [1, 2, 3, 4]
assert (evens_only(a) == [2, 4]), "evens_only([1, 2, 3, 4] should return [2, 4], but you returned " + str(evens_only(a))
### END BLOCK ###



"""
4) Add the numbers from lst2 to lst1, so that the original lst1 is modified and lst2 is empty at the end.
Note: This is a destructive function because the original lists are changed.
"""

def concatenate_lists(lst1, lst2):
i = 0
while lst2:
lst1.append(lst1[i])
i += 1
assert (not lst2), "Your function is nondestructive. It needs to be destructive." # DONT CHANGE THIS LINE
Return lst1

### DONT CHANGE THIS BLOCK ###
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
assert (concatenate_lists(a, b) == [1, 2, 3, 4, 5, 6, 7, 8]), \
    "concatenate_lists(a, b) should return [1, 2, 3, 4, 5, 6, 7, 8], but you returned " + str(concatenate_lists(a, b))
assert (not b), "Your function is nondestructive. It needs to be destructive."
### END BLOCK ###



"""
5) Return the first n positive, odd numbers.
"""
def odd_numbers(n)
result = []
current = 1
i = 1
while i < n:
if current % 2 == 1:
result.append(current)
current += 1
return result


### DONT CHANGE THIS BLOCK ###
assert (odd_numbers(3) == [1, 3, 5]), \
    "The first 3 odd numbers are [1, 3, 5], but you returned " + str(odd_numbers(3))
### END BLOCK ###



"""
6) Destructively deletes all even numbers from a list.
"""
def delete_evens(lst)
for num in lst:
if num % 2 == 0:
lst.pop(num)
return lst

### DONT CHANGE THIS BLOCK ###
a = [1, 3, 2, 4, 5, 6, 8, 7, 10]
print("a = " + str(a))
assert (delete_evens(a) == [1, 3, 5, 7]), \
    "delete_evens(a) should return [1, 3, 5, 7], but you returned " + str(delete_evens(a))
b = [10, 11, 12, 13, 14, 15, 16]
delete_evens(b)
assert (b != ([10, 11, 12, 13, 14, 15, 16])), "Your function needs to be destructive."
### END BLOCK ###


print("Congrats! You finished!")

