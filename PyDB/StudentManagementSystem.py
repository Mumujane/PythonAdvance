import pymysql
import re
import time
import hashlib
import random


def connet_db():
    """ 连接数据库 start """

    conn = pymysql.connect(host="localhost", port=3306, user="root",
                           password="1234qwer", database="python_test_1", charset="utf8")
    return conn


def doquery(table, row):

    #$sql = "select * from $table $where $order $limit";
    sql = "select * from `table` where `field`='{$id}' limit 1";
    pass

def register(cs, table, row):
    """
    注册的函数
    :param cs: Cursor对象
    :param table: 表名
    :param kwargs: 插入的键值对 字典
    :return: 
    """
    sqlA = list();
    for key in row:
        if row[key] is null:
            sqlA.append("`key` = NULL")
        else:
            sqlA.append("`key` = 'row[key]'")

    sqlA = ','.join(sqlA)
    print(sqlA)
    # insert into table_name set a=$a,b=$b”
    sql = "insert into `table` set $sqlA";
    cs.execute(sql)

def login():
    pass



def encode_password(password, salt):
    password = hashlib.md5(hashlib.md5(password) + salt);
    return password


def gen_salt():
    current_milli_time = lambda: int(round(time.time() * 1000))
    return hashlib.md5(current_milli_time()+random.randint(0,10000));

def searchClassInfo():
    pass


def searchCourseInfo():
    pass


def searchScorebyUid():
    pass


def searchScorebyCid():
    pass


def getBy(table, field_name, val):
    """
     查询获取一条数据

    :param table:
    :param field_name:
    :param val:
    :return:
    """
    sql = " select * from %s where `%s` = '%s' limit 1" %(table, field_name, val)




def main():
    conn = connet_db()
    # 获得游标对象
    cs = conn.cursor()
    while True:
        # 打印信息
        # alt+鼠标
        print("1 注册")
        print("2 登录")
        print("3 查看您的班级信息")
        print("4 查看课程,并选修")
        print("5 查看已经选择的要进修的课程")
        print("6 查看考试成绩")
        print("7 退出登录")

        # 等待用户的输入
        action = input()

        # 根据不同的指令完成不同的功能
        if action == "1":
            print()
            # 注册
            while True:
                mobile = input("请输入的手机号码")
                pwd = input("请输入您的密码")

                print(re.match(r"^1[35678]\d{9}$", mobile))

                if len(mobile) == 11 and re.match(r"^1[35678]\d{9}$", mobile):
                    # 查询是否有存在的信息
                    if getBy("mobile", mobile):
                        print("手机号可以使用,请完善您的信息")
                    else:
                        print("该手机已经被绑定, 不能重复绑定")
                        break
                else:
                    print("非法手机号,请重新输入")
                    break

                name = input("请输入用户名")

                # 注册:
                table = "users"
                salt = gen_salt()
                row = {
                    'name': name,
                    'mobile':mobile,
                    'password':encode_password(pwd, salt),
                    'salt':salt,
                    'reg_time':time.time(),
                }
                register(cs, table, row)

                # 完善用户姓名信息
                TODO

        elif action == "2":
            # 登录
            sign_up()
        elif action == "3":
            # 查看班级信息
            searchClassInfo()
        elif action == "4":
            # 查看课程信息
            searchCourseInfo()
            print("请输入种类名称")

        elif action == "5":
            # 查看选修课程
            searchSelectedCoursebyUid()
        elif action == "6":
            # 查看考试成绩

            # 查看全部考试成绩
            searchScorebyUid()
            # 查看指定课程的考试成绩
            searchScorebyCid()

        elif action == "7":
            # 退出
            break;
        else:
            print("亲,您的输入有误!")
    # 关闭
    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
