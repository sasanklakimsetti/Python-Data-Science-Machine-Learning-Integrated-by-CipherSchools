# Dictionary : combination of key-value pairs just like Maps in CPP and Java
# Doesn't allow duplicate keys
person={"name":"John","age":30}  # variable before colon is called key. after colon is called value
print(person.keys()) # prints all keys of the dictionary
print(person.values()) # prints all values of the dictionary
print(person.items()) # print all key-value pairs
print(person.get("name"))  # get value by key
person.update({"height":180}) # update dictionary with another dictionary
print(person)
person.pop("age")  # removes the age key from the dictionary
print(person)
