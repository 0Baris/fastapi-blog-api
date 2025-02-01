# 📚 Blog API

Bu proje, FastAPI kullanarak geliştirilmiş bir Blog API'sidir. Kullanıcıların blog yazıları oluşturmasına, düzenlemesine, silmesine ve yorum yapmasına olanak tanır.


> **Not:** Herhangi bir hata ile karşılaşırsanız bana [bariscem@proton.me](mailto:bariscem@proton.me) adresinden ulaşabilirsiniz, sorununuzu çözmekten memnuniyet duyarım.

## ✨ Özellikler

- Kullanıcı oluşturma, listeleme ve tekil kullanıcı getirme.
- Kategori oluşturma, düzenleme, silme ve listeleme.
- Blog yazısı oluşturma, düzenleme, silme ve listeleme.
- Yorum oluşturma, düzenleme, silme ve listeleme.

## 🛠️ Teknolojiler

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [bcrypt](https://pypi.org/project/bcrypt/)

## 🚀 Adım Adım Kurulum (Docker ile)

### Gereksinimler

- PostgreSQL
  
1. **Proje Deposu Klonlama:**
   ```bash
   git clone https://github.com/0Baris/fastapi-blog-api.git
   cd fastapi-blog-api
   ```

2. **Docker ve Docker Compose Kurulumu:**
   Docker ve Docker Compose'un sisteminizde kurulu olduğundan emin olun. Kurulum için aşağıdaki bağlantıları kullanabilirsiniz:
   - [Docker Kurulumu](https://docs.docker.com/get-docker/)
   - [Docker Compose Kurulumu](https://docs.docker.com/compose/install/)

3. **.env Dosyasını Oluşturma ve Yapılandırma:**
   Projenin kök dizininde `.env` dosyası oluşturun ve aşağıdaki ortam değişkenlerini ekleyin:
   ```env
   POSTGRES_USER=blog_ad
   POSTGRES_PASSWORD=blog_sifre
   POSTGRES_DB=blog_db
   DATABASE_URL=postgresql://blog_ad:blog_sifre@db:5432/blog_db
   ```

4. **Docker Konteynerlerini Başlatma:**
   ```bash
   docker-compose up --build
   ```

5. **Geliştirme Sunucusuna Erişim:**
   Tarayıcıda `http://localhost:8000/docs` veya `http://localhost:8000/redoc` adreslerinden API dokümantasyonuna ulaşabilirsiniz.

## 📖 API Kullanımı

- **`database.py`**: Veritabanı bağlantısını ve yapılandırmayı içerir.
- **`models.py`**: SQLAlchemy ile veritabanı tablolarını tanımlar.
- **`schemas.py`**: Pydantic ile gelen ve giden verileri doğrular.
- **`hashing.py`**: Kullanıcı parolalarını güvenli bir şekilde saklamak için hashleme işlemlerini içerir.
- **`main.py`**: FastAPI endpoint'lerini ve veritabanı işlemleri içerir.


### Tüm Kullanıcıları Getirme

- **Endpoint:** `/users/`
- **Yöntem:** `GET`

### Tekil Kullanıcı Getirme

- **Endpoint:** `/users/{user_id}`
- **Yöntem:** `GET`

### Kategori Ekleme

- **Endpoint:** `/category/`
- **Yöntem:** `POST`
- **İstek Gövdesi:**
    ```json
    {
        "title": "Kategori Başlığı"
    }
    ```

### Tüm Kategorileri Getirme

- **Endpoint:** `/category/`
- **Yöntem:** `GET`

### Tekil Kategori Getirme

- **Endpoint:** `/category/{category_id}`
- **Yöntem:** `GET`

### Kategori Güncelleme

- **Endpoint:** `/category-update/{category_id}`
- **Yöntem:** `PUT`
- **İstek Gövdesi:**
    ```json
    {
        "title": "Yeni Kategori Başlığı"
    }
    ```

### Kategori Silme

- **Endpoint:** `/category-delete/{category_id}`
- **Yöntem:** `DELETE`

### Gönderi Oluşturma

- **Endpoint:** `/posts/`
- **Yöntem:** `POST`
- **İstek Gövdesi:**
    ```json
    {
        "title": "Gönderi Başlığı",
        "content": "Gönderi İçeriği",
        "category_id": 1,
        "author_id": 1
    }
    ```

### Tüm Gönderileri Getirme

- **Endpoint:** `/posts/`
- **Yöntem:** `GET`

### Tekil Gönderi Getirme

- **Endpoint:** `/posts/{post_id}`
- **Yöntem:** `GET`

### Gönderi Güncelleme

- **Endpoint:** `/posts-update/{post_id}`
- **Yöntem:** `PUT`
- **İstek Gövdesi:**
    ```json
    {
        "title": "Yeni Gönderi Başlığı",
        "content": "Yeni Gönderi İçeriği"
    }
    ```

### Gönderi Silme

- **Endpoint:** `/posts-delete/{post_id}`
- **Yöntem:** `DELETE`

### Yorum Ekleme

- **Endpoint:** `/posts/{post_id}/add-comment`
- **Yöntem:** `POST`
- **İstek Gövdesi:**
    ```json
    {
        "content": "Yorum İçeriği",
        "author_id": 1
    }
    ```

### Yorum Silme

- **Endpoint:** `/posts/{post_id}/delete-comment`
- **Yöntem:** `DELETE`

## 🤝 Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir issue açın.

## 📜 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.

## 📚 Kaynakça

- [FastAPI Dokümantasyonu](https://fastapi.tiangolo.com/learn)
- [SQLAlchemy ORM Dokümantasyonu](https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html)
- [Using FastAPI with SQLAlchemy](https://blog.stackademic.com/using-fastapi-with-sqlalchemy-5cd370473fe5)
- [Build a CRUD App with FastAPI and SQLAlchemy](https://codevoweb.com/build-a-crud-app-with-fastapi-and-sqlalchemy/)
- [Creating A CRUD API with FastApi](https://medium.com/@stanker801/creating-a-crud-api-with-fastapi-sqlalchemy-postgresql-postman-pydantic-1ba6b9de9f23)
- [SQLAlchemy and Flask-Bcrypt](https://medium.com/@sharoze.archer/strong-password-hashing-with-sqlalchemy-for-enhanced-database-security-efc4ecda9f08)