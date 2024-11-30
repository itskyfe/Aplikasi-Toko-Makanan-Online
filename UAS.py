from prettytable import PrettyTable
from datetime import datetime
import colorama 
from colorama import Fore
import pwinput

colorama.init(autoreset=True)

#************** Data yang diperlukan Fitur *******************

# Data akun
akun = [
    {"username":"rizky", "password":"123", "saldo":0, "gold":100, "status":"biasa"},
    {"username":"sultan", "password":"asd", "saldo":0, "gold":0, "status":"vip"}
]

# List menu sarapan
sarapan = [
    {"no": 1, "nama_makanan":"bubur ayam", "harga":5, "stok":10},
    {"no": 2, "nama_makanan":"nasi kuning", "harga":5, "stok":10},
    {"no": 3, "nama_makanan":"nasi campur", "harga":5, "stok":10},
    {"no": 4, "nama_makanan":"nasi pecel", "harga":5, "stok":10},
    {"no": 5, "nama_makanan":"nasi uduk", "harga":5, "stok":10}
]

# List menu makan siang
makan_siang = [
    {"no": 1, "nama_makanan":"gado-gado", "harga":5, "stok":10},
    {"no": 2, "nama_makanan":"ayam goreng", "harga":5, "stok":10},
    {"no": 3, "nama_makanan":"soto ayam", "harga":5, "stok":10},
    {"no": 4, "nama_makanan":"mie ayam", "harga":5, "stok":10},
    {"no": 5, "nama_makanan":"bakso", "harga":5, "stok":10}
]

# List menu makan malam
makan_malam = [
    {"no": 1, "nama_makanan":"nasi goreng", "harga":5, "stok":10},
    {"no": 2, "nama_makanan":"mie goreng", "harga":5, "stok":10},
    {"no": 3, "nama_makanan":"tahu tek-tek", "harga":5, "stok":10},
    {"no": 4, "nama_makanan":"sate ayam", "harga":5, "stok":10},
    {"no": 5, "nama_makanan":"lalapan", "harga":5, "stok":10}
]

# List paket gold member biasa 
gold_biasa = [
    {"no": 1, "paket":"murah", "gold":10, "harga":12000},
    {"no": 2, "paket":"sedang", "gold":25, "harga":27000},
    {"no": 3, "paket":"sultan", "gold":50, "harga":52000},
    {"no": 4, "paket":"gacor", "gold":100, "harga":102000},
]

# List paket gold member vip
gold_vip = [
    {"no": 1, "paket":"hemat", "gold":5, "harga":5000},
    {"no": 2, "paket":"murah", "gold":10, "harga":8000},
    {"no": 3, "paket":"sedang", "gold":25, "harga":20000},
    {"no": 4, "paket":"sultan", "gold":50, "harga":40000},
    {"no": 5, "paket":"gacor", "gold":100, "harga":80000},
]

# List voucher 
voucher = [
    {"kode_voucher":"gacor3", "jumlah_diskon":3, "status":"available"},
    {"kode_voucher":"gacor5", "jumlah_diskon":5, "status":"available"},
    {"kode_voucher":"gacor7", "jumlah_diskon":7, "status":"available"}
]

#*************************************************************

#************** Fungsi Pendukung Fitur ***********************

# Function tabel untuk memuat menu makanan
def tabel(data):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama makanan", "Harga", "Stok"]
    for menu in data:
        tabel.add_row([menu["no"], menu["nama_makanan"], menu["harga"], menu["stok"]])
    print(tabel)

# Function tabel untuk memuat paket gold
def list_gold(data):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Paket", "Jumlah Gold", "Harga"]
    for list in data:
        tabel.add_row([list["no"], list["paket"], list["gold"], list["harga"]])
    print(tabel)
    return tabel

# Function untuk menampilkan Invoice
def invoice(nama_makanan, jumlah, total_harga, diskon, total_harga_setelah_diskon):
    struk = PrettyTable()
    struk.field_names = ["Invoice Pembayaran"]
    struk.add_row([f"Tanggal Transaksi : {datetime.now().strftime("%d-%m-%y %H:%M:%S")}"])
    struk.add_row([f"Nama Makanan : {nama_makanan}"])
    struk.add_row([f"Jumlah Item : {jumlah} item"])
    struk.add_row([f"Total Harga : {total_harga} gold"])
    struk.add_row([f"Diskon : {diskon} gold"])
    struk.add_row([f"Total Bayar : {total_harga_setelah_diskon} gold"])
    struk.add_row(["Terima kasih sudah bertransaksi"])
    print(struk)

# Function untuk transaksi
def transaksi(data, user):
    while True:
        try:
            pilih = int(input("Masukkan pilihan menu anda (ketik 0 jika ingin kembali) : "))
            if pilih == 0 and user["status"] == "biasa":
                menu_biasa(user)
            if pilih == 0 and user["status"] == "vip":
                menu_vip(user)
            for menu in data:
                if pilih == menu["no"]:
                    jumlah = int(input("Masukkan jumlah makanan yang ingin dipesan : "))
                    if jumlah <= 0:
                        print(Fore.RED + "jumlah tidak valid")
                    else:
                        if jumlah > menu["stok"]:
                            print(Fore.RED + "Stok tidak mencukupi")
                        else:
                            total_harga = jumlah * menu["harga"]
                            print(Fore.CYAN + f"Total belanjaan anda adalah : {total_harga} gold")
                            opsi_voucher = str(input("Apakah anda ingin menggunakan voucher? (y/n): ")).lower()
                            if opsi_voucher == "y":
                                masukan_voucher = input("Masukkan kode voucher anda : ")
                                for kode in voucher:
                                    if masukan_voucher == kode["kode_voucher"] and kode["status"] == "available":
                                        if total_harga <= kode["jumlah_diskon"]:
                                            print(Fore.RED + "Kode tidak bisa digunakan karena melebih batas diskon")
                                        else:
                                            total_harga_setelah_diskon = total_harga - kode["jumlah_diskon"]
                                            if user["gold"] < total_harga_setelah_diskon:
                                                print(Fore.RED + "Gold anda tidak cukup")
                                            else:
                                                user["gold"] -= total_harga_setelah_diskon
                                                menu["stok"] -= jumlah
                                                kode["status"] = "unavailable"
                                                print(Fore.GREEN + "Transaksi Berhasil!")
                                                invoice(menu["nama_makanan"], jumlah, total_harga, kode["jumlah_diskon"], total_harga_setelah_diskon)
                                                break
                                else:
                                    print(Fore.RED + "voucher tidak valid")
                                    break
                            elif opsi_voucher == "n":
                                if user["gold"] < total_harga:
                                    print(Fore.RED + "Gold anda tidak cukup")
                                else:
                                    user["gold"] -= total_harga
                                    menu["stok"] -= jumlah
                                    diskon = "0"
                                    total_harga_setelah_diskon = total_harga
                                    print(Fore.GREEN + "Transaksi Berhasil!")
                                    invoice(menu["nama_makanan"], jumlah, total_harga, diskon, total_harga_setelah_diskon)
                            else:
                                print(Fore.RED + "Opsi tidak ada")
                    break
        except ValueError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except EOFError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
            
# Function untuk penukaran saldo menjadi gold
def top_up_gold(data, user):
    while True:
        try:
            list_gold(data)
            pilihan = int(input("Masukkan nomor paket gold (ketik 0 untuk kembali) : "))
            if pilihan == 0:
                break
            for paket in data:
                if pilihan == paket["no"]:
                    if user["saldo"] < paket["harga"]:
                        print(Fore.RED + "Saldo Anda tidak mencukupi untuk top-up gold.")
                    else:
                        user["saldo"] -= paket["harga"]
                        user["gold"] += paket["gold"]
                        print(Fore.GREEN + f"=== Top-Up Gold berhasil! ===")
                    break
            else:
                print(Fore.RED + "Pilihan paket tidak ditemukan.")
        except ValueError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except EOFError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")

#**************************************************************

#**************** Fungsi Yang Memuat Fitur ********************

# Function login
def login():
    percobaan = 3
    while True:
        print("+--------------+")
        print("| Landing Page |")
        print("+--------------+")
        print("|  1. Login    |")
        print("|  2. Keluar   |")
        print("+--------------+")
        try:
            opsi = int(input("Masukkan pilihan Anda: "))
            if opsi == 1:
                while percobaan > 0:
                    username = input("Masukkan username Anda: ")
                    password = pwinput.pwinput("Masukkan password Anda: ")
                    for user in akun:
                        if username == user["username"] and password == user["password"]:
                            print(Fore.GREEN + "=== Login Berhasil! ===")
                            print("Selamat datang di Kyfood!")
                            if user["status"] == "biasa":
                                menu_biasa(user)
                            else:
                                menu_vip(user)
                            break

                    percobaan -= 1
                    if percobaan > 0:
                        print(Fore.RED + f"Username atau password salah. Sisa percobaan: {percobaan}")
                    else:
                        print(Fore.RED + "Akun Anda diblokir. Silakan hubungi admin untuk membuka kembali.")
                        exit()
            elif opsi == 2:
                print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami.")
                exit()
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except EOFError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except ValueError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")

# Function menu utama bagi member biasa
def menu_biasa(user):
    while True:
        print("+--------------------+")
        print("|     Menu Utama     |")
        print("+--------------------+")
        print("|  1. Order makanan  |")
        print("|  2. Cek Saldo      |")
        print("|  3. Cek Gold       |")
        print("|  4. Cek Voucher    |")
        print("|  5. Logout         |")
        print("+--------------------+")
        try:
            opsi = int(input("Masukkan pilihan anda : "))
            if opsi == 1:
                menu_order(user)
            elif opsi == 2:
                menu_saldo(user)
            elif opsi == 3:
                menu_gold_biasa(user)
            elif opsi == 4:
                cek_voucher()
            elif opsi == 5:
                print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami.")
                exit()
            else:
                print(Fore.RED + "Pilihan tidak ada, silahkan masukan pilihan anda")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except EOFError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except ValueError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")

# Function menu utama bagi member vip
def menu_vip(user):
    while True:
        print("+--------------------+")
        print("|     Menu Utama     |")
        print("+--------------------+")
        print("|  1. Order makanan  |")
        print("|  2. Cek Saldo      |")
        print("|  3. Cek Gold       |")
        print("|  4. Cek Voucher    |")
        print("|  5. Logout         |")
        print("+--------------------+")
        try:
            opsi = int(input("Masukkan pilihan anda : "))
            if opsi == 1:
                menu_order(user)
            elif opsi == 2:
                menu_saldo(user)
            elif opsi == 3:
                menu_gold_vip(user)
            elif opsi == 4:
                cek_voucher()
            elif opsi == 5:
                print(Fore.YELLOW + "Terima kasih telah menggunakan layanan kami.")
                exit()
            else:
                print(Fore.RED + "Pilihan tidak ada, silahkan masukan pilihan anda")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except EOFError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except ValueError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")

# Function untuk order makanan sesuai jam
def menu_order(user):
    jam = datetime.now().hour
    if 6 <= jam <= 10:
        tabel(sarapan)
        transaksi(sarapan,user)
    elif 11 <= jam <= 17:
        tabel(makan_siang)
        transaksi(makan_siang,user)
    elif 18 <= jam < 21:
        tabel(makan_malam)
        transaksi(makan_malam,user)
    else:
        print("+--------------------+")
        print("|     Toko Tutup     |")
        print("+--------------------+")

# Function untuk top up saldo member
def menu_saldo(user):
    while True:
        try:
            print(f"Saldo anda adalah : Rp {user["saldo"]}")
            print("[1] Top Up Saldo")
            print("[2] Kembali")
            opsi = int(input("Masukkan pilihan anda : "))
            if opsi == 1:
                if user["status"] == "biasa":
                    nominal = int(input("Masukkan nominal top up (Rp 10.000 - Rp 2.000.000): Rp "))
                    if 10000 <= nominal <= 2000000:
                        saldo = user["saldo"]
                        total_saldo = saldo + nominal
                        user["saldo"] = total_saldo
                        print(Fore.GREEN + "=== Top Up berhasil ===")
                    else:
                        print(Fore.RED + "Nominal tidak valid")
                else:
                    nominal = int(input("Masukkan nominal top up (Rp 10.000 - Rp 5.000.000): Rp "))
                    if 10000 <= nominal <= 5000000:
                        saldo = user["saldo"]
                        total_saldo = saldo + nominal
                        user["saldo"] = total_saldo
                        print(Fore.GREEN + "=== Top Up berhasil ===")
                    else:
                        print(Fore.RED + "Nominal tidak valid")
            elif opsi == 2:
                break
            else:
                print(Fore.RED + "Pilihan tidak ada")
        except ValueError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except EOFError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")

# Fungsi Cek dan Top-Up Gold untuk member biasa
def menu_gold_biasa(user):
    while True:
        print("+------------------+")
        print("|    Cek Gold      |")
        print("+------------------+")
        print(f"Gold Anda: {user['gold']}")
        print("[1] Top Up Gold")
        print("[2] Kembali")
        try:
            opsi = int(input("Masukkan pilihan Anda: "))
            if opsi == 1:
                top_up_gold(gold_biasa, user)
            elif opsi == 2:
                break
            else:
                print(Fore.RED + "Pilihan tidak ada.")
        except ValueError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except EOFError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")

# Fungsi Cek dan Top-Up Gold untuk member VIP
def menu_gold_vip(user):
    while True:
        print("+------------------+")
        print("|    Cek Gold      |")
        print("+------------------+")
        print(f"Gold Anda: {user['gold']}")
        print("[1] Top Up Gold")
        print("[2] Kembali")
        try:
            opsi = int(input("Masukkan pilihan Anda: "))
            if opsi == 1:
                top_up_gold(gold_vip, user)
            elif opsi == 2:
                break
            else:
                print(Fore.RED + "Pilihan tidak valid.")
        except ValueError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except EOFError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")

# Fungsi untuk Cek voucher
def cek_voucher():
    while True:
        tabel = PrettyTable()
        tabel.field_names = ["Kode voucher", "Jumlah diskon (gold)", "status"]
        for kode in voucher:
            tabel.add_row([kode["kode_voucher"], kode["jumlah_diskon"], kode["status"]])
        print(tabel)
        try:
            opsi = int(input("ketik 0 jika ingin kembali : "))
            if opsi == 0:
                break
            else:
                print(Fore.RED + "Input tidak valid")
        except ValueError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except KeyboardInterrupt:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")
        except EOFError:
            print(Fore.RED + "\nInput tidak valid, silahkan masukan pilihan anda")

login()
