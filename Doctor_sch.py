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
     collection=db['Doctor_Sch']
     insert1={'Doc_id':t1,'Doc_nm':t2,'Start_dt':t3,'End_Dt':t4,'Start_time':t5,'End_time':t6}
     collection.insert_one(insert1)
     print("<script>alert('Data_Saved.....')</script>")
     #Update Button:-
    if(btn=="Update"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hospital']
     collection=db['Doctor_Sch']
     collection.update_one({'Doc_id':t1},{'$set':{'Doc_nm':t2,'Start_dt':t3,'End_Dt':t4,'Start_time':t5,'End_time':t6}})
     print("<script>alert('Record Update sir  .....')</script>")
#Delete Button
    if(btn=="Delete"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Doctor_Sch']
        s={'Doc_id':t1}
        collection.delete_many(s)
        print("<script>alert('Record Deleted.....')</script>")
#AllSearch Button:
    if(f.getvalue("b1")=="Allsearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Doctor_Sch']
        print("<center><table border=15 cellpadding=5 <tr><th>Doc_id</th> <th> doc_nm</th> <th>Start_dt</th>  <th>End_Dt</th>  <th>Start_time</th> <th>End_time</th> ")
        for x in collection.find({}):
            print("<tr><th>",x["Doc_id"],"</th>","<th>",x["Doc_nm"],"</th>","<th>",x["Start_dt"],"</th>","<th>",x["End_Dt"],"</th>","<th>",x["Start_time"],"</th>","<th>",x["End_time"],"</th>","</th></tr>") 
            print("<body><input  type=button value='Report' onclick=window.print()></body>")
#particular Search Button:
    if(f.getvalue("b1")=="Psearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Doctor_Sch']
        print("<center><table border=15 cellpadding=5  <tr><th>Doc_id</th> <th> Doc_nm</th> <th>Start_dt</th> <th>End_Dt</th>  <th>Start_time</th> <th>End_time</th> ")
        for x in collection.find({'Doc_id':t1}):
            print("<tr><th>",x["Doc_id"],"</th>","<th>",x["Doc_nm"],"</th>","<th>",x["Start_dt"],"</th>","<th>",x["End_Dt"],"</th>","<th>",x["Start_time"],"</th>","<th>",x["End_time"],"</th>","</th></tr>") 
except Exception:
    traceback.print_exc()
     