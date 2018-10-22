import pymysql

conn = pymysql.connect(host = "localhost", port = 3306, user = "root",
                password = "1234qwer", database="python_test_1", charset="utf8")

cursor = conn.cursor()


cursor.execute("select * from pythontest.classes;")



row_data = cursor.fetchone()
row_data2 = cursor.fetchall()

print(row_data2)
cursor.close()
conn.close()
