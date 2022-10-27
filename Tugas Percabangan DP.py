#Tugas Dasar Pemrograman
#Nama: Abu Nur Al-Faruq
#Kelas: Ti 22 E
#Nim: 20220040223


 nama = input("Masukan Nama : ")

 nilai = int(input("Masukan Nilai : "))
if nilai >= 90 :
  grade = "A"
  print("Dengan Pujian")
elif nilai >= 80:
  grade = "B"
  print("Sangat Memuaskan")
elif nilai >= 70:
  grade = "C"
  print("Memuaskan")
elif nilai >= 60:
  grade = "D"
  print("Tidak Memuaskan")
elif nilai >= 0:
  grade = "E"
  print("Tidak Lulus")
  else:
  print("Input Salah")
  
print("Nama :", nama, "Grade kamu", grade)