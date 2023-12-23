#! C:/Users/91810/AppData/Local/Programs/Python/Python311/python
import cgi
import pymongo
from pymongo import MongoClient
import traceback
print("Content-Type:text/html")
print()
f = cgi.FieldStorage()
t1 = f.getvalue("t1")
t2 = f.getvalue("t2")
t3 = f.getvalue("t3")
t4 = f.getvalue("t4")
b1 = f.getvalue("b1")
try:
    if (b1 == "SignUp"):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client['Hospital']
        collection = db['Admin']
        a = 0
        for x in collection.find({}):
            if (x["Username"] == t1):
                a = 1
                break
        if (a == 1):
            print("<script>alert('Username already taken')</script>")
        elif (t2 != t3):
            print("<script>alert('Passwords do not match')</script>")
        elif (a == 0 and t2 == t3):
            insert1={'Username':t1,'Password':t2,'count':t4}
            collection.insert_one(insert1)
            print("<script>alert('User Created...!!')</script>")
            print("<script>window.open('index.html','self')</script>")

except Exception:
    traceback.print_exc()
