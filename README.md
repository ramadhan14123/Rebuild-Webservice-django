# WEBSERVICE DJANGO

Repositori ini merupakan hasil rebuild dari proyek microservice yang dibangun menggunakan framework Django, berdasarkan repositori awal: [hepidad/c004-webservice](https://github.com/hepidad/c004-webservice).

## Daftar Isi

- [Tentang Proyek](#Tentang-Proyek)
- [Instalasi dan Penggunaan](#instalasi-dan-penggunaan)
- [Struktural Direktori](#struktural-direktori)
  
## Tentang Proyek
Proyek ini merupakan hasil rebuild yang dibuat untuk tujuan pembelajaran konsep arsitektur webservice. Melalui proyek ini, pengguna dapat memahami bagaimana server side dan client side (webservice) saling berinteraksi satu sama lain, serta bagaimana komunikasi terjadi antara client dan server dalam sistem terdistribusi menggunakan framework Django.

## Instalasi dan Penggunaan
1. Clone repository Ini
```bash
git clone https://github.com/ramadhan14123/Rebuild-Webservice-django.git
```
2. Masuk ke direktory proyek
```bash
cd Rebuild-Webservice-django
```
3. Buat virtual environment pada setiap direktori proyek `carsweb_client_django` dan `carsweb_server_django`
- Membuat environment 
```bash
python -m venv env
```
- Aktivasi environment
``` bash
env\Script\activate
```
4. Install library dari requirements
```bash
pip install -r req.txt #lakukan pada semua direktori
```

5. Jalankan migrasi pada server side `carsweb_server_django`
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Menjalankan proyek
- menjalankan server side
```bash
python manage.py runserver 5012
```
- menjalankan client side
```bash
python manage.py runserver 5011
```


## Struktur Direktori
```bash
.
└── Rebuild-Webserviced-Django/
    ├── carsweb_client_django/ #Direktori utama client side
    │   ├── carsweb_client/
    │   │   └── client/
    │   │       ├── __pycache__
    │   │       ├── static
    │   │       ├── templates 
    │   │       ├── __init__.py
    │   │       ├── urls.py
    │   │       └── views.py 
    │   ├── env #harus ada environment
    │   ├── db.sqlite3
    │   ├── manage.py
    │   ├── README.md
    │   └── req.txt
    └── carsweb_server_django/ #Direktori utama server side
        ├── carserver/
        │   ├── carserver
        │   ├── server
        │   ├── db.sqlite3
        │   └── manage.py
        ├── env #harus ada environment
        ├── req.txt
        ├── .gitignore
        └── README.md
```
