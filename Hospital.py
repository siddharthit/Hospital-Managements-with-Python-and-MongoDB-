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
t7=f.getvalue("t7")
btn=f.getvalue("b1")
try:
    if(btn=="Save"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hosptital']
     collection=db['hospital']
     #primary key:-
     k=0
     for x in collection.find({}):
        if(x['Hos_id']==t1):
                k=1
                break
     if(k==1):
      print("<script>alert('Error id .....')</script>")
     else:
        insert1={'Hos_id':t1,'Hos_nm':t2,'Con_no':t3,'@mail':t4,'Contact_pre':t5,'Reg':t6}
        collection.insert_one(insert1)
        print("<script>alert('Data_Saved.....')</script>")
    #Update Button:-
    if(btn=="Update"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hosptital']
     collection=db['hospital']
     collection.update_one({'Hos_id':t1},{'$set':{'Hos_nm':t2,'Con_no':t3,'@mail':t4,'Contact_pre':t5,'Reg':t6}})
     print("<script>alert('Record Update sir  .....')</script>")
#Delete Button
    if(btn=="Delete"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hosptital']
        collection=db['hospital']
        s={'Hos_id':t1}
        collection.delete_many(s)
        print("<script>alert('Record Deleted.....')</script>")
#AllSearch Button:
    if(f.getvalue("b1")=="Allsearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hosptital']
        collection=db['hospital']
        print("<center><table border=15 cellpadding=5 <tr><th>Hos_id</th> <th> Hos_nm </th> <th>Con_no</th> <th>@mail</th>  <th>Contact_pre</th> <th>Reg</th> ")
        for x in collection.find({}):
            print("<tr><th>",x["Hos_id"],"</th>","<th>",x["Hos_nm"],"</th>","<th>",x["Con_no"],"</th>","<th>",x["@mail"],"</th>","<th>",x["Contact_pre"],"</th>","<th>",x["Reg"],"</th></tr>") 
            print("<body><input  type=button value='Report' onclick=window.print()></body>")
#particular Search Button:
    if(f.getvalue("b1")=="Psearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hosptital']
        collection=db['hospital']
        print("<center><table border=15 cellpadding=5  <tr><th>Hos_id</th> <th> Hos_nm </th> <th>Con_no</th> <th>@mail</th>  <th>Contact_pre</th> <th>Reg</th> ")
        for x in collection.find({'Hos_id':t1}):
            print("<tr><th>",x["Hos_id"],"</th>","<th>",x["Hos_nm"],"</th>","<th>",x["Con_no"],"</th>","<th>",x["@mail"],"</th>","<th>",x["Contact_pre"],"</th>","<th>",x["Reg"],"</th></tr>") 
except Exception:
    traceback.print_exc()