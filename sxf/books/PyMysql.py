
import pymysql

# 打开数据库连接
db = pymysql.connect('localhost','root','root','forenms_ycrs')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select * from app_access")

# 使用 fetchall() 方法获取s所有数据.
data = cursor.fetchall()

print(data)

# 关闭数据库连接
db.close()



