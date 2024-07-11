
import mysql.connector

def update_record(id,  nama, spesialisasi ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="rumah_sakit"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE pasien_rs SET id = %s, nama = %s, spesialisasi = %s WHERE id = %s"
        val = (id, nama, spesialisasi, id)
        print("Executing SQL:", sql % val)  
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()


