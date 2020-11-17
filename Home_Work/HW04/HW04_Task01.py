import sys

lession_name, work_hours, salary_per_hour, award = sys.argv

total_salary = (
    (float(work_hours) * float(salary_per_hour)) + float(award)
)

print(total_salary)