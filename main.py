import task01, task02

print("--- TASK 01 ---")
total, average = task01.total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
print("\n")
print("--- TASK 02 ---")
cats_info = task02.get_cats_info("cats_info.csv")
print(cats_info)
