#Insert items to the array, notifying the user if the inserted value is "" or not a number. User can choose to quit Inserting numbers.
def InsertNumbers():
    list_of_numbers = []
    iterator = 0

    while 1:
        try:
            print(f"You are currently adding number {iterator+1}")
            print("To exit type: 'q'")

            number = input("Insert number: ")

            if number.strip() == "":
                print("Input cannot be empty. Please enter a number.")
                continue
            elif number == "q":
                break
            iterator += 1
            float(number)
            list_of_numbers.append(number)

        except ValueError:
            print("Please insert proper number.")
            iterator -= 1
            continue

    print(f"You've added {iterator} items")
    print(list_of_numbers)

    return iterator, list_of_numbers

def QuickSort(numbers):   
    while True: 
    

def main():
    