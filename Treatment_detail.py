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
     collection=db['Treatment_detail']
     insert1={'Tre_id':t1,'med_id':t2,'Qua':t3,'dos_des':t4}
     collection.insert_one(insert1)
     print("<script>alert('Data_Saved.....')</script>")
#Update Button:-
    if(btn=="Update"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hospital']
     collection=db['Treatment_detail']
     collection.update_one({'Tre_id':t1},{'$set':{'med_id':t2,'Qua':t3,'dos_des':t4}})
     print("<script>alert('Record Update sir  .....')</script>")
#Delete Button
    if(btn=="Delete"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Treatment_detail']
        s={'Tre_id':t1}
        collection.delete_many(s)
        print("<script>alert('Record Deleted.....')</script>")
#AllSearch Button:
    if(f.getvalue("b1")=="Allsearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Treatment_detail']
        print("<center><table border=15 cellpadding=5 <tr><th>Ser_id</th><th> Ser_nm</th> <th>Qua</th> <th> dos_des</th></tr>")
        for x in collection.find({}):
            print("<tr><th>",x["Tre_id"],"</th>","<th>",x["med_id"],"</th>","<th>",x["Qua"],"</th>","<th>",x["dos_des"],"</th>","</th></tr>")
            print("<body><input  type=button value='Report' onclick=window.print()></body>")
#particular Search Button:
    if(f.getvalue("b1")=="Psearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Treatment_detail']
        print("<center><table border=15 cellpadding=5 <tr><th>Ser_id</th><th> Ser_nm</th> <th>Qua</th> <th> dos_des</th></tr>")
        for x in collection.find({'Tre_id':t1}):
            print("<tr>","<th>",x["Tre_id"],"</th>","<th>",x["med_id"],"</th>","<th>",x["Qua"],"</th>","<th>",x["dos_des"],"</th>","</tr>") 
     
except Exception:
        traceback.print_exc()