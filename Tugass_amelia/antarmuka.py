from crud.read import read
from crud.create import create_record
from crud.update import update_record
from crud.delete import delete_record

def main():
    while True:
        print("\nMODIFIKASI DATABASE")
        print("-----------------------------------------")
        print("1. CREATE")
        print("2. READ")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. EXIT")
        print("-----------------------------------------")

        pil = int(input("MASUKKAN PILIHAN: "))

        if pil == 1:
            id = int(input("Masukkan  ID: "))
            nama = input("Masukkan nama: ")
            spesialisasi = input("Masukan Spesialisasi Dokter: ")
            create_record( id, spesialisasi, nama )
            print("\nData berhasil ditambahkan\n.")
            read()

        elif pil == 2:
            read()

        elif pil == 3:
            id = int(input("Masukkan ID : "))
            nama = input("Masukkan nama : ")
            spesialisasi = input("Masukan Spesialisasi Dokter: ")
            update_record(id, nama, spesialisasi)
            print("\nData berhasil diupdate\n.")
            read()

        elif pil == 4:
            id = int(input("Masukkan ID Pasien yang ingin dihapus: "))
            delete_record(id)
            print("\nData berhasil dihapus\n.")
            read()

        elif pil == 5:
            print("Sampai Jumpa!")
            break
        else:
            print("Pilihan tidak Tersedia. Silakan coba lagi.")

if __name__ == "__main__":
    main()