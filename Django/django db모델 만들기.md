# django db모델 만들기



### 1. 가상환경 설정 pyenv

### 2. django 설치

### 3.$ django-admin startproject first_workshop .

### 4.$ python manage.py startapp pages

### 5. settings.py에서 ALLOWED_HOSTS 에 url 추가, INSTALLED_APPS에 students.apps.StudentsConfig

## 5-1.migration하기



### 6. models.py에 db를 위한 class 만들기

### 7. admin.py에 admin.site.register(Student)   -->class 등록(from .models import student(class))

### *8. urls.py에 등록

```python
from django.contrib import admin
from django.urls import path , include
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

```



### 9.

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

class가 변경되면 다시 migration 해줘야함(설계도가 변경되었기 때문에)

### 10. admin 계정만들기

```bash
$ python manage.py createsuperuser
```

### 11. models.py의 클래스 안에 'def __str__'을 통해 오버라이드 가능

