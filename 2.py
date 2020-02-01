import re;

print("Tool untuk membuat username dan password yang sesuai Arkademy batch 5 tes")
cekUsername = raw_input("Masukkan Username : ")
cekPassword = raw_input("Masukkan Password : ")
if re.match("^x[A-Z]{4,7}x$", cekUsername) and re.match("(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{3}", cekPassword):
    print("Pas Sekali")
else:
    print("Coba lagi")