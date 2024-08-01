work_hours = input('Enter hours per day in entire week, separated by space: ').split()

print(work_hours)

total_hour = 0
for i in work_hours:
    total_hour += int(i)
print(total_hour)

wage = int(input('Enter hourly wage: '))
total_salary_per_week = total_hour * wage
print('Salary is: ',total_salary_per_week)