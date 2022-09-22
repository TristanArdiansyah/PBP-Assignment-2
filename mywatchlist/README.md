## App Django: Mywatchlist

1. Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON dan XML merupakan platform yang dapat digunakan untuk menyimpan data-data dari sebuah website. Perbedaan antara JSON dan XML adalah JSON merupakan format data-interchange yang ringan dan independen dari bahasa pemrograman lain. Selain itu JSON dibangun berdasarkan Javascript Language yang mudah dimengerti dan dibuat. Sedangkan XML didesain untuk menyimpan data namun kurang baik dalam menampilkannya. Struktur XML dibuat semudah dibaca mungkin baik itu oleh mesin ataupun manusia.
HTML merupakan hypertext markup language, dan html merupakan design page yang akan dilihat oleh viewer. HTML tidak dapat digunakan untuk menyimpan data
2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita membutuhkan data delivery agar data yang ditampilkan pada website dapat selalu disesuaikan secara dinamis dengan database yang dimiliki. Dengan demikian, informasi yang terdapat pada website selalu dapat disesuaikan hanya dengan merubah database yang disimpan,
3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. Pertama-tama saya membuat app baru bernama "mywatchlist"
    2. lalu saya menambahkan app "mywatchlist" di settings.py pada folder project_django
    3. Setelah itu saya menambahkan routing baru pada urls.py yang terdapat dalam folder project_django
    4. Setelah itu saya menambahkan attribut-attribut yangh saya butuhkan pada models.py
    5. Lalu saya membuat folder fixtures yang selanjutnya saya isikan dengan file json yang berisi database saya
    6. Setelah semua data saya masukan kedalam database tersebut, saya lakukan command untuk makemigrations, migrate, dan juga loaddata kedalam websaya
    7. Lalu saya buat folder templates yang berisi template html dari web saya dan saya lakukan pemanggilan kepada data yang saya miliki di file json saya
    8. Setelah hal tersebut selesai saya buat routing dalam file views.py, agar terdapat 3 path website, yaitu tampilan dalam html dan tampilan dalam bentuk raw data json/xml
    9. Setelah itu saya buat unit test pada tests.py untuk melakukan pengecekan pada seluruh routing saya apakah semua nya sudah dapat mengembalikan HTML 200 OK
    10. Terakhir untuk implementasi bonus saya melakukan iterasi pada function show_mywatchlist pada views tepatnya pada variable pemanggilan data untuk menghitung seberapa banyak movie yang sudah diwatch dan total movienya, lalu saya kurangi untuk melakukan perbandingan pada if conditios. Jika pada if conditions, movie yang telah ditonton lebih banyak, message awal saya ubah.
    11. Setelah itu saya mengisi README.md dan melakukan deployment ke github
4. Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md
![Gambar]('../../Postman/HTML.png?raw=true')
![Gambar]('../../Postman/JSON.png?raw=true')
![Gambar]('../../Postman/XML.png?raw=true')