# 🩺 TSISTEM PAKAR THT 

Sebuah aplikasi Sistem Pakar berbasis GUI (Graphical User Interface) untuk mendiagnosis penyakit pada Telinga, Hidung, dan Tenggorokan (THT). Aplikasi ini menggunakan metode **Forward Chaining** dan perhitungan **Certainty Factor** sederhana untuk memberikan persentase tingkat kecocokan penyakit berdasarkan gejala yang dipilih oleh pengguna.

Edisi ini dirancang dengan antarmuka bergaya **Dark Terminal / Medical Cyberpunk**, dengan tata letak visual 180 derajat (panel hasil di sebelah kiri dan input gejala di sebelah kanan) untuk memberikan pengalaman layaknya menggunakan sistem medis futuristik.

---

## ✨ Fitur Utama

* **Mesin Inferensi Berbasis Aturan**: Menggunakan metode *Forward Chaining* untuk mencocokkan gejala dengan basis pengetahuan yang berisi 23 penyakit THT dan 37 gejala.
* **Sistem Skoring (Certainty Factor Terkomputasi)**: Menghitung skor probabilitas berdasarkan *Coverage* (seberapa banyak aturan gejala terpenuhi) dan *Precision* (seberapa relevan input gejala terhadap penyakit).
* **Terminal UI / Dark Mode**: Tema gelap pekat dengan aksen *Neon Cyan* dan *Pink*, lengkap dengan representasi visual *ASCII Progress Bar*.
* **Pencarian Gejala Cepat**: Terdapat fitur *search bar* bergaya CLI untuk memfilter gejala dengan cepat secara *real-time*.
* **Top-5 Diagnosis**: Menampilkan 5 kemungkinan penyakit tertinggi secara otomatis dengan indikator *Primary Match* dan *Alternative*.

---

## 🧠 Bedah Kode & Arsitektur Sistem

Sistem ini dirancang menggunakan paradigma pemrograman berorientasi objek (OOP) untuk antarmuka pengguna (GUI), dan pemrograman prosedural untuk logika inferensinya. Berikut adalah rincian arsitektur sistem:

### 1. Basis Pengetahuan (Knowledge Base)
Struktur data statis yang bertindak sebagai "memori kepakaran" dari sistem.
* **`GEJALA` (Kamus/Dictionary)**: Menyimpan 37 gejala. Disusun menggunakan *Key* (misal: "G1") sebagai ID unik agar pemrosesan data akurat, dan *Value* (misal: "Nafas abnormal") untuk tampilan UI.
* **`PENYAKIT` (List of Dictionaries)**: Berisi daftar 23 penyakit. Setiap item menyimpan `"nama"` penyakit dan `"gejala"` yang berisi *list* ID gejala yang menjadi aturan bersyarat (berlogika AND) agar penyakit tersebut terdiagnosis.

### 2. Mesin Inferensi (Fungsi `inferensi`)
Jantung dari sistem pakar ini. Fungsi `inferensi(gejala_dipilih)` menerima *list* kode gejala dari pengguna dan memprosesnya melalui alur berikut:
1. **Pencocokan Iteratif**: Melakukan *looping* ke seluruh basis pengetahuan `PENYAKIT`.
2. **List Comprehension (Irisan)**: Mengecek irisan gejala wajib penyakit dengan gejala yang dipilih pengguna `[g for g in p["gejala"] if g in gejala_dipilih]`.
3. **Perhitungan Skor Probabilitas**:
   * **Coverage (Bobot 60%)**: Menghitung seberapa banyak syarat penyakit ini yang terpenuhi (`jumlah gejala cocok / total gejala penyakit`).
   * **Precision (Bobot 40%)**: Menghitung relevansi input (`jumlah gejala cocok / total keluhan user`). Mencegah sistem memberi skor tinggi jika user menginputkan terlalu banyak gejala yang tidak relevan.
4. **Sorting & Slicing**: Mengurutkan penyakit berdasarkan skor tertinggi dan mengembalikan 5 kandidat utama (*Top-5*).

### 3. Antarmuka GUI (Class `SistemPakarTHT`)
Dibangun menggunakan library standar `tkinter` dengan tata letak 180 derajat (Kiri: Hasil, Kanan: Input).
* **State Management**: Menggunakan `tk.BooleanVar()` yang di-*bind* ke setiap *checkbox*. Perubahan status centang akan otomatis tercatat.
* **Filter Dinamis**: Memanfaatkan `trace_add("write", ...)` pada kolom pencarian untuk memanggil fungsi *render* ulang gejala secara otomatis setiap kali ada ketikan.
* **Scrollable Area**: Diimplementasikan dengan meletakkan `tk.Frame` di dalam `tk.Canvas` yang diikat dengan `ttk.Scrollbar`, karena `tkinter` tidak memiliki *scroll* bawaan untuk Frame.
* **ASCII Progress Bar**: Visualisasi skor di-*render* secara manual menggunakan karakter blok (`█` dan `░`) untuk menguatkan nuansa terminal/hacker.

---

## 🛠️ Persyaratan Sistem

Aplikasi ini dibangun murni menggunakan pustaka bawaan Python, sehingga tidak memerlukan instalasi *library* eksternal melalui `pip`.

* **Python 3.x** atau yang lebih baru.
* **Tkinter** (Sudah terpasang secara *default* pada instalasi Python standar di OS Windows dan macOS. Untuk pengguna Linux, mungkin memerlukan instalasi tambahan seperti `sudo apt install python3-tk`).

---

## 🚀 Cara Menjalankan Aplikasi

1. Pastikan Python 3 sudah terinstal di komputer/laptop Anda.
2. Unduh atau salin kode program utama ke dalam sebuah file dengan ekstensi `.py` (misalnya: `tht_sys.py`).
3. Buka **Terminal** atau **Command Prompt**.
4. Navigasikan ke dalam direktori tempat file `tht_sys.py` tersebut disimpan.
5. Jalankan perintah eksekusi berikut:
   ```bash
   python tht_sys.py
