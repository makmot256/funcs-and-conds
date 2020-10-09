#using the def function for elements that donot repeat themselves
from collections import Counter
def single_element(lst):
    for num in lst:
        x = lst.count(num)
        if x == 1:
            return num

print(single_element([2,2,1]))
print(single_element([4,1,2,1,2]))
print(single_element([6,7,4,4,7]))

# from collections  import Counter
# def johnson1(lst):
#     for num in lst:         
#         x = lst.count(num)
#     if x == 1:
#       return num

# print(johnson1([2, 2, 1]))
# print(johnson1([4, 1, 2, 1, 2]))
# print(johnson1([6, 7, 4, 4, 7]))
 