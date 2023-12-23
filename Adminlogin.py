#! C:/Users/91810/AppData/Local/Programs/Python/Python311/python
print("Content-Type:text/html")
print()
import cgi 
import traceback
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")

b1=f.getvalue("b1")
try:
    if(b1=="Confirm"):
         client=pymongo.MongoClient("mongodb://localhost:27017/")
         db=client['Hospital']
         collection=db['Adminlogin']
         a=0
         b=0
         for x in collection.find({}):
            if(x["Login_id"]==t1):
                if(x["Login_id"]=="admin"):
                    a=1
                elif(x["Login_id"]=="admin1" and t2=="admin1"):
                    a=2
                    b=2
                    break
                if(x["password"]==t2):
                    b=1
         if(a==0):
            print("<script>alert('Invalid Admin Id ')</script>")
         elif(b==0):
            print("<script>alert('Incorrect Admin_password')</script>")
         elif(a==1 and b==1):
            print("<script>window.open('registration.html','_self')</script>")
         elif(a==2 and b==2):
            print("<script>window.open('Reset.html','_self')</script>")
                    
                    
except Exception:
    traceback.print_exc() 