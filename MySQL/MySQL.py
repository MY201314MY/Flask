import pymysql

db = pymysql.connect(
    "localhost",
    "root",
    "123456",
    "flask")

print("******MySQL Database******")
cursor = db.cursor()
def version():
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("database version: %s" % data)


def information():
    cursor.execute("SELECT user,PLUGIN FROM mysql.user")
    message = cursor.fetchall()
    print("There're %d users totally in MySQL" % len(message))
    for information in message:
        if information[0] == 'root':
            print("账号：%s 密码：%s" % (information[0], information[1]))
            break


def table():
    cursor.execute("DROP TABLE IF EXISTS machine")

    sql = """CREATE TABLE machine(
        name CHAR(32) NOT NULL ,
        age INT,
        temperature FLOAT )"""
    cursor.execute(sql)


def insert():
    sql = """
    INSERT INTO machine(name, age, temperature)
    VALUES ("MacBook pro", %d, 38.6)       
    """ % 6
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def query():
    sql = """SELECT*FROM machine
    """
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            name = row[0]
            age = row[1]
            temperature = row[2]

        print("****  设备名称：%s -- 使用年限：%s -- 温度：%s C****" % (name, age, temperature))
    except:
        print("Error: unable to fetch data.")


def update():
    sql = """
    UPDATE machine SET age=age+1 WHERE name='MacBook pro' 
    """
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


if __name__ == "__main__":
    update()
    query()
    db.close()



