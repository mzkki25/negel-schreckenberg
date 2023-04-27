## Negel Schreckenberg

Negel-Schreckenberg (NS) adalah model matematika untuk menggambarkan perilaku lalu lintas pada jalan raya. Model ini dikembangkan oleh Kai Nagel dan Michael Schreckenberg pada tahun 1992.

Model NS didasarkan pada selular otomata, yang merupakan model matematika yang terdiri dari jaringan sel atau kotak yang masing-masing dapat mengambil satu dari beberapa nilai diskrit. Dalam kasus NS, setiap sel mewakili sepotong jalan dengan panjang tertentu.

Dalam model NS, setiap mobil direpresentasikan oleh satu sel. Setiap mobil memiliki kecepatan maksimum, dan selalu berusaha untuk mencapai kecepatan maksimum tersebut. Namun, mobil juga dipengaruhi oleh mobil di depannya dan oleh kondisi lalu lintas di jalan.

Parameter-parameter pada fungsi negel_schreckenberg adalah sebagai berikut:
1. M: Merupakan panjang jalan (road length) dalam sel atau kotak. Ini menentukan jumlah sel dalam model selular otomata.
2. prob: Probabilitas gangguan acak. Ini menentukan probabilitas mobil akan melakukan pengurangan kecepatan secara acak.
3. num_of_car: Jumlah mobil pada jalan. Ini menentukan jumlah mobil yang akan ditempatkan pada jalan awal.
4. vmax: Kecepatan maksimum yang diizinkan di jalan. Ini menentukan kecepatan maksimum yang dapat dicapai oleh setiap mobil.
5. tmax: Waktu maksimum yang diizinkan untuk simulasi. Ini menentukan berapa lama simulasi akan dijalankan.

Dalam fungsi negel_schreckenberg, parameter ini digunakan untuk membangun model matematika untuk menggambarkan perilaku lalu lintas pada jalan raya. Parameter-parameter ini menentukan kondisi awal dan batas-batas dari simulasi dan akan mempengaruhi perilaku mobil selama simulasi berlangsung. Parameter-parameter ini harus dipilih dengan hati-hati untuk memastikan simulasi menghasilkan hasil yang akurat dan berguna.
