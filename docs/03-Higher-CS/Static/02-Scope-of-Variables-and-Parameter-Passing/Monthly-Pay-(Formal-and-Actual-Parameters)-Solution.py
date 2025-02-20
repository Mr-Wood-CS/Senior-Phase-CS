def Employee_Info():
    employee_name = input("Enter employee's name:  ")
    pay = float(input("Enter employee's monthly pay:  "))
    bonus = float(raw_input("Enter employee's bonus this month:  "))

    return employee_name, pay, bonus
                  

# explain use of formal parameters...
def Add2Numbers(num1, num2):

    total = num1 + num2

    return total



def Output_Pay_Info(employee_name, total_pay):
    print
    print "Employee Name -", employee_name
    print "Pay for Month -", total_pay

    return


employee_name, pay, bonus = Employee_Info()

#explain use of actual parameters and what runs in procedure...
total_pay = Add2Numbers(pay, bonus)

Output_Pay_Info(employee_name, total_pay)
