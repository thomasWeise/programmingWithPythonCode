"""An example for dictionaries."""

num_str: dict[int, str] = {  # create and type hint a dictionary
    1: "one", 2: "two", 3: "three", 4: "four"}  # the elements
print(f"num_str = {num_str}")  # print the dictionary
print(f"I got {num_str[2]} shows and {num_str[1]} hat.") # get element

print(f"the keys are: {list(num_str.keys())}")  # print the keys
print(f"the values are: {list(num_str.values())}")  # print the values
print(f"the items are: {list(num_str.items())}")  # the key-value pairs

num_str[5] = "fivv"  # insert (or update) the value of a key
print(f"after adding key 1 num_str is now {num_str}")
num_str[5] = "five"  # update the value of a key
print(f"after updating key 1 num_str is now {num_str}")

del num_str[4]  # delete a key
print(f"after deleting key 4 num_str is now {num_str}")
# get the value of a key, then delete it
print(f"popping key 5 gets us {num_str.pop(5)}")

str_num: dict[str, int] = {}  # create empty dictionary
str_num.update({"one": 1, "two": 2, "three": 3, "four": 4})
print(f"{num_str[1]} + {num_str[2]} = {str_num['three']}")
