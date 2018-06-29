import csv
import MySQLdb
HOST = 'localhost'
USER = 'ganesh'
PASSWORD = 'ganesh55'
DATABASE = 'ACADEMIC_REPORT'


db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS VIKAS_studentmarks (student_name VARCHAR(30), subject VARCHAR(30),  marks FLOAT(100,2))')
cursor.execute('CREATE TABLE IF NOT EXISTS VIKAS_subjectfaculty (subject VARCHAR(30), name VARCHAR(30))')

with open('/home/ganesh/dev/ACADEMIC_REPORT/VIKAS/student_marks.csv','r') as marks_csv:
    student_data = csv.reader(marks_csv)
    for x in student_data:
        #print (x[2],float(x[2]))
        cursor.execute('INSERT INTO VIKAS_studentmarks (student_name,subject,marks) values(%s ,%s ,%s )',(x[0],x[1],x[2]))
with open('/home/ganesh/dev/ACADEMIC_REPORT/VIKAS/subject_faculty.csv','r') as subject_csv:
    subject_data = csv.reader(subject_csv)
    for y in subject_data:
        print (y)
        cursor.execute('INSERT INTO VIKAS_subjectfaculty (subject,name) values(%s ,%s  )',(y[0],y[1]))

db.commit()
cursor.close()
