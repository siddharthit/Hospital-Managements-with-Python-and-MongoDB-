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
t4=f.getvalue("t4")
btn=f.getvalue("b1")
try:
    if(btn=="Save"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hospital']
     collection=db['Service']
#primary key:-
     k=0
     for x in collection.find({}):
        if(x['ser_id']==t1):
                k=1
                break
     if(k==1):
      print("<script>alert('Error id .....')</script>")
     else:
        insert1={'ser_id':t1,'ser_nm':t2,'fee':t3,'hos_id':t4}
        collection.insert_one(insert1)
        print("<script>alert('Data_Saved.....')</script>")
#Update Button:-
    if(btn=="Update"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hospital']
     collection=db['Service']
     collection.update_one({'ser_id':t1},{'$set':{'ser_nm':t2,'fee':t3,'hos_id':t4}})
     print("<script>alert('Record Update sir  .....')</script>")
#Delete Button
    if(btn=="Delete"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Service']
        s={'Ser_id':t1}
        collection.delete_many(s)
        print("<script>alert('Record Deleted.....')</script>")
#AllSearch Button:
    if(f.getvalue("b1")=="Allsearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Service']
        print("<center><table border=15 cellpadding=5 <tr><th>Ser_id</th><th> Ser_nm</th> <th>fee</th> <th> hos_id</th></tr>")
        for x in collection.find({}):
            print("<tr><th>",x["ser_id"],"</th>","<th>",x["ser_nm"],"</th>","<th>",x["fee"],"</th>","<th>",x["hos_id"],"</th>","</th></tr>")
            print("<body><input  type=button value='Report' onclick=window.print()></body>")
#particular Search Button:
    if(f.getvalue("b1")=="Psearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Service']
        print("<center><table border=15 cellpadding=5 <tr><th>Ser_id</th><th> Ser_nm</th> <th>fee</th> </th><th> hos_id</th></tr>")
        for x in collection.find({'ser_id':t1}):
            print("<tr><th>",x["ser_id"],"</th>","<th>",x["ser_nm"],"</th>","<th>",x["fee"],"</th>","<th>",x["hos_id"],"</th>","</th></tr>") 
     
except Exception:
        traceback.print_exc()