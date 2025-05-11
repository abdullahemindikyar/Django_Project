# 🎬 Movie App - Film İzleme Platformu

Modern ve kullanıcı dostu bir film izleme platformu. Django ile geliştirilmiş bu web uygulaması, film severlerin filmleri keşfetmesini, favorilere eklemesini ve filmler hakkında etkileşimde bulunmasını sağlar.

## ✨ Özellikler

### 🎥 Film Yönetimi
- Film listesi görüntüleme
- Film detay sayfaları
- Popüler filmler bölümü
- Film arama ve filtreleme // sembolik 

### 👤 Kullanıcı Özellikleri
- Kullanıcı kaydı ve girişi
- Profil yönetimi
- Favori filmler listesi
- Film beğenme/beğenmeme
- Film favorilere ekleme/çıkarma

### 🎨 Modern Arayüz
- Responsive tasarım
- Bootstrap 5 framework'ü
- Font Awesome ikonları
- Modern renk şeması
- Animasyonlu geçişler
- Kullanıcı dostu navigasyon

## 🛠️ Teknolojiler

- **Backend:** Django 4.x
- **Frontend:** 
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5
  - Font Awesome
- **Veritabanı:** 
  - SQLite 
- **Diğer:** 
  - Django 

## 🚀 Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/movie-app.git
cd movie-app
```

2. Sanal ortam oluşturun ve aktif edin:
```bash
python -m venv venv
# Windows için:
venv\Scripts\activate
# Linux/Mac için:
source venv/bin/activate
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Veritabanı migrasyonlarını yapın:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Süper kullanıcı oluşturun:
```bash
python manage.py createsuperuser
```

6. Geliştirme sunucusunu başlatın:
```bash
python manage.py runserver
```

## 📁 Proje Yapısı

```
movieapp/
├── account/                 # Kullanıcı yönetimi uygulaması
│   ├── templates/          # Kullanıcı şablonları
│   ├── views.py           # Kullanıcı görünümleri
│   └── urls.py            # Kullanıcı URL'leri
├── movies/                 # Film uygulaması
│   ├── templates/         # Film şablonları
│   ├── models.py         # Film modelleri
│   ├── views.py          # Film görünümleri
│   └── urls.py           # Film URL'leri
├── static/                # Statik dosyalar
│   ├── css/             # CSS dosyaları
│   ├── js/              # JavaScript dosyaları
│   └── img/             # Görseller
├── templates/            # Ana şablonlar
├── manage.py            # Django yönetim scripti
└── requirements.txt     # Proje bağımlılıkları
```

## 🔑 Önemli URL'ler

- Ana Sayfa: `http://127.0.0.1:8000/`
- Film Listesi: `http://127.0.0.1:8000/movies/`
- Favori Filmler: `http://127.0.0.1:8000/movies/favorites/`
- Giriş: `http://127.0.0.1:8000/account/login/`
- Kayıt: `http://127.0.0.1:8000/account/register/`
- Profil: `http://127.0.0.1:8000/account/profile/`

## 👥 Kullanıcı Rolleri

### Ziyaretçi
- Film listesini görüntüleme
- Film detaylarını görüntüleme
- Kayıt olma ve giriş yapma

### Üye
- Film beğenme/beğenmeme
- Film favorilere ekleme/çıkarma
- Profil yönetimi
- Favori filmler listesi

## 📞 İletişim

Proje Sahibi - [@abdullahemindikyar](https://github.com/abdullahemindikyar)

Proje Linki: [https://github.com/abdullahemindikyar/Django_Project
