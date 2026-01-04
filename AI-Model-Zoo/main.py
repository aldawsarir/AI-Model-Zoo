models = []


def addModel():
    print("\n[Add Model]")
    name = input("Model Name: ").strip()
    task = input("Task (Classification / Detection / NLP): ").strip()

    while True:
        try:
            accuracy = float(input("Accuracy (0 - 100): "))
            if 0 <= accuracy <= 100:
                break
            else:
                print("Accuracy must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    status = input("Status (Trained / Needs Training): ").strip()

    model = {
        "name": name,
        "task": task,
        "accuracy": accuracy,
        "status": status
    }
    models.append(model)
    print("Model added successfully.")


def removeModel():
    print("\n[Remove Model]")
    if not models:
        print("No models in the zoo yet.")
        return

    name = input("Enter model name to remove: ").strip()
    for i, m in enumerate(models):
        if m["name"].lower() == name.lower():
            removed = models.pop(i)
            print(f"Removed: {removed['name']}")
            return

    print("Model not found.")


def updateModelAccuracy():
    print("\n[Update Model]")
    if not models:
        print("No models in the zoo yet.")
        return

    name = input("Enter model name to update: ").strip()
    for m in models:
        if m["name"].lower() == name.lower():

            print("\nWhat do you want to update?")
            print("1) Task")
            print("2) Accuracy")
            print("3) Status")
            choice = input("Choose (1/2/3): ").strip()

            if choice == "1":
                new_task = input("New Task: ").strip()
                m["task"] = new_task
                print("Task updated.")

            elif choice == "2":
                while True:
                    try:
                        new_accuracy = float(input("New Accuracy (0 - 100): "))
                        if 0 <= new_accuracy <= 100:
                            m["accuracy"] = new_accuracy
                            print("Accuracy updated.")
                            break
                        else:
                            print("Accuracy must be between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid number.")

            elif choice == "3":
                new_status = input("New Status (Trained / Needs Training): ").strip()
                m["status"] = new_status
                print("Status updated.")

            else:
                print("Invalid choice.")
            return

    print("Model not found.")


def displayModels():
    print("\n[Display Models]")
    if not models:
        print("The zoo is empty. Add some models first.")
        return

    print("-" * 60)
    print(f"{'ID':<4} {'Model Name':<20} {'Task':<15} {'Acc%':<7} {'Status'}")
    print("-" * 60)

    for idx, m in enumerate(models, start=1):
        print(f"{idx:<4} {m['name']:<20} {m['task']:<15} {m['accuracy']:<7.2f} {m['status']}")

    print("-" * 60)


def exitSystem():
    print("\nExiting AI Model Zoo...")
    return True


while True:
    print("\n====== AI Model Zoo (Mini Version) ======")
    print("1) Add Model")
    print("2) Remove Model")
    print("3) Update Model (Task/Accuracy/Status)")
    print("4) Display Models")
    print("5) Exit")
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        addModel()
    elif choice == "2":
        removeModel()
    elif choice == "3":
        updateModelAccuracy()
    elif choice == "4":
        displayModels()
    elif choice == "5":
        if exitSystem():
            break
    else:
        print("Invalid choice. Please choose 1-5.")