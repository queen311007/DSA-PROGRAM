# Undo/Redo System using Stacks
undo = []
redo = []
document = ""
while True:
    print("\n1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        undo.append(document)
        document = input("Enter new text: ")
        redo.clear()
    elif choice == 2:
        if undo:
            redo.append(document)
            document = undo.pop()
        else:
            print("Nothing to undo")
    elif choice == 3:
        if redo:
            undo.append(document)
            document = redo.pop()
        else:
            print("Nothing to redo")
    elif choice == 4:
        print("Document:", document)
    elif choice == 5:
        break
    else:
        print("Invalid choice")--------------------------------------------------------
Output:
1. Make Change
2. Undo
3. Redo
4. Display
5. Exit
Enter choice: 1
Enter new text: Hello
1. Make Change
2. Undo
3. Redo
4. Display
5. Exit
Enter choice: 1
Enter new text: Hello World
1. Make Change
2. Undo
3. Redo
4. Display
5. Exit
Enter choice: 4
Document: Hello World
1. Make Change
2. Undo
3. Redo
4. Display
5. Exit
Enter choice: 2
1. Make Change
2. Undo
3. Redo
4. Display
5. Exit
Enter choice: 4
Document: Hello
1. Make Change
2. Undo
3. Redo
4. Display
5. Exit
Enter choice: 3
1. Make Change
2. Undo
3. Redo
4. Display
5. Exit
Enter choice: 4
Document: Hello World
1. Make Change
2. Undo
3. Redo
4. Display
5. Exit
Enter choice: 5
