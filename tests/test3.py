data = {'name': 'John', 'age': 28, 'country': 'India'}
del data['country']  # Remove specific key, give keyError if key not exist

# Pop() remove specific, and return its value
# default (optional): A fallback value if the key doesn’t exist.
# If not provided and the key is missing, Python raises a KeyError.
removed1 = data.pop('age')
print(f"Removed 'age': {removed1}, Now dictionary content is: {data}") 

try:
    removed2 = data.pop('height')
    print(f"Removed 'height': {removed2}, Now dictionary content is: {data}")
except KeyError:
    print(f"KeyError: 'height' not found")

removed3 = data.pop('city',"NA")
print(f"Removed 'city': {removed3}, Now dictionary content is: {data}")

# Popitem() remove and return last inserted key-value as tuple, give keyError if empty
last = data.popitem()  # Pop last item
print(f"Last popped item: {last}, Now dictionary content is: {data}")
                          
data.clear()  # Clear all
print(f"After clear(): {data}")