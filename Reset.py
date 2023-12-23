#! C:/Users/91810/AppData/Local/Programs/Python/Python311/python
print("Content-Type:text/html")
print()
import cgi 
import traceback
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=int(f.getvalue("t2"))
btn=f.getvalue("b1")
try:
    if(btn=="Set"):
         client=pymongo.MongoClient("mongodb://localhost:27017/")
         db=client['Hospital']
         collection=db['Admin']
         collection.update_many({'Username':t1},{'$set':{'Count':t2}})
         print("<script>alert('Record updated...?')</script>")
         print("<script>window.open('index.html')</script>")
            
except Exception:
        traceback.print_exc()