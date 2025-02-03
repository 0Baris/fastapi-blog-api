# 📚 Blog API

Bu proje, FastAPI kullanılarak geliştirilmiş bir Blog API'sidir. Kullanıcıların blog yazıları oluşturmasına, düzenlemesine, silmesine ve yorum yapmasına olanak tanır.

> **Not:** Herhangi bir hata ile karşılaşırsanız bana [bariscem@proton.me](mailto:bariscem@proton.me) adresinden ulaşabilirsiniz. Sorununuzu çözmekten memnuniyet duyarım.

---

## ✨ Özellikler

- **Kullanıcı Yönetimi:**
  - Kullanıcı oluşturma.
  - Kullanıcı listeleme.
  - Tekil kullanıcı getirme.

- **Kategori Yönetimi:**
  - Kategori oluşturma.
  - Kategori düzenleme.
  - Kategori silme.
  - Tüm kategorileri listeleme.

- **Blog Yazı Yönetimi:**
  - Yazı oluşturma.
  - Yazı düzenleme.
  - Yazı silme.
  - Tüm yazıları listeleme.
  - Tekil yazı getirme.
  - Yazıya ait tüm yorumları listeleme.

- **Yorum Yönetimi:**
  - Yorum oluşturma.
  - Yorum silme.

- **Güvenlik:**
  - Kullanıcı parolaları için güvenli hashleme (bcrypt).
  - Ortam değişkenleriyle veritabanı bağlantı bilgilerini yönetme.

---

## 🛠️ Teknolojiler

- **Backend:**
  - [FastAPI](https://fastapi.tiangolo.com/): Modern, hızlı ve kolay bir Python frameworkü.
  - [SQLAlchemy](https://www.sqlalchemy.org/): Python için güçlü bir ORM.
  - [PostgreSQL](https://www.postgresql.org/): Güçlü bir ilişkisel veritabanı sistemine dayalı.
  - [bcrypt](https://pypi.org/project/bcrypt/): Parola hashleme işlemleri için kullanılır.

- **Diğer:**
  - [Pydantic V2](https://pydantic-docs.helpmanual.io/): Veri doğrulama ve seri hale getirme işlemleri için.
  - [Docker](https://www.docker.com/): Uygulamanın konteynerize edilmesi için.
  - [Docker Compose](https://docs.docker.com/compose/): Birden fazla servisi kolayca yönetmek için.

---

## 🚀 Adım Adım Kurulum (Docker ile)

### Gereksinimler

- **[Docker Kurulumu](https://docs.docker.com/get-docker/)**: Projenin çalışması için Docker'in kurulu olması gerekmektedir.
- **[Docker Compose Kurulumu](https://docs.docker.com/compose/install/)**: Servisleri bir arada yönetmek için Docker Compose'in kurulu olması gerekmektedir.

### Adımlar

1. **Proje Deposu Klonlama:**

   ```bash
   git clone https://github.com/0Baris/fastapi-blog-api.git
   cd fastapi-blog-api
   ```

2. **`.env` Dosyasını Oluşturma ve Yapılandırma:**

   Projenin kök dizininde `.env` dosyası oluşturun ve aşağıdaki ortam değişkenlerini ekleyin:

   ```env
   POSTGRES_USER=blog_user  # PostgreSQL kullanıcı adı
   POSTGRES_PASSWORD=blog_pass  # PostgreSQL şifresi
   POSTGRES_DB=blog_db  # PostgreSQL veritabanı adı
   DATABASE_URL=postgresql://blog_user:blog_pass@db:5432/blog_db  # Veritabanı bağlantısı
   ```

    > **Önemli:** docker-compose.yml dosyasındada bu işlemleri tekrarlamanız gerekiyor.

   #### **Notlar:**
   - `POSTGRES_USER`, `POSTGRES_PASSWORD`, ve `POSTGRES_DB` değerlerini kendi yapılandırmanıza göre güncelleyin.
   - `DATABASE_URL`: Veritabanı bağlantısını belirtir. `db` değeri, Docker Compose içindeki PostgreSQL servisinin adıdır.

3. **Docker Konteynerlerini Başlatma:**

   ```bash
   docker compose up --build
   ```

   Bu komut, Docker imajlarını oluşturur ve konteynerleri başlatır.

4. **Geliştirme Sunucusuna Erişim:**

   Tarayıcıda `http://localhost:8000/docs` veya `http://localhost:8000/redoc` adreslerinden API dokümantasyonuna ulaşabilirsiniz.

---

## 📖 API Kullanımı

Aşağıda, API endpoint'leri ve nasıl kullanılacakları açıklanmıştır.

### **Kullanıcı İşlemleri**

- **Tüm Kullanıcıları Getirme:**
  - **Endpoint:** `/api/v1/users/`
  - **Yöntem:** `GET`

- **Tekil Kullanıcıyı Getirme:**
  - **Endpoint:** `/api/v1/users/{user_id}`
  - **Yöntem:** `GET`

- **Kullanıcı Oluşturma:**
  - **Endpoint:** `/api/v1/users/`
  - **Yöntem:** `POST`
  - **İstek Gövdesi:**
    ```json
    {
        "username": "test",
        "email": "test@example.com",
        "password": "benbirsifreyim123"
    }
    ```

---

### **Kategori İşlemleri**

- **Tüm Kategorileri Getirme:**
  - **Endpoint:** `/api/v1/category/`
  - **Yöntem:** `GET`

- **Tekil Kategori Getirme:**
  - **Endpoint:** `/api/v1/category/{category_id}`
  - **Yöntem:** `GET`

- **Kategori Oluşturma:**
  - **Endpoint:** `/api/v1/category/`
  - **Yöntem:** `POST`
  - **İstek Gövdesi:**
    ```json
    {
        "title": "Teknoloji"
    }
    ```

- **Kategori Güncelleme:**
  - **Endpoint:** `/api/v1/category/update/{category_id}`
  - **Yöntem:** `PUT`
  - **İstek Gövdesi:**
    ```json
    {
        "title": "Yeni Kategori"
    }
    ```

- **Kategori Silme:**
  - **Endpoint:** `/api/v1/categories/delete/{category_id}`
  - **Yöntem:** `DELETE`

---

### **Blog Yazı İşlemleri**

- **Tüm Yazıları Getirme:**
  - **Endpoint:** `/api/v1/posts/`
  - **Yöntem:** `GET`

- **Tekil Yazı Getirme:**
  - **Endpoint:** `/api/v1/posts/{post_id}`
  - **Yöntem:** `GET`

- **Yazı Oluşturma:**
  - **Endpoint:** `/api/v1/posts/`
  - **Yöntem:** `POST`
  - **İstek Gövdesi:**
    ```json
    {
        "title": "Python ile FastAPI Kullanımı",
        "content": "FastAPI, modern bir Python frameworküdür.",
        "category_id": 1,
        "author_id": 1
    }
    ```

- **Yazı Güncelleme:**
  - **Endpoint:** `/api/v1/posts/update/{post_id}`
  - **Yöntem:** `PUT`
  - **İstek Gövdesi:**
    ```json
    {
        "title": "Güncellenmiş Yazı Başlığı",
        "content": "Güncellenmiş yazı içeriği."
    }
    ```

- **Yazı Silme:**
  - **Endpoint:** `/api/v1/posts/delete/{post_id}`
  - **Yöntem:** `DELETE`

---

### **Yorum İşlemleri**

- **Yorum Ekleme:**
  - **Endpoint:** `/api/v1/comments/{post_id}/add`
  - **Yöntem:** `POST`
  - **İstek Gövdesi:**
    ```json
    {
        "content": "Bu bir test yorumudur.",
        "author_id": 1
    }
    ```

- **Yorum Silme:**
  - **Endpoint:** `/api/v1/comments/{post_id}/delete`
  - **Yöntem:** `DELETE`

---

## 🤝 Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1. **Fork'layın:**
   Projeyi GitHub'da forklayın.

2. **Yeni Bir Dal Oluşturun:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Değişiklikleri Yapın ve Commit Edin:**
   ```bash
   git add .
   git commit -m "Özellik: Yeni özellik eklendi."
   ```

4. **Dalınızı Push Edin:**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Pull Request Oluşturun:**
   GitHub üzerinden orijinal depoya pull request açın ve değişikliklerinizi açıklayın.

---

## 📜 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

---

## 📚 Kaynakça

- [FastAPI Dokümantasyonu](https://fastapi.tiangolo.com/learn)
- [SQLAlchemy ORM Dokümantasyonu](https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html)
- [Using FastAPI with SQLAlchemy](https://blog.stackademic.com/using-fastapi-with-sqlalchemy-5cd370473fe5)
- [Build a CRUD App with FastAPI and SQLAlchemy](https://codevoweb.com/build-a-crud-app-with-fastapi-and-sqlalchemy/)
- [Creating a CRUD API with FastAPI](https://medium.com/@stanker801/creating-a-crud-api-with-fastapi-sqlalchemy-postgresql-postman-pydantic-1ba6b9de9f23)
- [Strong Password Hashing with SQLAlchemy](https://medium.com/@sharoze.archer/strong-password-hashing-with-sqlalchemy-for-enhanced-database-security-efc4ecda9f08)

---

## 🔍 Hata Ayıklama

Eğer uygulama çalışmadıysa, aşağıdaki adımları izleyin:

1. **Logları Kontrol Edin:**
   - Docker loglarını kontrol etmek için:
     ```bash
     docker compose logs app
     ```
   - PostgreSQL loglarını kontrol etmek için:
     ```bash
     docker compose logs db
     ```

2. **Ortam Değişkenlerini Doğrulayın:**
   - `.env` dosyasındaki yapılandırmaların doğru olduğundan emin olun.

3. **Dockerfile'i ve `docker-compose.yml`'i Denetleyin:**
   - `Dockerfile` ve `docker-compose.yml` dosyalarının son güncellemeyle uyumlu olduğundan emin olun.

4. **Pydantic Modellerini Yeniden Oluşturun:**
   - Eğer Pydantic V2 kullanıyorsanız, modellerinizde `from_attributes = True` kullanıldığından emin olun.
   - İlişkiler için `.rebuild()` yöntemini çağırın.


---

## 🙌 İletişim

Projeyle ilgili sorularınız, önerileriniz veya geri bildirimleriniz için bana ulaşabilirsiniz:

- **E-posta:** [bariscem@proton.me](mailto:bariscem@proton.me)
- **LinkedIn:** [Barış Cem Ant](https://www.linkedin.com/in/baris-cem-ant/)
- **GitHub:** [Barış Cem Ant](https://github.com/0Baris)

