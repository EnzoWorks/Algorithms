import pandas as pd

#Fragment testowy
"""data = {
    'Nazwa':[8, 1, 4],
    'Waga': [8, 1, 4],
    'Wartość': [120, 15, 4],
    'Dostępność': [1.0, 1.0, 1.0],
    'Wartość na kilogram': [15, 15, 1]
    }

df = pd.DataFrame(data)"""

data = {
    'Nazwa':[],
    'Waga': [],
    'Wartość': [],
    'Dostępność': [],
    'Wartość na kilogram': []
}

df = pd.DataFrame(data)

data_backpack = {
    'Nazwa':[],
    'Waga': [],
    'Wartość': [],
    'Wartość na kilogram': []
}

df_backpack = pd.DataFrame(data_backpack)

def Insert_items():
    try:    
        how_many = int(input(f"\nWprowadź ilość dostępnych przedmiotów: "))
        if how_many <= 0:
            print("Liczba dostępnych przedmiotów musi być większa od 0")
            return
    except ValueError:
        print("Liczba dostępnych przedmiotów musi być liczbą całkowitą dodatnią")
        return

    for _ in range(how_many):
        item_name = input(f"\nWprowadź nazwę przedmiotu: ")

        while True:
            try:
                weight = int(input(f"Wprowadź wagę przedmiotu: "))
                if weight <= 0:
                    print("Waga przedmiotu nie może być ujemna")
                    continue
                break
            except ValueError:
                print("Liczba przedmiotu musi być liczbą całkowitą dodatnią")

        while True:
            try:
                value = int(input(f"Wprowadź wartość przedmiotu: "))
                if value <= 0:
                    print("Wartość przedmiotu nie może być ujemna")
                    continue
                break
            except ValueError:
                print("Wartość przedmiotu musi być liczbą całkowitą dodatnią")

        while True:
            try:
                quantity = float(input(f"Wprowadź ilość przedmiotu: "))
                if quantity <= 0:
                    print("Ilość przedmiotu nie może być ujemna")
                    continue
                break
            except ValueError:
                print("Ilość przedmiotu musi być liczbą dodatnią")

        value_per_kg = round(value / weight, 2)

        df.loc[len(df)] = [item_name, weight, value, quantity, value_per_kg]

    print(df)

def Backpack():
    global df_backpack
    size = int(input("\nPodaj dostępne miejsce w plecaku: "))
    
    while size != 0 and not df.empty:

        expensive = df.nlargest(1, 'Wartość na kilogram')

        quantity_of = expensive['Dostępność'].values[0]
        product_weight = expensive['Waga'].values[0]

        if size >= product_weight and quantity_of > 0:
            df_backpack = pd.concat([df_backpack, expensive.drop(columns=["Dostępność"])], ignore_index=True)
            size -= product_weight
            
            df.loc[df['Nazwa'] == expensive['Nazwa'].values[0], 'Dostępność'] -= 1
            continue
            
        elif size != 0 and size < product_weight and quantity_of > 0:
            proportion = size / product_weight
            partial_value = round(expensive['Wartość'].values[0] * proportion, 2)
            partial_weight = size
            size = 0
            
            partial_item = pd.DataFrame({
                'Nazwa': [expensive['Nazwa'].values[0]],
                'Waga': [partial_weight],
                'Wartość': [partial_value],
                'Wartość na kilogram': [round(partial_value / partial_weight, 2)]
            })
            
            df_backpack = pd.concat([df_backpack, partial_item], ignore_index=True)
            

            df.loc[df['Nazwa'] == expensive['Nazwa'].values[0], 'Dostępność'] -= round(proportion, 2)
            break


        if df.loc[df['Nazwa'] == expensive['Nazwa'].values[0], 'Dostępność'].values[0] <= 0:
            df.drop(df[df['Nazwa'] == expensive['Nazwa'].values[0]].index, inplace=True) 

    def OverallValue():
        backpack_value = df_backpack['Wartość'].sum()
        print(f"\nWartość w plecaku: {backpack_value}\n")


    print(f"\nPrzedmioty w plecaku: \n{df_backpack}")
    OverallValue()
    print(f"Przedmioty na półce: \n{df}")


def Test():
    Backpack()

def main():
    Insert_items()
    Backpack()

main()