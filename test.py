from requests import put, get
# put('http://127.0.0.1:5000/todo1', data={'data': 'Remember the milk'}).json()

y = get('http://127.0.0.1:5000/users').json()
print(y)

# put('http://127.0.0.1:5000/todo2', data={'data': 'Change my brakepads'}).json()

# x = get('http://127.0.0.1:5000/todo2').json()
# print(x)
