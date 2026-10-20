import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1/todos") 

#CREATE
#  
new_todo = {
  "userId": 1,
    "title": "Complete Module 4",
    "completed": "false"
}


todo = requests.post("https://jsonplaceholder.typicode.com/users/1/todos",
json= new_todo
)

print(f"Created Todo: {todo.json()}")
print("-"*40)
print(f"Status Code: {todo.status_code}")


# READ

todos = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"id": 200}
    ) 

reads = todos.json()
print("="*40)
print(f"Read: {reads}")
print("-"*40)
print(f"Status Code:{todos.status_code}")
print("="*40)

# UPDATE 

updated = {
    "completed": "true"
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/todos/200",
    json=updated
    )


updated_todo = response.json()
print(f"Update Todo: {updated_todo}")
print("-"*40)
print(f"Status Code:{response.status_code}")
print("="*40)

# READ AGAIN 

todos_again = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"id": 200}
    ) 

reads_again = todos_again.json()

print(f"New Read: {reads_again}")
print("-"*40)
print(f"Status Code:{todos_again.status_code}")
print("="*40)

# DELETE

todos_delete = requests.delete(
    "https://jsonplaceholder.typicode.com/todos/200"
    ) 

deleted_product = todos_delete.json()


print(f"Delete: {deleted_product}")
print("-"*40)
print(todos_delete.status_code)
print("="*40)

# VERIFY 

verify = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"id": 200}
    ) 

done = verify.json()

print(f"Verify: {done}")
print("-"*40)
print(f"Status Code:{todos.status_code}")
print("="*40)