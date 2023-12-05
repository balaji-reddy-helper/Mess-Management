# Mess-Management  
Problem Statement:  
The goal of the project is to avoid students to carry their mess card to access dining facilities. This includes the creation of database to manage students’ information related to mess and mess incharge access the student details who are from incharge mess by searching the database using student ID.  

Database Used:  
•	Database: MONGODB  
•	Language: Python and Flask web Framework  
•	Frontend: HTML and CSS  

Database Schema:  
we have two collections(mess incharge,students) with fileds as follws  
Mess Incharge:  
  {  
    incha_id: 'nittm1',  
    name: 'subbarao',  
    mess: 'MM1',  
    mess_type: 'south_indian',  
    password: 'subbarao123',  
    user_id: 'subbaraomm1'  
  }  
Student:  
  {  
    stud_id: 23020,  
    name: 'cheta',  
    mess: 'MM4',  
    hostel: 'Jade',  
    room_no: 119,  
    phone: [ Long('9841612305') ]  
  }  

List of stakeholders:  
•	Mess incharge  
•	Student  

 Frontend:  
 html pages will be stored in templates folder  
 Backend:  
 Data created in database is stored in text files(Admin.txt,student.txt).  
