
print("Work of Rybchynchuk Vladyslav AP-31")
print("Lab 6")

from scipy.optimize import linear_sum_assignment 
 
# Матриця вартостей для задачі про призначення 
A = [ 
    [5, 6], 
    [2, 3], 
    [4, 7]  
] 
 
# Визначення імен програмістів та програм 
workers = ["l1", "l2", "l3"] 
works = ["Robota 1", "Robota 2"] 
 
# Вирішення задачі про призначення 
row_ind, col_ind = linear_sum_assignment(A) 
 
# Виведення матриці з написами 
print("   " + "   ".join(works)) 
for i in range(len(A)): 
    print(f"{workers[i]}  {A[i]}") 
 
# Виведення результатів та обчислення мінімального значення цільової функції 
min_time = 0 
print("\nОптимальне призначення:") 
for i in range(len(row_ind)): 
    worker_index = row_ind[i] 
    work_index = col_ind[i] 
    time = A[worker_index][work_index] 
    min_time += time 
    print(f"{workers[worker_index]} -> {works[work_index]} (вартість: {time})") 
 
print(f"\nМінімальний час виконання двох робіт: {min_time}")
