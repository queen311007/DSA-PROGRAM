# Event Processing System using Queue
from collections import deque
queue = deque()
while True:
    print("\n--- Event Processing System ---")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    # Add Event
    if choice == 1:
        event = input("Enter event: ")
        queue.append(event)
        print("Event added:", event)
    # Process Next Event
    elif choice == 2:
        if queue:
            event = queue.popleft()
            print("Event processed:", event)
        else:
            print("Queue is empty.")
    # Display Pending Events
    elif choice == 3:
        if queue:
            print("Pending Events:", list(queue))
        else:
            print("No pending events.")
    # Cancel Event
    elif choice == 4:
        event = input("Enter event to cancel: ")
        if event in queue:
            queue.remove(event)
            print("Event cancelled:", event)
        else:
            print("Event not found.")
    # Exit
    elif choice == 5:
        break
    else:
        print("Invalid choice!")--------------------------------------------------------
Output:--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 1
Enter event: Login User
Event added: Login User--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 1
Enter event: Update Database
Event added: Update Database--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 1
Enter event: Send Email
Event added: Send Email--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 3
Pending Events: ['Login User', 'Update Database', 'Send Email']--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 2
Event processed: Login User--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 3
Pending Events: ['Update Database', 'Send Email']--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 4
Enter event to cancel: Send Email
Event cancelled: Send Email--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 3
Pending Events: ['Update Database']--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 2
Event processed: Update Database--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 3
No pending events.--- Event Processing System --
1. Add Event
2. Process Next Event
3. Display Pending Events
4. Cancel Event
5. Exit
Enter your choice: 5
