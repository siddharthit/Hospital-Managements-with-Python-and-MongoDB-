#! C:\Users\91810\AppData\Local\Programs\Python\Python311\python
print("Content-Type:text/html")
print()
import cgi
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
t3=f.getvalue("t3")

btn=f.getvalue("b1")
try:
    if(btn=="Save"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hospital']
     collection=db['Treatment']
#primary key:-
     k=0
     for x in collection.find({}):
        if(x['treat_id']==t1):
                k=1
                break
     if(k==1):
      print("<script>alert('Error id .....')</script>")
     else:
        insert1={'treat_id':t1,'app_id':t2,'remark':t3}
        collection.insert_one(insert1)
        print("<script>alert('Data_Saved.....')</script>")
#Update Button:-
    if(btn=="Update"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hospital']
     collection=db['Treatment']
     collection.update_one({'treat_id':t1},{'$set':{'app_id':t2,'remark':t3}})
     print("<script>alert('Record Update sir  .....')</script>")
#Delete Button
    if(btn=="Delete"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Treatment']
        s={'treat_id':t1}
        collection.delete_many(s)
        print("<script>alert('Record Deleted.....')</script>")
#AllSearch Button:
    if(f.getvalue("b1")=="Allsearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Treatment']
        print("<center><table border=15 cellpadding=5 <tr><th>treat_id</th><th> App_id</th><th>remark</th></tr>")
        for x in collection.find({}):
            print("<tr><th>",x["treat_id"],"</th>", "<th>",x["app_id"],"</th>","<th>",x["remark"],"</th></tr>")
            print("<body><input  type=button value='Report' onclick=window.print()></body>")
#particular Search Button:
    if(f.getvalue("b1")=="Psearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Treatment']
        print("<center><table border=15 cellpadding=5 <tr> <th>treat_id</th> <th> App_id</th> <th>remark</th> </tr>")
        for x in collection.find({'treat_id':t1}):
            print("<tr><th>",x["treat_id"],"</th>","<th>",x["app_id"],"</th>","<th>",x["remark"],"</th></tr>") 
     
except Exception:
    traceback.print_exc()