ans=True
while ans:
    print ("""=============================
        PROGRAM SEDERHANA
    1.Menghitung Waktu Tempuh
    2.Delete a Student
    3.Look Up Student Record
    0.Exit/Quit
=============================""")
    ans = input("Pilih pilihanmu: ") 
    if ans == "1":
      waktutempuh=0.0
      jarak=0.0
      kecepatan=0.0
      print("=============================")
      print("   Menghitung Waktu Tempuh")
      jarak = input("Masukan jarak (km): ")
      jarak = float(jarak)
      
      kecepatan = input("Masukan kecepatan (km/jam): ")
      kecepatan = float(kecepatan)
      
      waktutempuh = jarak/kecepatan
      print("waktu tempuh:", waktutempuh,"jam")
      print("")
    elif ans == "2":
      print("\n Student Deleted") 
    elif ans == "3":
      print("\n Student Record Found") 
    elif ans == "0":
      print("\n Goodbye")
      break
    elif ans != "":
      print("\n Coba pilih yang ada di daftar!") 
