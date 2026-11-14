import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def show(label, response):
    """Print the method + URI and the labeled status code for any response."""
    print(f"Request     : {response.request.method} {response.url}")
    print(f"Status Code : {response.status_code}")


# CREATE
print("=" * 40)
print("1. CREATE")
new_todo = {
    "userId": 1,
    "title": "Complete Module 4",
    "completed": False,
}

create = requests.post(f"{BASE_URL}/todos", json=new_todo, timeout=10)
show("CREATE", create)
print(f"Result      : Created todo {create.json()}")

# Chain the ID from the POST response into every later URL
todo_id = create.json()["id"]
todo_url = f"{BASE_URL}/todos/{todo_id}"
print(f"Captured ID : {todo_id}")

# READ
print("=" * 40)
print("2. READ")
read = requests.get(todo_url, timeout=10)
show("READ", read)
if read.status_code == 200:
    print(f"Result      : {read.json()}")
else:
    print("Result      : Not found. JSONPlaceholder fakes creation, so the "
          "new todo was never actually stored.")

# UPDATE
print("=" * 40)
print("3. UPDATE")
update = requests.patch(todo_url, json={"completed": True}, timeout=10)
show("UPDATE", update)
if update.status_code == 200:
    print(f"Result      : {update.json()}")
else:
    print("Result      : Update failed. There is no stored todo to patch "
          "(same fake-creation reason).")

# READ AGAIN
print("=" * 40)
print("4. READ AGAIN")
read_again = requests.get(todo_url, timeout=10)
show("READ AGAIN", read_again)
if read_again.status_code == 200:
    print(f"Result      : completed = {read_again.json()['completed']}")
else:
    print("Result      : Still not found, so the update can't be verified.")

# DELETE
print("=" * 40)
print("5. DELETE")
delete = requests.delete(todo_url, timeout=10)
show("DELETE", delete)
print(f"Result      : Delete response body: {delete.json()}")

# VERIFY
print("=" * 40)
print("6. VERIFY")
verify = requests.get(todo_url, timeout=10)
show("VERIFY", verify)
if verify.status_code == 404:
    print("Result      : Confirmed: todo no longer exists.")
else:
    print(f"Result      : Unexpected status {verify.status_code}.")
print("=" * 40)
