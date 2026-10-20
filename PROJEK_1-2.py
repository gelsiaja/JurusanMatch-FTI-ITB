print("=============================================")
print("   JURUSANMATCH FTI ITB - Rekomendasi Jurusan")
print("=============================================")

# Memilih kelompok TPB.
print("Kamu mahasiswa TPB dari kelompok mana?")
print("1. FTI-SP (Sistem dan Proses)")
print("2. FTI-RI (Rekayasa Industri)")

kelompok = input("Jawaban (1/2): ").strip()

while kelompok not in ["1", "2"]:
    print("Pilihan tidak valid. Ketik 1 untuk FTI-SP atau 2 untuk FTI-RI.")
    kelompok = input("Jawaban (1/2): ").strip()


# =====================================================
# BAGIAN FTI-RI
# =====================================================
if kelompok == "2":
    print("\n=== Tes Minat FTI-RI ===")

    pertanyaan_ri = [
        (
            "Jika diberi kesempatan menyelesaikan masalah di sebuah perusahaan, "
            "mana yang lebih menarik bagimu?",
            "a. Menganalisis proses kerja agar lebih efisien, produktif, dan minim pemborosan.",
            "b. Mengembangkan ide produk atau teknologi baru agar memiliki nilai dan peluang bisnis."
        ),
        (
            "Proyek mana yang paling ingin kamu kerjakan?",
            "a. Merancang sistem produksi dan distribusi agar berjalan optimal.",
            "b. Merancang strategi pengembangan produk inovatif dari ide hingga peluncuran."
        ),
        (
            "Ketika melihat sebuah masalah, apa yang pertama kali ingin kamu lakukan?",
            "a. Mengumpulkan data, mencari akar masalah, dan mengukur kinerja sistem.",
            "b. Mencari peluang, mengeksplorasi ide baru, dan menilai potensi pengembangannya."
        ),
        (
            "Mata kuliah atau topik mana yang lebih menarik bagimu?",
            "a. Optimisasi, riset operasi, ergonomi, dan sistem manufaktur.",
            "b. Manajemen teknologi, inovasi produk, kewirausahaan, dan strategi bisnis."
        ),
        (
            "Kamu diminta membantu perusahaan yang mengalami penurunan kinerja. "
            "Kamu lebih memilih untuk...",
            "a. Memetakan alur kerja dan memperbaiki proses yang tidak efisien.",
            "b. Mengevaluasi peluang inovasi dan merancang strategi pertumbuhan baru."
        ),
        (
            "Dalam sebuah proyek kelompok, peran mana yang paling ingin kamu ambil?",
            "a. Menganalisis data, menyusun model, dan memastikan solusi bekerja secara optimal.",
            "b. Menghubungkan tim teknis dengan kebutuhan pengguna dan tujuan bisnis."
        ),
        (
            "Jika harus memilih topik penelitian, mana yang lebih menarik?",
            "a. Menentukan konfigurasi persediaan dan distribusi terbaik berdasarkan data.",
            "b. Menilai kelayakan pengembangan teknologi baru menjadi produk komersial."
        ),
        (
            "Apa yang paling membuatmu puas setelah menyelesaikan proyek?",
            "a. Menemukan solusi terukur yang membuat suatu sistem bekerja lebih baik.",
            "b. Mewujudkan gagasan baru menjadi inovasi yang bermanfaat dan bernilai."
        ),
        (
            "Perusahaan seperti apa yang paling ingin kamu bantu kembangkan?",
            "a. Perusahaan yang ingin meningkatkan kualitas, efisiensi, dan keandalan operasional.",
            "b. Perusahaan yang ingin menciptakan produk, teknologi, atau model bisnis baru."
        ),
        (
            "Bayangkan kamu memimpin sebuah proyek teknologi. Prioritas utamamu adalah...",
            "a. Memastikan sistem berjalan efektif, sumber daya digunakan optimal, dan hasilnya konsisten.",
            "b. Memastikan inovasi layak dikembangkan, sesuai kebutuhan pasar, dan berkelanjutan secara bisnis."
        )
    ]

    nama_jurusan_ri = ["Teknik Industri", "Manajemen Rekayasa"]
    skor_ri = [0, 0]

    for nomor, data_pertanyaan in enumerate(pertanyaan_ri, start=1):
        teks_pertanyaan, opsi_a, opsi_b = data_pertanyaan

        print("\nPertanyaan", nomor)
        print(teks_pertanyaan)
        print(opsi_a)
        print(opsi_b)

        jawaban = input("Pilih jawaban a atau b: ").lower().strip()

        while jawaban not in ["a", "b"]:
            print("Jawaban tidak valid. Silakan pilih a atau b.")
            jawaban = input("Pilih jawaban a atau b: ").lower().strip()

        if jawaban == "a":
            skor_ri[0] += 1
        else:
            skor_ri[1] += 1

    print("\n=== Hasil Tes Minat FTI-RI ===")
    print(nama_jurusan_ri[0], ":", skor_ri[0])
    print(nama_jurusan_ri[1], ":", skor_ri[1])
    print("\nJurusan dengan kecenderungan minat tertinggi:")

    skor_tertinggi_ri = max(skor_ri)

    if skor_ri[0] == skor_tertinggi_ri:
        print("-", nama_jurusan_ri[0])

    if skor_ri[1] == skor_tertinggi_ri:
        print("-", nama_jurusan_ri[1])


# =====================================================
# BAGIAN FTI-SP
# =====================================================
else:
    print("\n=== Tahap 1: Tes Minat FTI-SP ===")

    pertanyaan_sp = [
        (
            "Jika kamu diberi kesempatan membuat sebuah proyek, mana yang paling menarik bagimu?",
            "a. Membuat proses untuk menghasilkan suatu bahan, seperti sabun atau pupuk.",
            "b. Membuat alat yang dapat mengukur suhu, tekanan, atau energi.",
            "c. Mengembangkan makanan agar lebih awet, aman, dan berkualitas.",
            "d. Mengubah bahan dari tumbuhan menjadi sumber energi atau produk yang bermanfaat."
        ),
        (
            "Pelajaran atau topik mana yang paling ingin kamu pelajari lebih dalam?",
            "a. Reaksi kimia dan cara mengolah bahan menjadi produk.",
            "b. Cara kerja alat, sensor, dan sistem pengendali.",
            "c. Pembuatan pabrik makanan dan produksi makanan dalam skala besar.",
            "d. Energi terbarukan dan pemanfaatan sumber daya alam."
        ),
        (
            "Di antara pelajaran-pelajaran berikut, mana yang paling kamu ungguli?",
            "a. Fisika Mekanika dan Kimia.",
            "b. Fisika II, Matematika, dan Informatika.",
            "c. Kimia dan Biologi.",
            "d. Kimia dan Biologi."
        ),
        (
            "Kamu diminta melakukan penelitian. Topik mana yang paling membuatmu penasaran?",
            "a. Bagaimana suatu reaksi kimia dapat menghasilkan produk dengan lebih efisien?",
            "b. Bagaimana cara kerja sensor untuk mendeteksi perubahan suhu?",
            "c. Apa yang membuat makanan cepat basi dan bagaimana memperlambatnya?",
            "d. Bagaimana bahan pertanian dapat diubah menjadi bahan bakar alternatif?"
        ),
        (
            "Jika bisa bekerja di laboratorium, eksperimen mana yang ingin kamu coba?",
            "a. Menguji reaksi beberapa zat untuk menghasilkan produk tertentu.",
            "b. Mengukur dan menganalisis perubahan suhu atau tekanan menggunakan alat.",
            "c. Menguji pengaruh suhu dan penyimpanan terhadap kualitas makanan.",
            "d. Menguji potensi bahan tumbuhan sebagai sumber energi."
        ),
        (
            "Perusahaan seperti apa yang paling ingin kamu bantu kembangkan?",
            "a. Perusahaan yang memproduksi bahan kimia atau produk industri.",
            "b. Perusahaan yang mengembangkan alat ukur dan teknologi pengendali.",
            "c. Perusahaan yang membuat makanan dan minuman.",
            "d. Perusahaan yang mengembangkan energi terbarukan dari biomassa."
        ),
        (
            "Ketika melihat suatu produk, hal apa yang paling membuatmu penasaran?",
            "a. Bagaimana bahan-bahan penyusunnya bereaksi hingga menjadi produk tersebut.",
            "b. Bagaimana teknologi di dalamnya bekerja dan mengendalikan prosesnya.",
            "c. Bagaimana produk tersebut dibuat agar aman dikonsumsi dan tahan lama.",
            "d. Apakah bahan pembuatnya bisa berasal dari sumber daya alam terbarukan."
        ),
        (
            "Jika kamu harus membuat inovasi untuk masa depan, apa yang ingin kamu kembangkan?",
            "a. Proses produksi yang menghasilkan produk kimia dengan lebih sedikit limbah.",
            "b. Alat pintar yang dapat mengukur dan mengendalikan sistem secara otomatis.",
            "c. Makanan bergizi, aman, dan tetap berkualitas selama penyimpanan.",
            "d. Teknologi yang mengubah limbah pertanian menjadi energi atau bahan bernilai."
        ),
        (
            "Masalah mana yang paling ingin kamu pecahkan?",
            "a. Bagaimana membuat suatu produk melalui proses kimia yang lebih baik?",
            "b. Bagaimana membuat mesin atau sistem bekerja lebih akurat dan efisien?",
            "c. Bagaimana menjaga kualitas dan keamanan makanan yang dikonsumsi masyarakat?",
            "d. Bagaimana memanfaatkan bahan alam untuk mengurangi ketergantungan pada energi fosil?"
        ),
        (
            "Kalau bisa pilih tempat pekerjaan, kira-kira kamu prefer yang mana?",
            "a. Lotte Chemical atau Kilang Pertamina.",
            "b. Pertamina Geothermal, NVIDIA, atau TSMC.",
            "c. Unilever, Indofood, atau Nestle.",
            "d. Pertamina NRE atau Astra Agro."
        )
    ]

    nama_jurusan_sp = [
        "Teknik Kimia",
        "Teknik Fisika",
        "Teknik Pangan",
        "Teknik Bioenergi Kemurgi"
    ]
    skor_sp = [0, 0, 0, 0]

    for nomor, data_pertanyaan in enumerate(pertanyaan_sp, start=1):
        teks_pertanyaan, opsi_a, opsi_b, opsi_c, opsi_d = data_pertanyaan

        print("\nPertanyaan", nomor)
        print(teks_pertanyaan)
        print(opsi_a)
        print(opsi_b)
        print(opsi_c)
        print(opsi_d)

        jawaban = input("Pilih jawaban a, b, c, atau d: ").lower().strip()

        while jawaban not in ["a", "b", "c", "d"]:
            print("Jawaban tidak valid. Silakan pilih a, b, c, atau d.")
            jawaban = input("Pilih jawaban a, b, c, atau d: ").lower().strip()

        indeks_jawaban = "abcd".index(jawaban)
        skor_sp[indeks_jawaban] += 1

    print("\nPeringkat jurusan dari skor tertinggi ke terendah:")

    urutan_jurusan = sorted(
        range(len(skor_sp)),
        key=lambda indeks: skor_sp[indeks],
        reverse=True
    )

    for nomor, indeks in enumerate(urutan_jurusan, start=1):
        print(
            nomor,
            ".",
            nama_jurusan_sp[indeks],
            "-",
            skor_sp[indeks],
            "skor"
        )

    # =====================================================
    # BAGIAN FTI-SP: RASIONALISASI PILIHAN
    # =====================================================
    print("\n=== Tahap 2: Rasionalisasi Pilihan Jurusan ===")
    print("TK = Teknik Kimia")
    print("TF = Teknik Fisika")
    print("PG = Teknik Pangan")
    print("TB = Teknik Bioenergi Kemurgi")

    pilihan = []

    while len(pilihan) < 4:
        nomor_pilihan = len(pilihan) + 1
        jawaban = input("Pilihan " + str(nomor_pilihan) + ": ").upper().strip()

        if jawaban in ["TK", "TF", "PG", "TB"]:
            sudah_dipilih = False
            nomor = 0

            while nomor < len(pilihan):
                if jawaban == pilihan[nomor]:
                    sudah_dipilih = True
                nomor += 1

            if sudah_dipilih == False:
                pilihan.append(jawaban)
            else:
                print("Jurusan itu sudah dipilih. Masukkan jurusan lain.")
        else:
            print("Kode tidak valid. Gunakan TK, TF, PG, atau TB.")

    ip = float(input("IP semester 1: ").replace(",", "."))

    while True:
        jawaban_ganesha = input(
            "Apakah hanya ingin berkuliah di Ganesha? (ya/tidak): "
        ).lower().strip()

        if jawaban_ganesha in ["ya", "y"]:
            harus_ganesha = True
            break
        elif jawaban_ganesha in ["tidak", "t"]:
            harus_ganesha = False
            break
        else:
            print("Jawab dengan ya atau tidak.")

    IPminTF = 2.71
    IPminTK = 3.78
    IPminTB = 2.61

    hasil = []

    posisi_tb = 0
    posisi_pg = 0
    nomor = 0

    while nomor < 4:
        if pilihan[nomor] == "TB":
            posisi_tb = nomor
        elif pilihan[nomor] == "PG":
            posisi_pg = nomor
        nomor += 1

    if posisi_tb < posisi_pg:
        tb_di_atas_pg = True
    else:
        tb_di_atas_pg = False

    if pilihan[0] == "TK":
        if ip > IPminTK:
            if harus_ganesha == True:
                hasil.append("TK")
                hasil.append("TF")

                nomor = 0
                while nomor < 4:
                    if pilihan[nomor] != "TK" and pilihan[nomor] != "TF":
                        hasil.append(pilihan[nomor])
                    nomor += 1
            else:
                hasil = pilihan.copy()

        elif ip < IPminTK and ip > IPminTF:
            if harus_ganesha == True:
                hasil.append("TK")
                hasil.append("TF")

                nomor = 0
                while nomor < 4:
                    if pilihan[nomor] != "TK" and pilihan[nomor] != "TF":
                        hasil.append(pilihan[nomor])
                    nomor += 1
            else:
                hasil = pilihan.copy()

        elif ip < IPminTF:
            if tb_di_atas_pg == True:
                hasil = ["TB", "TF", "PG", "TK"]
            else:
                nomor = 0
                while nomor < 4:
                    if pilihan[nomor] != "TK":
                        hasil.append(pilihan[nomor])
                    nomor += 1
                hasil.append("TK")
        else:
            hasil = pilihan.copy()

    elif pilihan[0] == "TF":
        if ip > IPminTF:
            hasil = pilihan.copy()

        elif ip < IPminTF:
            if tb_di_atas_pg == True:
                if ip > IPminTB:
                    hasil.append("TF")
                    hasil.append("TB")

                    nomor = 0
                    while nomor < 4:
                        if pilihan[nomor] != "TF" and pilihan[nomor] != "TB":
                            hasil.append(pilihan[nomor])
                        nomor += 1

                elif ip < IPminTB:
                    hasil.append("TB")
                    hasil.append("TF")

                    nomor = 0
                    while nomor < 4:
                        if pilihan[nomor] != "TF" and pilihan[nomor] != "TB":
                            hasil.append(pilihan[nomor])
                        nomor += 1
                else:
                    hasil = pilihan.copy()
            else:
                hasil.append("TF")

                nomor = 0
                while nomor < 4:
                    if pilihan[nomor] != "TF" and pilihan[nomor] != "TK":
                        hasil.append(pilihan[nomor])
                    nomor += 1

                hasil.append("TK")
        else:
            hasil = pilihan.copy()

    else:
        hasil = pilihan.copy()

    print("\n=== Hasil Rekomendasi ===")
    print("IP semester 1:", ip)

    if harus_ganesha == True:
        print("Hanya ingin Ganesha: Ya")
    else:
        print("Hanya ingin Ganesha: Tidak")

    nomor = 0

    while nomor < 4:
        kode = hasil[nomor]

        if kode == "TK":
            print("Pilihan", nomor + 1, ": TK - Teknik Kimia")
        elif kode == "TF":
            print("Pilihan", nomor + 1, ": TF - Teknik Fisika")
        elif kode == "PG":
            print("Pilihan", nomor + 1, ": PG - Teknik Pangan")
        else:
            print("Pilihan", nomor + 1, ": TB - Teknik Bioenergi Kemurgi")

        nomor += 1