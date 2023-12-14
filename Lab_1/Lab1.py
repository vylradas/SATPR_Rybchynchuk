f1 = open("Table 1.txt", "r")
f2 = open("Table 2.txt", "r")

print("Work of Rybchynchuk Vladyslav AP-31")
print("Lab 1")

#Завдання 1.
def first_table():
    print()
    print("Table #1")
    #Створюємо список елементів(від A1 до A4/від K1 до K4)
    Table1 = list()
    n = range(len(Table1))
    for l in f1:
        Table1.append([int(i) for i in l.split()])
    
    Result = list()
    for i in range(len(Table1)-1):
        sum = 0
            
        for j in range(len(Table1[0])):
            sum+=Table1[i][j]*Table1[len(Table1)-1][j]

        Result.append(sum)
         
    print("Sums of grades:",Result)
    print("Max: ", max(Result), "in A",Result.index(max(Result))+1)
    print()

#Завдання 2. 
def second_table():
    print()
    print("Table #2")
    #Створюємо список елементів(від A1 до A5/від K1 до K5)
    Table2 = list()

    for l in f2:
        Table2.append([float(i) for i in l.split()])

    for i in range(len(Table2[0])):
        tmpL = list()
        # j - рядок, i - столбік
        for j in range(len(Table2) - 2):
            tmpL.append(Table2[j][i])
        if Table2[len(Table2)-1][i]:
            for j in range(len(Table2) - 2):
                Table2[j][i]=(Table2[j][i]-min(tmpL))/(max(tmpL)-min(tmpL))
        else:
            for j in range(len(Table2) - 2):
                Table2[j][i]=(max(tmpL)-Table2[j][i])/(max(tmpL)-min(tmpL))
            
    Result = list()
    for i in range(len(Table2)-2):
        sum = 0
        
        for j in range(len(Table2[0])):
            sum+=Table2[i][j]*Table2[len(Table2)-2][j]
            Sum = round(sum, 3)
        
        Result.append(Sum)
        
    print("Sums of grades:", Result)
    print("Max: ", max(Result), "in A",Result.index(max(Result))+1)
    print()


menu = {
    1: first_table,
    2: second_table,
}

# Меню вибору та перегляду розв'язку завдання
def main():
    while True:
        print("List of tables")
        print("1. Table 1") #Перше завдання
        print("2. Table 2") #Друге завдання
        print("0. End the program")

        selection = int(input("Switch the table: "))

        if selection == 0:
            print("End The Program.")
            break  #Виходимо з циклу, якщо вибрано 0.
        
        #Виклик функції відповідно до вибору користувача
        selected_action = menu.get(selection)
        
        #Перевірка на коректне введення значення
        if selected_action:
            selected_action()
        else:
            print("Error. Try again.")

# Виклик функції
'''if __name__ == "__main__": '''
main()
