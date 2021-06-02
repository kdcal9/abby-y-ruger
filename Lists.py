# names = ['john', 'katie', 'sarah', 'darrn', 'jeff']
# print(names[2])
# #square brackets will provide a new list but does not modify the original list. 
# names[0] = 'Jon'
# print(names)

#return highest number in a list
# numbers = [3,7,2,22,1,4,5]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


# #2D lists
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# #nested for loop
# for row in matrix:
#     for item in row:
#         print(item)


#methods in lists, example below is removing duplicates
# numbers = [5,2,1,7,4,10, 7, 4]
# uniques = []

# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# #tuples
# numbers = (1,2,3)
# print(numbers[0])

#unpacking
coordinates = (1,2,3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

#shorthand to acheive the same results - assigning another variable to a item in a tuple or list.
# x,y,z = coordinates
# print(x)

#dictionaries
# customer = {
#     'name': 'John Smith',
#     'age': 30,
#     'is_verified': True
#     }

# print(customer['name'])
# print(customer.get('birthday', 'birthday not assigned'))

# phone = input("Phone: ")
# digits = {
#     "1" : "one",
#     "2" : "two",
#     "3" : "three",
#     "4" : "four"
#     }
# output = ""
# for character in phone:
#     output += digits.get(character,  "!") + " "
# print(output)

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😃",
#     ":(": "🙁"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
