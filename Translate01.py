#nama program
print ("Alat Terjemahan Angka Sederhana \n")
#database terjemahan
dictionary = {1:"one", 2:"dua", 3:"tiga",4:"four",5:"five",6:"six",7:""}

#Fungsi untuk mendefinisikan option yang akan dipilih
def option ():
    print ("\n")
    print ("Pilihlah bahasa")
    print ("1.Inggris")
    print ("2. Exit")
    pilihan = int(input("Masukan pilihan anda :"))
    return pilihan
#Fungsi untuk mendefinisikan bahasa ingrris
def inggris():
    pilih= int(input("Masukan angka :"))
    pilih in dictionary
    print (dictionary.get(pilih))
    return pilih

#Program inti pemanggil function option dan function inggris 
pilihan = True
while(pilihan<2):
    pilihan = option()
    if (pilihan ==2):
        break;
    else:
        if (pilihan==1):
            inggris ()
