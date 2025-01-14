#Insert items to the array, notifying the user if the inserted value is "" or not a number. User can choose to quit Inserting numbers
def InsertNumbers():
    list_of_numbers = []
    iterator = 0

    while True:
        print(f"You are currently adding number {iterator + 1}")
        print("To exit type: 'q'")
        number = input("Insert number: ")

        if number.strip() == "":
            print("Input cannot be empty. Please enter a number.")
            continue
        if number.lower() == "q":
            break

        try:
            number = float(number)
            list_of_numbers.append(number)
            iterator += 1

        except ValueError:
            print("Please insert a proper number.")
            continue

    print(f"You've added {iterator} items")
    print(list_of_numbers)

    return list_of_numbers

#Dont sort if the length of the array <= 1. Else divide array into 3 new arrays by using List Comprehensions
def QuickSort(numbers):
    length = len(numbers)
    if length <= 1:
        return numbers
    
    pivot = numbers[length // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]

    return QuickSort(left) + middle + QuickSort(right)

def main():
    list_of_numbers = InsertNumbers()
    if list_of_numbers:
        sorted_numbers = QuickSort(list_of_numbers)
        print(f"Sorted array:  {sorted_numbers}")
    else:
        print("Theres nothing to sort.")


main()
