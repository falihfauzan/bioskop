print ("**********Selamat Datang Di CGF Blitch**********")

print ("\nDaftar Film Hari ini :")
def list ():
    print ("==========================================")
    print ("(1) **Teater 1**")
    print ('- Film 1                    : 10.00     = Rp. 50.000')
    print ('- Film 2                    : 12.00     = Rp. 50.000')
    print ('- Film 3                    : 14.00     = Rp. 50.000')
    print ("(2) **Teater 2**")
    print ('- Film 4                    : 11.00     = Rp. 50.000')
    print ('- Film 5                    : 13.00     = Rp. 50.000')
    print ('- Film 6                    : 15.00     = Rp. 50.000')
    print ("==========================================")
list()

a = int (input("Silahkan Pilih Teater (Silahan Ketik Nomor)"))
if a == 1:
    print ("1. Film 1      : 10.00")
    print ("2. Film 2      : 12.00")
    print ("3. Film 3      : 14.00")
elif a == 2:
    print ("4. Film 4      : 11.00")
    print ("5. Film 5      : 13.00")
    print ("6. Film 6      : 15.00")
else:
    while True:
        print ("**********Teater Tidak Tersedia, Silahkan Pilih Lagi!**********")
        a = int (input("Silahkan Pilih Teater (Silahkan Ketik Nomor): "))
        if a == 1 or a == 2:
            if a == 1:
                print ("1. Film 1      : 10.00")
                print ("2. Film 2      : 12.00")
                print ("3. Film 3      : 14.00")
            elif a == 2:
                print ("4. Film 4      : 11.00")
                print ("5. Film 5      : 13.00")
                print ("6. Film 6      : 15.00")
            break
a = int (input("Silahkan Pilih Film (Silahkan Ketik Nomor)"))
if a == 1:
    spec = 'Film 1 (10.00)'
    harga = 50000
elif a == 2:
    spec = 'Film 2 (12.00)'
    harga = 50000
elif a == 3:
    spec = 'Film 3 (14.00)'
    harga = 50000
elif a == 4:
    spec = 'Film 4 (11.00)'
    harga = 50000
elif a == 5:
    spec = 'Film 5 (13.00)'
    harga = 50000
elif a == 6:
    spec = 'Film 6 (15.00)'
    harga = 50000
else:
    while True:
        print ("**********Film Tidak Tersedia, Silahkan Pilih Lagi!**********")
        a = int (input("Silahkan Pilih Film(Silahkan Ketik Nomor): "))
        if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or 6:
            if a == 1:
                spec = 'Film 4 (11.00)'
                harga = 50000
            elif a == 2:
                spec = 'Film 5 (13.00)'
                harga = 50000
            elif a == 3:
                spec = 'Film 6 (15.00)'
                harga = 50000
            elif a == 4:
                spec = 'Film 4 (11.00)'
                harga = 50000
            elif a == 5:
                spec = 'Film 5 (13.00)'
                harga = 50000
            elif a == 6:
                spec = 'Film 6 (15.00)'
                harga = 50000
            break
total = int (input("Masukan Jumlah Tiket Pembelian :"))
print('\nNota Pembelian Tiket')

print('Film          :',spec)
print('Jumlah Tiket     :',total)
print('Harga            :Rp.',harga)
bayar = total * harga

print ("Anda Harus Membayar : Rp.{}".format(bayar))
ubay=int(input("Uang Bayar :"))
kembali=(ubay-bayar)
print('Uang Kembali :',kembali)
print('\nNote : Bonus Didalam Teater')
bonus = ['botol Air Minum','Pop Corn']
for i in range (len(bonus)):
    print("1",bonus[i])
print ("===========================================================================")
print ('******** Terima Kasih Dan Selamat Menonton ********')
print ("===========================================================================")
exit()