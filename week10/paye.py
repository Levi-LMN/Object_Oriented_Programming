##1. Safaricom Company Ltd uses the following PAYE (Pay As You Earn) percentage
#tax rates for all its employees’ salary categories
 #Gross Salary (Kshs.) PAYE rate (%)
#50,001 and above 14
#40,000 – 49,999 12
#35,000 – 39,999 11
#25,000 – 34,999 8
#16,000 – 24,999 5
#9,500 – 15,999 3
#Below 9500 0

#The following standard deductions apply to all employees
 #N.S.S.F = Ksh. 80.00
 #N.H.I.F = Ksh. 200.00
 #Service charge = Ksh. 100.00
#The overtime rate is Kshs. 300 per hour for the first 50 hours an employee has
#worked overtime. Any extra overtime hour is paid at Kshs. 350
#At the end of the month, the payroll clerk runs a payroll through which he enters
#each employee’s basic salary into the computer and overtime hours worked as
#recorded in a claim form filled by the employee.
#The computer in turn adds up the basic salary and the overtime pay (if any) to
#get the gross pay. The computer then determines the PAYE amount payable from
#the gross pay.
#Finally, the employee’s net pay is calculated using the formula:
#Net Pay = Gross pay – [PAYE + (N.S.S.F + N.H.I.F + Service charge)]
#Required:
#Write a python program that performs the above-mentioned payroll activities for
#a single employee and outputs Gross Pay, PAYE Amount and Net Pay on the
#screen


def calculate_paye(gross_salary):
    if gross_salary >= 50001:
        paye = gross_salary * 0.14
    elif gross_salary >= 40000:
        paye = gross_salary * 0.12
    elif gross_salary >= 35000:
        paye = gross_salary * 0.11
    elif gross_salary >= 25000:
        paye = gross_salary * 0.08
    elif gross_salary >= 16000:
        paye = gross_salary * 0.05
    elif gross_salary >= 9500:
        paye = gross_salary * 0.03
    else:
        paye = 0
    return paye


def calculate_net_pay(gross_salary):
    paye = calculate_paye(gross_salary)
    nssf = 80
    nhif = 200
    service_charge = 100
    net_pay = gross_salary - (paye + (nssf + nhif + service_charge))
    return net_pay


def calculate_overtime_pay(overtime_hours):
    if overtime_hours <= 50:
        overtime_pay = overtime_hours * 300
    else:
        overtime_pay = (50 * 300) + ((overtime_hours - 50) * 350)
    return overtime_pay


def calculate_gross_pay(basic_salary, overtime_hours):
    gross_pay = basic_salary + calculate_overtime_pay(overtime_hours)
    return gross_pay


def main():
    basic_salary = float(input("Enter basic salary: "))
    overtime_hours = float(input("Enter overtime hours: "))
    gross_pay = calculate_gross_pay(basic_salary, overtime_hours)
    paye = calculate_paye(gross_pay)
    net_pay = calculate_net_pay(gross_pay)
    print(f"Gross Pay: {gross_pay}")
    print(f"PAYE: {paye}")
    print(f"Net Pay: {net_pay}")

main()




