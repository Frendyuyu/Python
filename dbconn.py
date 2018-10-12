import pyodbc
data = {}
countn = 0
DBfile = r"E:\wwwroot\DB\Material.accdb;"  # 数据库文件
conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile)

cursor = conn.cursor()
if __name__ == "__main__":
    "Program Start"

    SQL = "SELECT * from Dri;"
    # Test = cursor.execute(SQL)
    # print(type(Test))


    '''
    for row in cursor.execute(SQL):
        print("=====" * 20)
        data[countn] = row
        countn = countn + 1

        print(row)
    '''
    cursor.close()
    conn.close()
