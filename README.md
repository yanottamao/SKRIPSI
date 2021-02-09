# Repository Skripsi

## Skripsi Pemetaan

### Deskripsi

Repository untuk kode skripsi pemetaan dalam ruang menggunakan ardrone

### Cara Menjalankan Kode

- Install ROS Indigo beserta pendukungnya

  Tutorial install : [install ros indigo](https://github.com/yanottamao/ros_install)

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
```

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
