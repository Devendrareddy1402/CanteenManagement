import pymysql 
import pymysql.cursors
from tabulate import tabulate

givenhost = input("Host: ")
givenuser = input("User: ")
givenport = int(input("Port: "))
givenpassword = input("Password: ")



try:
    base = pymysql.connect(host =givenhost, user = givenuser, port = givenport, password = givenpassword, db = "CANTEEN", cursorclass = pymysql.cursors.DictCursor)
    
    if(base.open):
        print("Connected")
    else:
        print("Connection Failed")
    
    
except Exception as exp:
    print("Failed")
    print(">>>>", exp)




cur = base.cursor()
    
query = "SELECT * FROM Customers WHERE ID = %s "
data = (108)
cur.execute(query,data)

rows = cur.fetchall()


print(list(rows[0].keys()))
a = []
a.append(list(rows[0].keys()))


for row in rows:
    b = []
    for k in row.keys():
        b.append(row[k])
    a.append(b)
    
print(tabulate(a, tablefmt = "psql"))