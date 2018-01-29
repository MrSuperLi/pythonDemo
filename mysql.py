import pymysql

connection = pymysql.connect(host="192.168.146.141", port=3306, user="root",
                             password="123456", db="oa_debug", charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

cursor.execute("select * from human_user where account=%s and user_id=%s", ('qingliang', 13))

print(cursor.description)

for row in cursor:
    print(row)

cursor.close()