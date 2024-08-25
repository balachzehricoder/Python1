student_list= ["Balach", "Hadi","Ahsan","Zaid", "Fatima", "Ali", "Ahmed"]
print(student_list)

# specific index
print(student_list[5])


# replace 
student_list[2]= "zara"
print(student_list)



# add
student_list.append("zaid godila")

print(student_list)


# remove
student_list.remove("zaid godila")
print(student_list)


# pop

student_list.pop(2)
print(student_list)



# insert
student_list.insert(2,"zahid")
print(student_list)


#sort
student_list.sort()
print(student_list)

#reverse
student_list.reverse()
print(student_list)


#copy
student_list2= student_list.copy()
print(student_list2)
#extend
student_list.extend(student_list2)
print(student_list)

#clear
# student_list.clear()
# print(student_list)


# in
print("Zaid" in student_list)


# len
print(len(student_list))

#count
print(student_list.count("Zaid"))

#index
print(student_list.index("Fatima"))