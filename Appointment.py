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
     db=client['Hospital']
     collection=db['Appointment']
#primary key:-
     k=0
     for x in collection.find({}):
        if(x['App_id']==t1):
                k=1
                break
     if(k==1):
      print("<script>alert('Error id .....')</script>")
     else:
        insert1={'App_id':t1,'Hos_id':t2,'App_date':t3,'App_time':t4,'Dt_id':t5,'Srv_id':t6,'Pat_id':t7}
        collection.insert_one(insert1)
        print("<script>alert('Data_Saved.....','_self')</script>")

#Update Button:-
    if(btn=="Update"):
     client=pymongo.MongoClient("mongodb://localhost:27017/")
     db=client['Hospital']
     collection=db['Appointment']
     collection.update_one({'App_id':t1},{'$set':{'Hos_id':t2,'App_Date':t3,'App_Tme':t4,'DT_id':t5,'Srv_Id':t6,'Pat_id':t7}})
     print("<script>alert('Record Update sir  .....')</script>")
#Delete Button
    if(btn=="Delete"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Appointment']
        s={'App_id':t1}
        collection.delete_many(s)
        print("<script>alert('Record Deleted.....')</script>")
#AllSearch Button:
    if(f.getvalue("b1")=="Allsearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Appointment']
        print("<center><table border=15 cellpadding=5 <tr><th>App_id</th> <th> Hos_id</th> <th>App_Data</th> <th>App_Time</th>  <th>Dt_id</th> <th>Srv_id</th> <th>Pat_id</th></tr>")
        for x in collection.find({}):
            print("<tr><th>",x["App_id"],"</th>","<th>",x["Hos_id"],"</th>","<th>",x["App_date"],"</th>","<th>",x["App_time"],"</th>","<th>",x["Dt_id"],"</th>","<th>",x["Srv_id"],"</th>", "<th>",x["Pat_id"],"</th>","</th></tr>")
            print("<body><input  type=button value='Report' onclick=window.print()></body>")
#particular Search Button:
    if(f.getvalue("b1")=="Psearch"):
        client=pymongo.MongoClient("mongodb://localhost:27017/")
        db=client['Hospital']
        collection=db['Appointment']
        print("<center><table border=15 cellpadding=5 <tr><th>App_id</th><th> Hos_id</th> <th>App_Data</th> <th>App_Time</th>  <th>Dt_id</th> <th>Srv_id</th> <th>Pat_id</th></tr>")
        for x in collection.find({'App_id':t1}):
            print("<tr><th>",x["App_id"],"</th>","<th>",x["Hos_id"],"</th>","<th>",x["App_data"],"</th>","<th>",x["App_time"],"</th>","<th>",x["Dt_id"],"</th>","<th>",x["Srv_id"],"</th>", "<th>",x["Pat_id"],"</th>","</th></tr>") 
except Exception:
    traceback.print_exc()