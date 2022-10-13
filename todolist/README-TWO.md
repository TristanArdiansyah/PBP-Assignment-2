# App Django: To-Do List
http://tokotristan.herokuapp.com/todolist/

## TUGAS 6: Javascript dan AJAX

1. **Jelaskan perbedaan antara asynchronous programming dengan synchronous programming**
Perbedaan utama antara asyncrhonus programming dengan synchronus programming terletak pada metodenya.

Asychronus programming merupakan metode pemrograman dimana program dapat menjalankan beberapa tugas/fungsi secara bersamaan. Hal tersebut dapat dilakukan karena asynchronous programming merupakan multithreaded model dengan non-blocking architecture. Dengan begitu, sebuah function asynchronus dipanggil, baris code selanjutnya tetap dapat dijalankan tanpa perlu menunggu function sebelumnya selesai dijalankan.

Synchronus programming merupakan metode pemrograman dimana program menjalankan tugas/fungsi secara berurutan (sequential). Hal tersebut dapat dilakukan karena asynchronous programming merupakan singlethreaded model sehingga hanya 1 task yang dikerjakan dalam satu waktu. Ketika sebuah task/function dijalankan, instruksi untuk menjalankan task lainnya tidak dapat dijalankan. Akibatnya, program harus task/function tersebut selesai terlebih dahulu sebelum menjalankan task/function berikutnya.


2. **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini**

Event Driven Programming paradigm merupakan paradigma pemrograman dimana program akan mengeksekusi sesuatu berdasarkan event yang terjadi. Flow dari paradigma ini sangat dipengaruhi oleh event yang dilakukan user sehingga flow dari program seringkali tidak dapat dilakukan secara asychronous. Implementasinya pada tugas ini adalah pada pemanggilan modal untuk <code>Create Task</code> dan submisi Todolist baru pada modal tersebut. Program hanya akan menjalankan fungsi <code>document.getElementById("submit_btn").onclick = addTodoList</code> untuk membuat task ketika button <code>Buat todolist</code> dipanggil.

3. **Jelaskan penerapan asynchronous programming pada AJAX**

Implemetnasi asynchronous pada AJAX dapat dilihat pada penerapan refresh page ketika Todo baru dibuat. Setiap kali button <code>Buat Todolist</code> ditekan, program akan secara assynchronous melakukan iterasi terhadap seluruh data pada database lalu merefresh tampilan todolist tanpa harus melakukan reload terhadap page itu sendiri. 

4. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas**
    1. Menambahkan CDN dari AJAX pada head di <code>todolist.html</code> agar AJAX dapat diimplementasikan pada html tersebut.
    2. Menambahkan dua function pada views.py yaitu <code>show_json</code> untuk mengembalikan halaman page yang berisi raw json database, dan juga <code>add_todolist_item</code> yaitu fungsi yang mengambil data dari form lalu menambahkannya ke database pengguna yang sedang login
    3. Membuat routing pada urls.py untuk memanggil kedua fungsi baru tersebut
    4. Membuat sebuah modal pada <code>todolist.html</code> untuk memberikan form yang harus diisi user untuk menambahkan todolist baru
    5. Mengubah routing button untuk create task menuju modal yang sebelumnya dibuat
    6. Menerapkan asynchronous refresh untuk database user logged ini menggunakan AJAX. 
    7. Melakukan deployment dan pengetesan kepada seluruh fitur baru yang dibuat