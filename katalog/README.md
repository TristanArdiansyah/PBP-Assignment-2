## App Django: Katalog
http://tokotristan.herokuapp.com/katalog/

1. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html**

![Gambar]('../../BaganReqClientMVT_NandaTristanArdiansyah_2106752086.png?raw=true')

2. **Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?** 

    Virtual environment digunakan untuk mengisolasi package dari dependencies lokal. Hal tersebut dilakukan untuk mencegah terjadinya tabrakan dengan versi lain yang terdapat pada komputer lokal. Dengan demikian, dependencies yang diinstall selalu uptodate dan tidak bergantung pada versi yang terinstall di local computer. 

    Sebenarnya untuk membuat aplikasi berbasis django tidak wajib untuk menggunakan virtual environment. Namun, hal tersebut adalah best practice untuk mencegah hal-hal yang dapat mengganggu saat melakukan development. Selain itu, dengan virtual environment kita dapat memastikan dependencies yang diinstall di computer lokal ataupun computer server akan selalu sama dan tidak ada library lain yang mungkin dapat mengganggu jalannya web Django kita.

2. **Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

    1. Pertama tama tentunya saya harus melakukan fork dari github pbp ke repositori github pribadi saya
    2. Setelah itu saya lakukan cloning repositori saya ke local computer saya agar saya dapat melakukan editing program di computer saya
    3. Setelah itu saya mengisi file views.py untuk memanggil data yang ada di database initial_catalog_data.json dan juga menambahkan context, yaitu berupa variabel yang nantinya saya akan panggil di template html. Lalu, saya melakukan loaddata database saya dengan memanggil command pada cmd: python manage.py loaddata initial_wishlist_data.json
    4. Lalu saya memetakan routing terhadap fungsi views untuk memanggil database saya ke web Django saya pada urls.py. Selain itu, saya juga mendaftarkan aplikasi katalog ke urls.py yang terdapat pada folder project_django.
    5. Setelah itu saya melakukan editing pada templates untuk menempatkan context nama dan npm saya, serta melakukan looping untuk memanggil data katalog yang terdapat pada database saya.
    6. Setelah itu saya mencoba run app saya di localhost untuk mengecek apakah app saya sudah bener
    7. Setelah selesai dan sudah benar, saya melakukan add, commit dan push untuk mengupdate repositori saya di github
    8. Lalu saya melakukan deployment dengan menyambungkan akun heroku saya dengan repositori saya.








