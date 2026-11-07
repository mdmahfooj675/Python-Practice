# insert some element at the end , insert at particular index , and remove some element

print("question -> insert some element at the end , insert at particular index and remove the some element")

marks = [65 , 88 , 98 , 78 , 90 , 45]

# insert some element using the append method
marks.append(86)
print("after append the latest list : " , marks)

marks.append(59)
print("after append the latest list : " , marks)

marks.append(94)
print("after append the latest list : " , marks)


# insert the element at a particular index using insert method
marks.insert(2,77)
print("append element at particular index : " , marks)
      
marks.insert(5,86)
print("append element at particular index : " , marks)
      
marks.insert(4,97)
print("append element at particular index : " , marks)


# remove the  element using remove method 
marks.remove(98)
print("after remove method : " , marks)

marks.remove(45)
print("after remove method : " , marks)

# remove the element in a certain index using pop method
marks.pop(5)
print("atfer pop function : " , marks)

marks.pop(4)
print("after pop function : " , marks)


print("code ended....")