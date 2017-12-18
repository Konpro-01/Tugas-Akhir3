#nama program
print ("Alat Terjemahan Angka Sederhana \n")
#database terjemahan
Dictionary = {1:"one", 2:"dua", 3:"tiga",4:"four",5:"five",6:"six",7:"seven", 8:"eight", 9:"nine", 10:"ten"}
Kamus_Palembang = {1:"sikok", 2:"duo", 3:"tigo", 4:"empat", 5:"limo", 6:"enem", 7:"tojo", 8:"lapan", 9:"sembilan", 10:"sepulo"}

#Fungsi untuk mendefinisikan option yang akan dipilih
def option ():
    print ("\n")
    print ("Pilihlah bahasa")
    print ("1.Inggris")
    print ("2.Palembang")
    print ("3. Exit")
    pilihan = int(input("Masukan pilihan anda :"))
    return pilihan

#Fungsi untuk mendefinisikan bahasa ingrris
def Inggris():
    pilih= int(input("Input number :"))
    pilih in Dictionary
    print (Dictionary.get(pilih))
    return pilih

#Fungsi untuk mendefinisikan bahasa jawa
def Palembang():
    pilih=int(input("Masoke angko:"))
    pilih in Kamus_Palembang
    print(Kamus_Palembang.get(pilih))
    return pilih

#Program inti pemanggil function option dan function inggris 
pilihan = True
while(pilihan<3):
    pilihan = option()
    if (pilihan ==3):
        break;
    else:
        if (pilihan==1):
            Inggris ()
        elif (pilihan ==2):
            Palembang()
