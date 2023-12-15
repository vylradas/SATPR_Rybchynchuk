import pandas as pd
import numpy as np
from prettytable import PrettyTable

# Функція для побудови дерева рішень та обчислення таблиці
def build_decision_tree(purchases, probabilities, demands):
    table = PrettyTable()
    table.field_names = [
        'Попит', 'Ймовірність', 'Закупка', 'Спрос', 'Продано',
        'Не продано', 'Незадовіл. попит', 'Очікуваний дохід1',
        'Очікуваний дохід2', 'Кінцевий дохід'
    ]

    for purchase in purchases:
        for probability in probabilities:
            for demand in demands:
                if demand >= purchase:
                    sold = purchase
                    not_sold = purchase - sold
                    unsatisfied_demand = 0
                else:
                    sold = demand
                    not_sold = purchase - sold
                    unsatisfied_demand = sold - demand

                expected_income_1 = probability * sold * (2400 - 1500)
                expected_income_2 = sold * (2400 - 1500)
                final_income = expected_income_2 - 1500 * not_sold

                table.add_row([
                    purchase, probability, purchase, demand, sold,
                    not_sold, unsatisfied_demand, expected_income_1,
                    expected_income_2, final_income
                ])

    return table