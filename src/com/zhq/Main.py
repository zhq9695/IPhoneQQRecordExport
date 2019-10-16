# coding:utf-8
import sqlite3 as db
import time

database_path = ""
database_name = ""
store_file_path = ""
my_name = ""
user_name = ""

# 从SQLite文件中读取数据
def readFronSqllite(db_path, exectCmd):
    conn = db.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor = conn.cursor()  # 该例程创建一个 cursor，将在 Python 数据库编程中用到
    cursor.execute(exectCmd)  # 该例程执行一个 SQL 语句
    rows = cursor.fetchall()  # 该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    return rows


if __name__ == "__main__":
    rows = readFronSqllite(database_path, "SELECT * FROM " + database_name + "ORDER by time")
    with open(store_file_path, "w", encoding='utf-8') as f:
        for row in rows:
            print(float(rows.index(row)) * 100 / len(rows), '%')
            user = ""
            if row[4] == 0:
                user = my_name
            elif row[4] == 1:
                user = user_name
            content = row[6]
            if content == None:
                content = ""
            t = time.localtime(row[2])
            t = time.strftime("%Y-%m-%d %H:%M:%S", t)
            f.write(user + " " + t + " :\n")
            f.write(content + "\n")
    print("DONE")
