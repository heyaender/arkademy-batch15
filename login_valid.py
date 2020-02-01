print "Welcome to Arkademy Bootcamp Batch 15"
print "Silahkan masukkan username dan password terlebih dahulu !"

login = False
akun = {'xANDRIx':'gila@WWW'}


while not login: #perulangan untuk mencocokan inputan user dengan data akun sampai dengan kondisi benar
    username = raw_input("Username : ")
    password = raw_input("Password : ")
    if username == akun and password == akun:
        continue
    elif username not in akun:
        print("Pengguna ini tidak ada !")
        continue
    elif password != akun[username]:
        print("Password salah !")
        continue
    elif password == akun[username]:
        print("Selamat datang kembali {} di Arkademy".format(username))
        exit
        login = True
