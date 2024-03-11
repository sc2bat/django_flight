# django_flight

## 장고 서버 프로젝트
이 프로젝트는 장고 웹 애플리케이션으로 Flutter 프로젝트를 위한 API 서버입니다. 

### 사용된 스킬
언어 Python 3.8
데이터베이스 MySQL 8.0 
서버 Ubuntu 22.04.4 LTS

### 기능
사용자 등록 및 로그인
데이터베이스(MySql 8.0) CRUD 작업

### 설치 및 실행
이 프로젝트를 실행하려면 다음 단계를 따르십시오:

#### 설치 및 설정
MySQL 설치 및 설정
MySQL 8.0 데이터베이스를 설치하고 설정합니다.
```
sudo apt update
sudo apt install mysql-server
```

#### 프로젝트 설정
프로젝트를 클론하고 가상 환경을 설정합니다.
```
git clone https://github.com/your_username/your_project.git
cd your_project
python -m venv venv
source venv/bin/activate (윈도우에서는 venv\Scripts\activate)
pip install -r requirements.txt
```

#### Django 설정
프로젝트 내부의 settings.py 파일에서 MySQL 데이터베이스에 대한 설정을 변경합니다.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### 데이터베이스 마이그레이션을 수행합니다:
```
python manage.py migrate
```

#### 서버를 실행합니다:
```
python manage.py runserver
```

브라우저에서 http://localhost:8000으로 접속하여 애플리케이션을 확인합니다.