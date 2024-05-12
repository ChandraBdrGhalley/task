from queue import Queue

# Initialize the queue to store patient names
patient_queue = Queue()

while True:
    print("\nDesk Manager - Patient Registration and Appointment System")
    print("1. Register Patient")
    print("2. Remove Patient After Meeting Doctor")
    print("3. Display Registered Patient Queue")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Register Patient
        patient_name = input("Enter patient name: ")
        patient_queue.put(patient_name)
        print("Patient", patient_name, "registered.")

    elif choice == '2':
        # Remove Patient After Meeting Doctor
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            next_patient = patient_queue.get()
            print("Patient", next_patient, "removed after meeting the doctor.")

    elif choice == '3':
        # Display Registered Patient Queue
        if patient_queue.empty():
            print("No patients in the queue.")
        else:
            print("Current patient queue:")
            for index, patient in enumerate(list(patient_queue.queue), start=1):
                print(index, ".", patient)

    elif choice == '4':
        # Exit
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")

    #get - will remove 
    # put - will add1