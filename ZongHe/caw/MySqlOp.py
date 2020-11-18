"""
查数据库操作
"""

# 连接数据库
import pymysql


def connect(db):
    """
    链接数据库
    :param db:db={"ip":"jy001","port":"4406","dbName":"future","username":"root","pwd":"123456"}
    :return:
    """
    host = db['ip']
    port = int(db["port"])
    user = db["username"]
    name = db["dbName"]
    pwd = db["pwd"]
    try:
        conn = pymysql.connect(host=host, port=port, user=user, database=name, password=pwd, charset='utf8')
        print(f"链接数据库{host}:{port}成功")
    except Exception as e:
        print(f"链接数异常，异常信息:{e}")
    return conn


# 断开数据库链接
def disconnect(conn):
    try:
        conn.close()
        print(f"断开数据库成功")
    except Exception as e:
        print(f"断开数据库链接，异常信息:{e}")


# 执行sql语句
def execute(conn, sql):  # 链接相当于建了一条到数据库的路
    try:
        cursor = conn.cursor()  # 获取游标，相当于在路上跑的一辆车，通过车把数据取回来
        cursor.execute(sql)  # 执行sql语句
        conn.commit()  # 提交
        cursor.close()  # 关闭游标
        print(f"执行sql语句{sql}成功")
    except Exception as e:
        print(f"执行SQL语句{sql}异常，异常信息:{e}")


# 测试代码
if __name__ == '__main__':
    db = {"ip": "jy001", "port": "4406", "dbName": "future", "username": "root", "pwd": "123456"}
    conn = connect(db)
    execute(conn, "delete from Member where MobilePhone=18012345678;")
    disconnect(conn)
