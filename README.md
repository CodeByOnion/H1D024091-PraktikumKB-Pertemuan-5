# 🩺 THT_SYS // Terminal Diagnosis System v1.0

Sebuah aplikasi Sistem Pakar berbasis GUI (Graphical User Interface) untuk mendiagnosis penyakit pada Telinga, Hidung, dan Tenggorokan (THT). Aplikasi ini menggunakan metode **Forward Chaining** dan perhitungan **Certainty Factor** sederhana untuk memberikan persentase tingkat kecocokan penyakit berdasarkan gejala yang dipilih oleh pengguna.

Edisi ini dirancang dengan antarmuka bergaya **Dark Terminal / Medical Cyberpunk**, dengan tata letak visual 180 derajat (panel hasil di sebelah kiri dan input gejala di sebelah kanan) untuk memberikan pengalaman layaknya menggunakan sistem medis futuristik.

---

## ✨ Fitur Utama

* **Mesin Inferensi Berbasis Aturan**: Menggunakan metode *Forward Chaining* untuk mencocokkan gejala dengan basis pengetahuan yang berisi 23 penyakit THT dan 37 gejala.
* **Sistem Skoring (Certainty Factor Terkomputasi)**: Menghitung skor probabilitas berdasarkan *Coverage* (seberapa banyak aturan gejala terpenuhi) dan *Precision* (seberapa relevan input gejala terhadap penyakit).
* **Terminal UI / Dark Mode**: Tema gelap pekat dengan aksen *Neon Cyan* dan *Pink*, lengkap dengan representasi visual *ASCII Progress Bar*.
* **Pencarian Gejala Cepat**: Terdapat fitur *search bar* bergaya CLI untuk memfilter gejala dengan cepat.
* **Top-5 Diagnosis**: Menampilkan 5 kemungkinan penyakit tertinggi secara otomatis dengan indikator *Primary Match* dan *Alternative*.

---

## 🛠️ Persyaratan Sistem

Aplikasi ini dibangun murni menggunakan pustaka standar Python, sehingga tidak memerlukan instalasi *library* eksternal pihak ketiga (seperti `pip install`).

* **Python 3.x** atau yang lebih baru.
* **Tkinter** (Sudah terpasang secara *default* pada instalasi Python standar di Windows/macOS. Untuk pengguna Linux, mungkin perlu menginstal `python3-tk`).

---

## 🚀 Cara Menjalankan Aplikasi

1. Pastikan Python sudah terinstal di komputer Anda.
2. Simpan kode sumber ke dalam sebuah file, misalnya `tht_sys.py`.
3. Buka Terminal atau Command Prompt.
4. Navigasikan ke direktori tempat file tersebut disimpan.
5. Jalankan perintah berikut:

   ```bash
   python tht_sys.py
