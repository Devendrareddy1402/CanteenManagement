import pymysql
import pymysql.cursors
import subprocess
import re
import datetime
from datetime import timedelta
from tabulate import tabulate
regex = "^[a-z0-9]+[@][a-z]+[\.][a-z]{5}[\.][a-z]{2,3}[\.][a-z]{2,3}"




def viewtable(rows):
    try:
        a = []
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")
        return 
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    
    print(tabulate(a, tablefmt="psql", headers= "firstrow"))
    print()


#------------------  PHONE NUMBER -----------------------
def isValid(s):
    pattern = re.compile("(0/91)?[6-9]+[0-9]{9}")
    return pattern.match(s)



#-------------------- ADDING CUSTOMER -------------------
def addcustomer():
    try:
        newcus = {}
        newcus[0] = input("Name: ")
        newcus[1] = input("Gender: ")
        if(newcus[1] == 'M' or newcus[1] == 'G'):
            newcus[2] = int(input("ID: "))
            newcus[3] = input("Email: ")
            newcus[4] = input("Role: ")
            if(re.search(regex, newcus[3])):
                newcus[5]= int(input("Amount: "))
                newcus[6] = input("Phone Number: ")
                numbers = newcus[6].split(" ")
                query="INSERT INTO Customers VALUES(%s,%s,%s,%s,%s,%s)" 
                data = (newcus[0],newcus[1],newcus[2],newcus[3],newcus[4],newcus[5])
                cur.execute(query,data)
                base.commit()
                print(" Updated Customers Table ")
                for number in numbers:
                    if(isValid(number)):
                        phone_query = "INSERT INTO CustomerNumber VALUES(%s,%s,%s)" 
                        phone_data = (newcus[2], newcus[0], number)
                        cur.execute(phone_query, phone_data)
                        base.commit()
                        print(" Updated Customersnumber Table ")
                    else:
                        txt = "{num} is not a valid phone number"
                        print(txt.format(number))
            else:
                print("Email is not valid")
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)



#-------------------- ADD BILL ------------------------
def addbill():
    
    try:
        newbill = {}
        newbill[0] = int(input("Customer ID: "))
        newbill[1] = input("Name of the person: ")
        newbill[2] = int(input("StallID: "))
        newbill[3] = int(input("Amount: "))
        newbill[4] = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
       
        newbill[5] = f"{newbill[2]}-{newbill[4]}"
        
        print(newbill[5])
        query = "INSERT INTO Bill VALUES(%s, %s,%s,%s,%s,%s)" 
        data = (newbill[0], newbill[1], newbill[2], newbill[3], newbill[4], newbill[5])
        cur.execute(query,data)
        base.commit()
        
        update_query = "UPDATE Customers SET Amount = Amount + %s WHERE ID = %s"
        update_data =  (newbill[3], newbill[0])
        cur.execute(update_query, update_data)
        base.commit()
        
    
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)


#-------------- ADD DEPENDENT -----------------------
def adddependent():
    try:
        newdep = {};
        newdep[0] = int(input("Customer ID: "))
        newdep[1] = input("DependentName: ")
        newdep[2] = input("DependentGender: ")
        if(newdep[2] in ['M', 'G']):
            query = "INSERT INTO Dependents VALUES(%s, %s, %s)"
            data = (newdep[0], newdep[1], newdep[2])
            cur.execute(query, data);
            base.commit()
        else:
            print("Gender is not valid")
    
    except Exception as exp:
        base.rollback()
        print(">>>>", exp)
        


#-------------- ADD NEW STALL ------------------------------
def addstall():
    try:
        newstall = {}
        newstall[0] = input("Stall Name: ")
        newstall[1] = int(input("ID: "))
        newstall[2] = input("Opening Time: ")
        newstall[3] = input("Closing Time: ")
        start_time = datetime.datetime.strptime(newstall[2], "%H:%M:%S")
        end_time = datetime.datetime.strptime(newstall[3], "%H:%M:%S")
        
        if(end_time < start_time):
            end_time += timedelta(days = 1)
        duration = end_time - start_time
        
        query = "INSERT INTO Stall VALUES(%s, %s, %s, %s, %s)"
        data = (newstall[0], newstall[1], newstall[2], newstall[3], duration)
        
        cur.execute(query, data)
        base.commit()
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)
        
        
#------------ ADD NEW EMPLOYEE --------------------------
def addemployee():
    try:
        newemp = {}
        newemp[0] = input("Name: ")
        newemp[1] = input("Gender: ")
        
        if(newemp[1] in ['M', 'F']):
            newemp[2] = int(input("ID: "))
            newemp[3] = int(input("StallID: "))
            newemp[4] = input("Role: ")
            newemp[5] = int(input("Salary: "))
            newemp[6] = int(input("Workingdays: "))
            newemp[7] = int(input("Manager ID: "))
            
            query = "INSERT INTO Employee VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (newemp[0], newemp[1], newemp[2], newemp[3], newemp[4], newemp[5], newemp[6], newemp[7])
            
            cur.execute(query, data)
            base.commit()
        
        else:
            print("Gender is not valid")
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>",exp)




#-------------- HIKE EMPLOYEE ------------------------------------
def hikeemployee():
    try:
        id = int(input("Employee ID:  "))
        final = int(input("Final Salary: "))
        
        query = "UPDATE Employee SET Salary = %d WHERE ID = %d"  
        data = (final, id)
        
        cur.execute(query,data)
        base.commit()
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)        
        
        
        
#------------------- CUSTOMER DETAILS -------------------------------    
def customerdetails():
    try:
        customerid = int(input("Enter Customer ID: "))
        query = "SELECT * FROM Customers WHERE ID = %s"
        data = (customerid)
        cur.execute(query, data)
        detail = cur.fetchall()
        viewtable(detail)
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)
    
 
 
#----------------------- DELETE CUSTOMER ----------------------------   
def deleteCustomer():
    try:
        delc = {}
        delc[0] = int(input("Customer ID to be deleted: "))
        delphone = "DELETE FROM CustomerNumber WHERE CustomerID = %s"
        delphonedata = (delc[0])
        cur.execute(delphone, delphonedata)
        base.commit()
        query = "DELETE FROM Customers WHERE  ID= %s"
        data = (delc[0])
        cur.execute(query, data)
        base.commit()
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)



#---------------------------- DELETE EMPLOYEE --------------------------
def deleteEmployee():
    try:
        dele = {}
        dele[0] = int(input("Employee ID to be Deleted: "))    
        query = "DELETE FORM Employee WHERE ID = %s"
        data = (dele[0])
        cur.execute(query,data)
        base.commit()
        
    except Exception as exp:
        base.rollback()
        print("Failed ")
        print(">>>>", exp)




#-------------------- LIST ABOVE 500 -------------------------------------
def listabove500():
    try:
        query = "SELECT * FROM Customers WHERE Amount > 500"
        cur.execute(query)
        record = cur.fetchall()
        viewtable(record)
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)




#----------------------- CUSTOMER PAID -----------------------------------
def customerPaid():
    try:
        cusid= int(input("Customer ID: "))
        paid = int(input("Amount Paid: "))
        query = "UPDATE Customers SET Amount = Amount - %s WHERE ID = %s"
        data = (paid, cusid)
        cur.execute(query,data)
        base.commit()
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)
        
        
#--------------------------- TOTAL SPENT -------------------------------     
def totalspent():
    try:
        cusid = int(input("Customer ID: "))
        query = "SELECT SUM(Amount) FROM Customers WHERE ID = %s"
        data = (cusid)
        cur.execute(query,data)
        record = cur.fetchall()
        viewtable(record) 
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)


#-------------------------- DISPLAY CUSTOMERS ----------------------------
def displaycustomer():
    try:
        query = "SELECT * FROM Customers"
        cur.execute(query)
        customerrecords = cur.fetchall()
        viewtable(customerrecords)
        
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)


#---------------------------- DISPLAY STALLS ---------------------------------
def displaystalls():
    try:
        query = "SELECT * FROM Stall"
        cur.execute(query)
        stallsrecords = cur.fetchall()
        viewtable(stallsrecords)
        
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)



#--------------------------- DISPLAY BILLS ----------------------------------
def displaybills():
    try:
        query = "SELECT * FROM Bill"
        cur.execute(query)
        billrecords = cur.fetchall()
        viewtable(billrecords)
        
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)


#------------------------- DISPALY EMPLOYEES --------------------------------
def displayemployees():
    try:
        query = "SELECT * FROM Employee"
        cur.execute(query)
        employeerecords = cur.fetchall()
        viewtable(employeerecords)
        
        
    except Exception as exp:
        base.rollback()
        print("Failed")
        print(">>>>", exp)



def function(given):
    
    if(given == 1):
        addcustomer()
    elif(given == 2):
        addbill()
    elif(given == 3):
        adddependent()
    elif(given == 4):
        addstall()
    elif(given == 5):
        addemployee()
    elif(given == 6):
        hikeemployee()
    elif(given == 7):
        customerdetails()
    elif(given == 8):
        deleteCustomer()
    elif(given == 9):
        deleteEmployee()
    elif(given == 10):
        listabove500()
    elif(given == 11):
        customerPaid()
    elif(given == 12):
        totalspent()
    elif(given == 13):
        displaycustomer()
    elif(given == 14):
        displaystalls()
    elif(given == 15):
        displaybills()
    elif(given == 16):
        displayemployees()
    
    else:
        print("INVALID OPTION")
        
        
    
givenhost = input("Enter host: ")
givenuser = input("Enter user: ")
givenport = int(input("Enter port: "))
givenpassword = input("Enter password: ")
tmp = subprocess.call("clear", shell = True)
try:
    base = pymysql.connect(host = givenhost, user = givenuser , port = givenport, password = givenpassword
                           ,db = "CANTEEN", cursorclass = pymysql.cursors.DictCursor)
    tmp = subprocess.call("clear", shell= True)
    if(base.open):
        print("Connected")
    else:
        print("Connection failed")
    
    with base.cursor() as cur:
        while(1):
            print("Select 1 to add a new Customer ")
            print("Select 2 to add a new bill ")
            print("Select 3 to add a new dependent ")
            print("Select 4 to add a new stall ")
            print("Select 5 to add a new Employee ")
            print("Select 6 to give hike to an Employee ")
            print("Select 7 to list customer details ")
            print("Select 8 to delete a customer ")
            print("Select 9 to delete an employee ")
            print("Select 10 to list customers with Amount > 500")
            print("Select 11 if a customer paid some amount ")
            print("Select 12 for amount spent by a customer ")
            print("Select 13 to print all the customers ")
            print("Select 14 to print all the stalls ")
            print("Select 15 to print all the bills ")
            print("Select 16 to print all the employees ")
            print("Select 17 to exit ")
            received = int(input("Enter choice: "))
            
            if(received == 17):
                break
            
            else:
                function(received)
            
except Exception as exp:
    tmp = subprocess.call("clear", shell = True)
    print("Connection to the database is failed")
    print(">>>>> ", exp)
    
    