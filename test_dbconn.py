from dbconn import *

if __name__ == "__main__":
	for i in cursor.execute("SELECT * FROM DRI;"):
		print(i)
		