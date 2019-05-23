import psycopg2
conn=psycopg2.connect(
	database="testdb",
	user="postgres",
	password="iamagoodboy600",
	host="localhost",
	port="5433",
)
cur=conn.cursor()
#row=cur.execute("create table demo2(id INT primary key,student_name char(20) not null,marks int)")
cur.execute("insert into demo2 values(2,'prafulla',44);")
conn.commit()

