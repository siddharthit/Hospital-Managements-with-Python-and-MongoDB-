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
t5=f.getvalue("t5")
t6=f.getvalue("t6")

btn=f.getvalue("b1")
try:
    if(btn=="Save"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hospital']
     collection=db['Staff']
#primary key:-
     k=0
     for x in collection.find({}):
        if(x['Stf_id']==t1):
                k=1
                break
     if(k==1):
      print("<script>alert('Error id .....')</script>")
     else:
        insert1={'Stf_id':t1,'Stf_nm':t2,'Dgnt':t3,'Con_no':t4,'@mail':t5,'Hos_id':t6}
        collection.insert_one(insert1)
        print("<script>alert('Data_Saved.....')</script>")
#Update Button:-
    if(btn=="Update"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hospital']
     collection=db['Staff']
     collection.update_one({'Stf_id':t1},{'$set':{'Stf_nm':t2,'Dgnt':t3,'Con_no':t4,'@mail':t5,'Hos_id':t6}})
     print("<script>alert('Record Update sir  .....')</script>")
#Delete Button
    if(btn=="Delete"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Staff']
        s={'Stf_id':t1}
        collection.delete_many(s)
        print("<script>alert('Record Deleted.....')</script>")
#AllSearch Button:
    if(f.getvalue("b1")=="Allsearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Staff']
        print("<center><table border=15 cellpadding=5 <tr> <th>Stf_id</th> <th> Stf_id</th> <th>Dgnt</th> <th>Con_no</th>  <th>@mail</th> <th>Hos_id</th> ")
        for x in collection.find({}):
            print("<tr><th>",x["Stf_id"],"</th>","<th>",x["Stf_nm"],"</th>","<th>",x["Dgnt"],"</th>","<th>",x["Con_no"],"</th>","<th>",x["@mail"],"</th>","<th>",x["Hos_id"],"</th>","</th></tr>") 
            print("<body><input  type=button value='Report' onclick=window.print()></body>")
#particular Search Button:
    if(f.getvalue("b1")=="Psearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Staff']
        print("<center><table border=15 cellpadding=5  <tr> <th>Stf_id</th> <th> Stf_id</th ><th>Dgnt</th> <th>Con_no</th>  <th>@mail</th> <th>Hos_id</th> ")
        for x in collection.find({'Stf_id':t1}):
            print("<tr><th>",x["Stf_id"],"</th>","<th>",x["Stf_nm"],"</th>","<th>",x["Dgnt"],"</th>","<th>",x["Con_no"],"</th>","<th>",x["@mail"],"</th>","<th>",x["Hos_id"],"</th>","</th></tr>") 
except Exception:
    traceback.print_exc()
     