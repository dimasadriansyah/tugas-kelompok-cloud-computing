import threading  # Mengimpor modul threading untuk mengelola eksekusi thread bersamaan

def partial_sum(start, end, result_list, index):
    """
    Function untuk menghitung jumlah total angka dalam rentang [start, end].
    Hasil perhitungan disimpan ke dalam result_list pada posisi 'index'.
    """
    total = 0  # Inisialisasi variabel total lokal untuk menyimpan hasil penjumlahan sementara
    for i in range(start, end + 1):  # Melakukan iterasi dari angka start hingga end (inclusive)
        total += i  # Menambahkan nilai i ke total sementara
    result_list[index] = total  # Menyimpan hasil akhir perhitungan bagian ini ke dalam list hasil

def main():
    """
    Function utama untuk menerima input dari pengguna dan mengatur pembagian tugas thread.
    """
    print("=== Program Penjumlahan Angka Terdistribusi dengan Thread ===")  # Menampilkan judul program
    
    # Meminta input dari pengguna secara dinamis
    start_num = int(input("Input angka awal: "))  # Meminta input angka awal dan mengubahnya ke integer
    end_num = int(input("Input angka akhir: "))  # Meminta input angka akhir dan mengubahnya ke integer
    num_threads = int(input("Thread yang digunakan (min 2): "))  # Meminta jumlah thread yang diinginkan
    
    # Validasi input minimal thread
    if num_threads < 2:  # Memeriksa apakah jumlah thread kurang dari 2
        print("Jumlah thread minimal adalah 2! Mengubah jumlah thread menjadi 2.")  # Pesan pemberitahuan
        num_threads = 2  # Mengatur ulang jumlah thread menjadi 2 jika input di bawah batas minimal
        
    # Validasi rentang angka
    if start_num > end_num:  # Memeriksa jika angka awal lebih besar dari angka akhir
        print("Error: Angka awal harus lebih kecil atau sama dengan angka akhir.")  # Menampilkan pesan error
        return  # Menghentikan eksekusi function jika rentang tidak valid
        
    total_numbers = end_num - start_num + 1  # Menghitung jumlah total bilangan yang akan dijumlahkan
    chunk_size = total_numbers // num_threads  # Menentukan berapa banyak angka yang ditangani setiap thread
    remainder = total_numbers % num_threads  # Menentukan sisa pembagian angka jika tidak habis dibagi
    
    threads = []  # Menyiapkan list kosong untuk menampung objek thread
    results = [0] * num_threads  # Menyiapkan list penampung hasil sementara dengan nilai awal 0
    
    current_start = start_num  # Menentukan batas awal perhitungan untuk thread pertama
    
    # Membuat dan mengonfigurasi setiap thread secara dinamis
    for i in range(num_threads):  # Iterasi sebanyak jumlah thread yang ditentukan
        # Menentukan rentang akhir untuk thread saat ini (membagi sisa angka ke thread awal jika ada)
        current_end = current_start + chunk_size - 1 + (1 if i < remainder else 0)
        
        # Mengatasi kasus jika range angka lebih kecil dari jumlah thread yang diminta
        if current_start > end_num:  
            break  # Berhenti membuat thread tambahan jika semua angka sudah tercover
            
        # Membuat objek thread baru dengan menargetkan function partial_sum dan argumen rentangnya
        t = threading.Thread(target=partial_sum, args=(current_start, current_end, results, i))
        threads.append(t)  # Menambahkan objek thread ke dalam list threads
        t.start()  # Memulai eksekusi thread
        
        current_start = current_end + 1  # Menggeser titik awal angka untuk thread berikutnya
        
    # Menunggu seluruh thread selesai dieksekusi
    for t in threads:  # Iterasi melalui setiap thread yang ada di list
        t.join()  # Memblokir alur utama sampai thread t selesai berjalan
        
    final_sum = sum(results)  # Menjumlahkan seluruh hasil parsial dari tiap thread
    print(f"\nHasil penjumlahan: {final_sum}")  # Menampilkan hasil akhir penjumlahan ke layar

if __name__ == "__main__":  # Memeriksa apakah berkas dijalankan langsung sebagai script utama
    main()  # Memanggil function utama untuk menjalankan program