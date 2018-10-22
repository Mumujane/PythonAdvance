"""
上下文管理器的使用
    上下文管理器的作用: 可以使用with
    实现 __exit__ 和 __enter__ 方法的类可以称为上下文管理器
"""
# class MyOpen(object):
#     def __init__(self):
#         print("init fun")
#
#     def __enter__(self):
#         print("enter")
#         return 100
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exit")
#
#
# with MyOpen() as f:
#     print(f)
#
# print("end")

from pymysql import connect

""" 
实现文件自动关闭功能: 
with open("./test.py") as f:
    content = f.read()   
"""


class Myopen(object):
    def __init__(self, path, mode="r"):
        self.f = open(path, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Now Exiting ...")
        self.f.close()


with Myopen("../Test.py", "a") as f:
    f.write("###123")
print("end")

print("===" * 10)
""" 使用生成器实现功能   """
from contextlib import contextmanager


@contextmanager
def MyYopen(path, mode="r"):
    f = open(path, mode)

    try:
        yield f
        print("yield exit")
    finally:
        # Code to release resource, e.g.:
        print("finally exit ")
        f.close()


with MyYopen("../Test.py", "a") as f:
    f.write("###hlsad")

print("===" * 10)

""" 实现数据库的自动关闭 """


class MyDatabaseOpen(object):
    def __init__(self, p_database, p_user, p_password, ):
        self.conn = connect(host='localhost', port=3306, database=p_database, user=p_user, password=p_password,
                            charset='utf8')

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        # 关闭
        self.conn.cursor().close()
        self.conn.close()


with MyDatabaseOpen(p_database='jing_dong', p_user='root', p_password='1234qwer') as cursor:
    id = 1
    sql = """ select * from goods where id = %s;"""
    cursor.execute(sql, (id,))  # sql参数化这个安全的sql语句 ,sql注入

    # 执行sql语句
    name = "xiaohui"
    sql = """ INSERT INTO classes (name) VALUES ("%s");""" % name
    cursor.execute(sql)
    print(cursor.execute(sql))

    # 得到数据
    data = cursor.fetchall()
    print(data)
print(dir())