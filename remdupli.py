#Implement a program that takes a list and removes duplicates.
def remove_duplicates(input_list):
    return list(set(input_list))

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
result = remove_duplicates(input_list)

print("Original list:", input_list)
print("List after removing duplicates:", result)
