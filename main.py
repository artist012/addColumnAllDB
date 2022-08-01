import sqlite3
import sys
import os

dir_path = "./"

def addCol(tableName, colName, colType):
    for (root, directories, files) in os.walk(dir_path):
        for file in files:
            con = sqlite3.connect(os.path.join(root, file))
            cur = con.cursor()
            try:
                cur.execute("ALTER TABLE {} ADD COLUMN {} {};".format(tableName, colName, colType))
                print('[{}] "{}" 컬럼이 {} 타입으로 생성되었습니다\n'.format(file, colName, colType))
            except sqlite3.OperationalError:
                print("[{}] 테이블이 없거나 컬럼명이 겹칩니다\n".format(file))
            except sqlite3.DatabaseError:
                print("[{}] 이 파일은 DB파일이 아닙니다\n".format(file))

if __name__ == "__main__":
    try:
        addCol(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print("전달된 인자값이 없습니다\nmain.py [테이블명] [컬럼명] [컬럼타입]")