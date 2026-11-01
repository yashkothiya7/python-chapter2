# Create a program name “employee.py” and implement the functions DA, HRA, PF, and ITAX. Create another program that 
# uses the function of employee module and calculates gross and net salaries of an employee

import employee     
 
def calculate_gross_salary(basic_salary):
    DA = employee.calculate_DA(basic_salary)    
    HRA = employee.calculate_HRA(basic_salary)
    PF = employee.calculate_PF(basic_salary)
    
    gross_salary = basic_salary + DA + HRA - PF
    return gross_salary

def calculate_net_salary(gross_salary):
    ITAX = employee.calculate_ITAX(gross_salary)
    net_salary = gross_salary - ITAX
    return net_salary

basic_salary = float(input("Enter basic salary : "))

gross_salary = calculate_gross_salary(basic_salary)
net_salary = calculate_net_salary(gross_salary)

print("Gross salary is : ", gross_salary)
print("net salary is  : ",net_salary)

