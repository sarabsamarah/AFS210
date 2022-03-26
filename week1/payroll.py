class Employee:
    def __init__(self, first=None, last=None, id=None, pay=0.00):
        self.firstName = first
        self.lastName = last
        self.employeeId = id 
        self.hourlyPay = pay

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getId(self):
        return self.employeeId

    def getHourlyPay(self):
        return self.hourlyPay

    def setHourlyPay(self, pay):
        self.hourlyPay

    def pay(self, hoursWorked):
        if hoursWorked <=40:
            return self.hourlyPay * hoursWorked
        else:
            weeklyPay = self.hourlyPay * 40
            weeklyPay += (self.hourlyPay * 1.5) * (hoursWorked - 40)
            return weeklyPay

id = int(input("Please enter your employee ID: "))
firstName = input("Please enter the employee's first name: ")
lastName = input("Please enter the employee's last name: ")
pay = float(input("Please enter the employee'a hourly pay rate: "))
newEmployee = Employee(firstName, lastName, id, pay)
hours = float(input("How many hours did " +newEmployee.getFirstName()+ " work this week?"))
print("{0} {1}' s paycheck amount is {2:2f}".format(newEmployee.getFirsName(),newEmployee.getLastName(),newEmployee.pay(hours)))



    




