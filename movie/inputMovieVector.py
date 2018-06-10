import connectDB
import countVec


def exec(train_dataSet):
    cursor = connectDB.exec()   #DB접속
    compacted_Infos=countVec.exec(train_dataSet)

    for mv in compacted_Infos:
        code=mv[0]
        title=mv[1]
        vector=str(mv[2])
        cursor.execute("insert into movieVector(code,title,vector) values(%d,'%s','%s')"%(code,title,vector))
        cursor.execute("commit")
        print(title," ",code)

