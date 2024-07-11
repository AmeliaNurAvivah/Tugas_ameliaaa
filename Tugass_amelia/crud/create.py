import mysql.connector

def create_record(id, nama, spesialisasi):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rumah_sakit"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO pasien_rs (id, nama, spesialisasi) VALUES ( %s, %s, %s)"
    val = (id, nama, spesialisasi)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()