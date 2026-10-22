Code
SIZE = 10
table = [None] * SIZE
def hash_function(key):
    return key % SIZE
def insert(key):
    index = hash_function(key)
    for i in range(SIZE):
        pos = (index + i) % SIZE
        if table[pos] is None:
            table[pos] = key
            print("Key inserted.")
            return
    print("Hash table is full.")
def search(key):
    index = hash_function(key)
    for i in range(SIZE):
        pos = (index + i) % SIZE
        if table[pos] == key:
            print("Key found at index", pos)
            return
        if table[pos] is None:
            break
    print("Key not found.")
def delete(key):
    index = hash_function(key)
    for i in range(SIZE):
        pos = (index + i) % SIZE
        if table[pos] == key:
            table[pos] = None
            print("Key deleted.")
            return
        if table[pos] is None:
            break
    print("Key not found.")
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", table[i])
while True:
    print("\n--- HASH TABLE ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        key = int(input("Enter key: "))
        insert(key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice.")
Output--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 1
Enter key: 15
Key inserted.--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 1
Enter key: 25
Key inserted.--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 1
Enter key: 35
Key inserted.--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 1
Enter key: 7
Key inserted.--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 4
Hash Table:
0 : None
1 : None
2 : None
3 : None
4 : None
5 : 15
6 : 25
7 : 35
8 : 7
9 : None--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 2
Enter key to search: 35
Key found at index 7--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 2
Enter key to search: 99
Key not found.--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 3
Enter key to delete: 25
Key deleted.--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 4
Hash Table:
0 : None
1 : None
2 : None
3 : None
4 : None
5 : 15
6 : None
7 : 35
8 : 7
9 : None--- HASH TABLE --
1. Insert
2. Search
3. Delete
4. Display
5. Exit
Enter choice: 5
Program terminated
