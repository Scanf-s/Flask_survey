# 기초적인 설문조사 WEB개발 프로젝트

이 프로젝트는, 사용자 정보를 입력받고, 해당 사용자가 주어진 설문 또는 테스트에 대한 답변을 기록하여 결과를 표시해주는 프로젝트 입니다.

> 추후, 결과 표시 기능을 pandas를 이용하여 업그레이드 할 예정입니다.

## 주요 기능
- 사용자 정보 입력: 설문 참여자 정보를 입력할 수 있습니다.
- 설문(테스트): Database에 저장한 설문 5문항을 보여줍니다.
- 결과: 사용자가 답변한 내용을 보여줍니다. (추후, 결과 표시 기능을 업그레이드 할 예정입니다.)
- 어드민 페이지: 각 사용자의 답변에 대한 기록, Database Model, 등을 확인할 수 있는 페이지 입니다.

## 개발 환경
![](https://img.shields.io/badge/AMD-ED1C24?style=for-the-badge&logo=amd&logoColor=white)
![](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 사용 기술
![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![](https://img.shields.io/badge/Jinja-B41717?style=for-the-badge&logo=Jinja&logoColor=white)
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)
![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![](https://img.shields.io/badge/Sqlalchemy-D71F00?style=for-the-badge&logo=SQLalchemy&logoColor=white)

## 프로젝트 구조
```yaml
```

## 실행방법
#### 1. Clone repo in TERMINAL
```bash
git clone repo
cd path_to_dir
```

#### 2. Install Docker
[Download Link](https://www.docker.com/products/docker-desktop/)

#### 3. Download Docker Image and Compose in TERMINAL
```bash
docker pull sullungim/flask-web
docker compose up  //automatically compose mysql database
```

#### 4. Flask-migrate
In docker web sub-container, open EXEC (terminal) and run below commands
```bash
flask db init
flask db migrate
flask db upgrade
```

#### 5. Run
```yaml
Open your web browser, connect to 127.0.0.1:5000/
Admin page route : 127.0.0.1/admin
Go to admin page, click question tab, add new questions first!!
```



### 패치 내역
#### 2024.05.11
- ~admin page question_list set deactivate 버튼을 클릭하면 false로 바뀌어야 하는데, 반영되지 않음. 수정 필요~ **(수정 완료)**

#### 2024.05.13
- 기존 프로젝트를 불편하게 구성해야했는데, Docker를 도입하여 기존 과정을 자동화하여 손쉽게 프로젝트를 다운받아서 실행할 수 있도록 개선하였습니다.


