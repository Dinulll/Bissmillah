nama = "Dini Aulia Hidayati"
panggil = "Dinul"
nim = 202410102072
asal = "Jember"
kel = "ORACLE"

name = input("Nama : ")
nick = input("Nama panggilan : ")
no = input("NIM : ")
dr = input("Asal : ")
klmpk = input("Kelompok : ")

if name == nama or nick == panggil or no == nim or dr == asal or klmpk == kel :
    print("Halo nama saya " +name, "biasa dipanggil " +nick, "NIM " +no, "Saya berasal dari " +asal, "dari kelompok " +klmpk )
else :
    print("Data yanng diinputkan tidak sesuai")