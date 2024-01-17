# Retto Social -> Kurulum

- Gerekli paketlerin kurulumu
- Pipenv ortamına girilmesi
- Environ ayarlamalarının yapılması
- Migration işlemlerinin yapılması
- Sunucunun ayağa kaldırılması

## 1 - Gerekli paketlerin kurulumu

Sistemimizi Pipenv ortamında kullanabilmemiz için paketlerin kurulumunu yapmamız gerekiyor.

```
pipenv install -r requirements.txt
```

komutu ile gerekli paketlerin kurulumunu yapabilirsiniz.

## 2 - Pipenv ortamına girilmesi
Paketlerin kurulumunu yaptık. Şimdi ise pipenv ortamına giriş yapabiliriz.

```
pipenv shell
```

komutu ile Pipenv shell ortamına girebilirsiniz.

## 3 - Environ ayarlarının yapılması
Projenize kullandığınız hassas bilgileri dış ortamlardan korumak için bir environ dosyası kullanmak istiyor olabilirsiniz. Retto içerisinde halihazırda ```.env``` isimli environ dosyasını tanımlıdır. İçerisine secret key, veritabanı bilgileriniz gibi bilgileri girebilirsiniz.

Kullanımı; .env dosyasına girin ve bilgileri tanımlayın

```
SECRET_KEY="secret_keyinizi_girin"
```

Bu dosyayı projeye göre konfigüre edebilirsiniz.

Ardından settings.py üzerinde bu verileri 

```python
env('SECRET_KEY')
``` 

gibi çekebilirsiniz.

**Not;** .env dosyası git üzerinde bulunmamaktadır. Dizin içerisine .env isimli dosyayı kendiniz oluşturup tanımlamaları yapmalısınız.

## 4 - Migration işlemlerinin yapılması

Projenin temel ayarlarını yaptık. Şimdi veritabanı migrationlarını yapacağız.

İlk olarak ```makemigrations``` komutunu kullanıyoruz.

```
python manage.py makemigrations
```

Kullandığınız işletim sistemi Linux veya MacOS ise ```python``` yerine ```python3``` ifadesini kullanabilirsiniz.

Ardından migrate işlemini gerçekleştiriyoruz

```
python manage.py migrate
```

Tebrikler. Veritabanı başarıyla migrate edildi.

## 5 - Sunucunun ayağa kaldırılması
Proje asenkron işlemler içerdiği için ASGI/Daphne sunucusu üzerinde çalışmaktadır. Daphne, django projenizi ASGI olarak ayağa kaldırmanızı sağlayan bir araçtır. Retto içerisinde kurulu gelmektedir.

Pipenv ortamı içerisindeyken;

```
python manage.py runserver
```

Eğer hosting üzerinde deploy işlemi yapıyorsanız runserver'dan sonra 0.0.0.0:80 yazarak sistemi default port üzerinde çalıştırabilirsiniz.