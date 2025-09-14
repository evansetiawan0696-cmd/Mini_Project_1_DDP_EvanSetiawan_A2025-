#profil
print("-" * 20)
print("nama : Evan_Setiawan")
print("NIM : 2509116036")
print("Kelas : Sisfor A 2025")
print("tugas : minpro 1")
print("-" * 20)

print()
print()

# Sistem pendaftaran pasien pada Klinik UNMUL
print("=" * 30)
print("selamat datang di Klinik UNMUL")
print("=" * 30)


# Program looping
while True:
    # Opsi jika pernah/belum berobat di klinik unmul
    print("-" * 40)
    apakah_pernah_berobat = input("Apakah sudah pernah berobat di sini? (iya/tidak/keluar): ")
    
    # opsi keluar
    if apakah_pernah_berobat == "keluar":
        print("=" * 40)
        print("Terima kasih telah menggunakan layanan Klinik UNMUL.")
        print("=" * 40)
        break
    
    # Pasien baru
    if apakah_pernah_berobat == "tidak":
        print("silahkan mendaftarkan data diri anda dahulu")
        # create data pasien baru
        data_pasien = []
        
        # Input data pasien
        nama = input("masukkan nama : ")
        umur = input("berapa umur anda: ")
        gender = input("jenis kelamin: ")
        alamat = input("alamat : ")
        TTL = input("tempat, tanggal lahir: ")
        
        # memasukkan input kedalam data
        data_pasien.append(nama)
        data_pasien.append(umur)
        data_pasien.append(gender)
        data_pasien.append(alamat)
        data_pasien.append(TTL)
        
        print("data pasien", data_pasien)
        
        # Read Validasi data
        while True:
            print("-" * 20)
            apakah_data_valid = input("Apakah data sudah benar? (iya/tidak): ")
            
            if apakah_data_valid == "iya":
                print("data berhasil disimpan")
                break
            elif apakah_data_valid == "tidak":
                print("Data akan dihapus. Silakan isi ulang data Anda.")
                # Input ulang data
                data_pasien = []
                nama = input("masukkan nama : ")
                umur = input("berapa umur anda: ")
                gender = input("jenis kelamin: ")
                alamat = input("alamat : ")
                TTL = input("tempat, tanggal lahir: ")
                
                # memasukkan input kedalam data
                data_pasien.append(nama)
                data_pasien.append(umur)
                data_pasien.append(gender)
                data_pasien.append(alamat)
                data_pasien.append(TTL)
                print("data pasien", data_pasien)
            else:
                print("Pilihan tidak valid. Silakan pilih 'iya' atau 'tidak'.")
    
    # Pasien lama
    elif apakah_pernah_berobat == "iya":
        print("-" * 40)
        print()
        print("status : pasien lama")
        print()
    else:
        print("Pilihan tidak valid. Silakan pilih 'iya', 'tidak', atau 'keluar'.")
        continue
    
    # Pemilihan poli dan keluhan (untuk kedua jenis pasien)
    print("silahkan memilih poli: ")
    
    print()
    PILIHAN_POLI = ("poli umum", "poli lansia", "poli anak", "poli gigi")
    print("-" * 40)
    print(PILIHAN_POLI)
    print("-" * 40)
    print()
    
    pilihan_poli = input("pilih poli: ")
    keluhan = input("keluhan yang anda rasakan: ")
    
    # Rincian pendaftaran
    print("=" * 40)
    print("rincian pendaftaran")
    print("=" * 40)
    print()
    print("-" * 40)
    
    if apakah_pernah_berobat == "tidak":
        print("status: pasien baru")
    else:
        print("status: pasien lama")
    
    print("pilihan poli:", pilihan_poli)
    print("keluhan:", keluhan)
    print("-" * 40)
    print()
    print("silahkan menunggu panggilan, terimakasih")
    print("terimakasih, lekas sembuh")
    
    # Konfirmasi ingin berobat lagi
    print("-" * 40)
    berobat_lagi = input("Apakah anda ingin berobat lagi? (iya/tidak): ")
    
    if berobat_lagi == "tidak":
        print("=" * 40)
        print("Terima kasih telah menggunakan layanan Klinik UNMUL.")
        print("=" * 40)
        break
    print()