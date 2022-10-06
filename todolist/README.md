## App Django: To-Do List
http://tokotristan.herokuapp.com/todolist/

## TUGAS 5

1. **Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**

    1. Inline CSS, adalah sebutan ketika pengaplikasian style dilakukan pada elemen tertentu saja. Kelebihan dari Inline CSS adalah sangat berguna ketika sedang menguji perubahan dari pengaplikasian style tertentu, solusi quick fix untuk permasalahan spesifik, dan juga http request yang lebih kecil. Kekurangan dari inline css adalah perubahan css hanya berlaku untuk satu elemen saja
    2. Internal CSS, adalah sebutan ketika kode css internal ditempatkan di bagian head dari sebuah halaman html. Kelebihan dari Internal CSS adalah class dan ID dapat digunakan untuk seluruh internal stylesheet, dan hanya membutuhkan satu file html itu sendiri. Kekurangan dari Internal CSS adalah perubahan yang dilakukan hanya berlaku untuk 1 file html itu sendiri.
    3. External CSS, adalah sebutan ketika semua kode rule css ditempatkan dalam file.css eksternal dari page. Kelebihan dari External CSS adalah ketika css didownload dan dipanggil akan lebih cepat karena pemanggilan hanya satu kali pada external CSS, dan perubahan bisa berlaku ke semua file yang mengaplikasikan file .css tersebut. Kekurangan dari CSS Eksternal adalah halaman tidak langsung menjadi bentuk sempurna ketika di load hingga loading css selesai.

2. **Jelaskan tag HTML5 yang kamu ketahui**

    1. Tag input yang merupakan fitur dari forms 2.0 pada HTML 5 mempermudah meminta input dari user
    2. Tag header footer dan section yang merupakan elemen semantic baru yang mempermudah mendefinisikan elemen heade, footer dan section
    3. Tag Audio dan Video yang memungkinkan page menampilkan Video dan Audio
    4. Tag Drag and Drop yang memungkinkan user melakukan drag and drop file pada web page

3. **Jelaskan tipe-tipe CSS selector yang kamu ketahui**
    1. element - memilih semua p elements
    2. element.class - memilih semua p elements dengan class tertentu
    3. :default - memilih setiap default input element
    4. :disabled - memilih setiap disabled input element
    5. :enabled - memilih setiap enabled input element
    6. :hover - memilih link saat mouse hover diatasnya

4. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas**
    1. Menaruh link bootstrap dan css yang saya butuhkan pada base.html agar bootstrap dapat diterapkan pada seluruh halaman html pada templates
    2. Mengubah login page menjadi menggunakan card agar tampilan page menjadi responsive
    3. Mengimpelementasikan card pada register page agar tampilan register page juga responsive
    4. Menambahkan Navbar pada laman utama todolist, dan juga mengisinya dengan link menuju create task dan juga memindahkan button logout ke navbar
    5. Mengubah tampilan task list yang sebelumya menggunakan table menjadi card agar tampilan web menjadi responsive
    6. Mengubah bentuk halaman page create-task menjadi cards agar tampilan lebih bagus dan responsive
    7. Melakukan deployment dan pengecekan webpage pada mobile agar dapat memastikan tampilan webpage menyeseuaikan dengan baik

## TUGAS 4

1. **Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**
csrf_token adalah value yang dibuat oleh server-side application untuk melindungi CSRF resource yang rentan. Value token tersebut digenerate secara random menggunakan pseudo-random number generator. Untuk sebuah request diterima oleh server, kedua token yang digenerate pada user-session dan server side harus sama. Jika kedua token tidak sama, user-session akan dihentikan dan event yang ada akan dimasukkan ke log sebagai potensi serangan csrf. 

2. **Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.**
Kita dapat membuat elemen form secara manual dengan menggunakan deklararasi method POST dibagian atas page HTML-nya. Lalu untuk table,label, dan inputnya dimasukan secara manual didalam page htmlnya.

3. **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**
    1. Display form kosong ditampilkan kepada user
    2. Form tersebut dapat berisi default initial values atau tidak. Pada saat ini data masih unbound karena masih belum masuk ke database yang dimasukkan user
    3. Setelah data dimasukkan dan button submit ditekan, Jika data belum sesuai lanjut ke nomor 6, jika sudah sesuai langsung ke nomor 7
    4. Jika data belum sesuai, form sudah melakukan binding terhadap data yang sebelumnya dimasukan sehingga user tidak perlu memasukan ulang data yang telah dimasukkan sebelumnya. Kembali ke nomor 3.
    5. Jika data valid, akan dilakukan cleaning terhadap data dari karakter yang invalid pada datatype python mengecek apakah data masih valid pada models yang telah diterapkan, jika data belum valid kembali ke nomor 3. Jika sudah lanjut ke nomor 6.
    6. Jika data sudah valid, data tersebut dapat selanjutnya dilakukan processing yang diperlukan. Pada konteks tugas ini, data disimpan kedalam database yang sudah tersedia.
    7. Setelah itu, user di redirect ke page tertentu, pada tugas ini dikembalikan kepada page /todolist/

4. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
    1. Buat aplikasi baru bernama todolist menggunakan commandline cmd. Setelah itu app baru tersebut didaftarkan pada settings.py yang terdapat pada folder project_django
    2. Menambahkan fungsi show_todolist pada views.py lalu mendaftarkan path pada urls.py yang terdapat pada project_django untuk mendaftarkan url /todolist/ sebagai path valid
    3. Menambahkan models-models yang diperlukan yaitu user, date, title, dan description. Setelah semua models dibuat
    4. Membuat sebuah register-page untuk app todolist, stepnya adalah sebagai berikut
        1. Membuat sebuah fungsi register() pada views.py yang berfungsi untuk membuat form register user baru lalu mengarahkan user ke register page
        2. Membuat sebuah template register.html untuk menempatkan form yang ada
        3. Menambahkan path yang ada kedalam urls.py yang dibuat didalam folder todolist yang memanggil fungsi register
    5. Membuat sebuah login-page yang stepnya adalah sebagai berikut
        1. Membuat sebuah fungsi login_user() pada views.py yang berfungsi untuk membuat form login user baru lalu mengarahkan user ke login_page page
        2. Membuat sebuah template login.html untuk menempatkan form yang ada
        3. Menambahkan path /login/ kedalam urls.py pada folder todolist yang memanggil fungsi login_user
    6. Membuat sebuah fitur logout yang stepnya adalah sebagai berikut
        1. Membuat sebuah fungsi logout() pada views.py yang berfungsi untuk memberikan request untuk melogout user yang sedang aktif
        2. Membuat sebuah button logout pada todolist.html. Button tersebut akan memanggil path logout
        3. Menambahkan path /logout/ kedalam urls.py pada folder todolist yyang memanggil fungsi logout_user
    7. Membuat form untuk fitur membuat task baru, prosesnya adalah sebagai berikut:
        1. Membuat forms.py yang didalamnya terdapat class TaskList yang berisikan atribut yang harus ditampilkan pada form pembuatan task. Attribut yang perlu dibuatkan form adalah title dan description
        2. Membuat sebuah fungsi create_task pada views.py yang didalamnya terdapat pemrosesan template forms.py kedalam template html
        3. Membuat sebuah file html bernama create-task.html yang memanggil template form yang dibuat pada file forms.py
        4. Membuat routing dari fungsi create_task() pada views.py untuk menampilkan form pada file create-task.html
        5. Menambahkan fungsi untuk memproses input dari form yang diisi user pada fungsi create_task. fungsi tersebut menambahkan cleaned data dari form yang sudah valid kedalam objects pada models. Setelah itu user diredirect ke mainpage /todolist/
    8. Membuat tampilan mainpage todolist dengan membuat file todolist.html yang berisi tabel task hasil input user, tombol untuk mengakses form create_task, dan juga informasi last login.
    9. Menambahkan fitur bonus yaitu button untuk mengubah status task dari tampilan mainpage dengan cara:
        1. Menambahkan sebuah model boolean isFinished pada models.py untuk flag status selesai atau belum
        2. Menambahkan sebuah fungsi change_status() pada views.py untuk melakukan perubahan status pada model isFinished pada data aktif
        3. Menambahkan conditional pada todolist.html terhadap models isFinished pada data terkait, untuk menampilkan pesan sesuai status isFinished
        4. Menambahkan sebuah routing untuk memanggil fungsi change_status() dari mainpage todolist.html
        5. Membuat sebuah button "switch" pada mainpage disamping data yang terkait untuk memanggil routing yang ditambahkan sebelumnya
        6. Melakukan redirecting kembali kepada page todolist agar halaman html direfresh
    10.  Menambahkan fitur bonus yaitu button untuk menghapus task yang ada dengan cara:
        1. Menambahkan sebuah fungsi delete_task() pada views.py 
        2. Memanggil data yang sesuai dengan id yang dipanggil lalu memanggil fungsi delete() untuk menambahkan query untuk menghapus data terkaut
        3. Menambahkan sebuah routing untuk memanggil fungsi delete_task() dari button mainpage todolist.html
        4. Membuat sebuah button "delete" pada mainpage disamping data yang terkait untuk memanggil routing yang ditambahkan sebelumnya
        5. Melakukan redirecting kembali kepada page todolist agar halaman html direfresh
    11. Melakukan deployment dengan push repository yang telah selesai
    12. Menambahkan dua dummy data untuk contoh task yang sudah ada:\
    #1\
    Username: dummyaccount\
    Password: qweasd121\
    #2\
    Username: dummyaccount2\
    Password: qweasd121