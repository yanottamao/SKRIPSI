# Repository Skripsi

## Skripsi Pemetaan

### Deskripsi

Repository untuk kode skripsi pemetaan dalam ruang menggunakan ardrone

### Kebutuhan

1. ROS Indigo

2. Gazebo versi 2.x

3. Pendukung

   Tutorial install : [install ros indigo](https://github.com/yanottamao/ros_install)

### Cara Menjalankan Kode

- Jalankan simulasi atau hubungkan ke drone fisik

```bash
$ cd simulasi/
menuju ke directory simulasi
```

```bash
$ roslaunch drone_application lab_sim_drone.launch
perintah menjalankan simulasi
```

- Jalankan kode di terminal

```bash
$ python nama_kode.py
perintah menjalankan program
main.py = kode pergerakan
misc.py = kode menjalankan slam
```

- Cara menjalankan lsd-slam

  1. Install library [lsd-slam](https://github.com/yanottamao/lsd_slam)

  2. Jalankan perintah di terminal

### Troubleshoot

- Ketika kode stuck

```bash
$ ctrl + c
keluar dari loop kode
```

### To Do future

- [ ] Integrasi semua fungsi
- [ ] Integrasi gui
- [ ] Menambah fungsi main untuk menggabungkan pemanggilan fungsi
- [ ] Membaca / menscan input keyboard tanpa enter, preliminary menggunakan module curses
- [ ] ...
- [ ] ...

### Progress to do

1. Menyederhanakan kode
2. Menjadikan fungsi pergerakan dll jadi satu tanpa mengulangi penulisan
3. Cari fungsi dari kode yang tidak yakin
