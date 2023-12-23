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
btn=f.getvalue("b1")
try:
    if(btn=="Login"):
         client=pymongo.MongoClient("mongodb://localhost:27017/")
         db=client['Hospital']
         collection=db['Admin']
#primary key 
         k=0
    for x in collection.find({}):
        if(x["Username"]==t1):
            if(x["Password"]==t2):
                k=1
                break
    if(k==1):
        print("<script>window.open('Menu.html','_self')</script>")
    for x in collection.find({}):
        if(x["Username"]==t1 and x["Password"]==t2):
            collection.update_many({"Username":t1},{'$set':{'Count':x["Count"]-1}})
            print("<script>alert('Invalid Username! Please try again.')</script>")
    else:
            print("<script>alert('Invalid Id And Password! Please try again.')</script>")  
except Exception:
        traceback.print_exc()