---
title: "Python 모듈 빌드 후 빌드된 것 사용하기"
metaTitle: "Python 모듈 빌드 후, 빌드된 것 사용 방법"
metaDescription: "Python 모듈 빌드 후, 빌드된 것 사용 방법에 정리되어 있음"
---

# 1. Getting Started
Python MySQLdb 모듈을 사용하여 파이썬 빌드 후, 빌드된 파일을 사용하는 방법에 대해 알아보겠습니다.

# 2. 모듈 빌드 방법
- MySQLdb 모듈 다운로드하기
``` bash
wget https://files.pythonhosted.org/packages/a5/e9/51b544da85a36a68debe7a7091f068d802fc515a3a202652828c73453cad/MySQL-python-1.2.5.zip
```

- MySQLdb 모듈 압축 해제 후, 경로 이동하기
``` bash
## 압축 해제
unzip MySQL-python-1.2.5.zip
## 경로 이동
cd MySQL-python-1.2.5
```

- 빌드 옵션 수정
  - MySQL이 설치된 경로가 커스텀일 경우, mysql_config 바이너리를 못 찾을 수 있습니다.
  - site.cfg를 수정하여 mysql_config 경로를 지정해주세요.
  ``` bash
  [options]
  # embedded: link against the embedded server library
  # threadsafe: use the threadsafe client
  # static: link against a static library (probably required for embedded)

  embedded = False
  threadsafe = True
  static = False

  # The path to mysql_config.
  # Only use this if mysql_config is not on your PATH, or you have some weird
  # setup that requires it.
  mysql_config = /usr/local/mariadb/bin/mysql_config

  # http://stackoverflow.com/questions/1972259/mysql-python-install-problem-using-virtualenv-windows-pip
  # Windows connector libs for MySQL. You need a 32-bit connector for your 32-bit Python build.
  connector = C:\Program Files (x86)\MySQL\MySQL Connector C 6.0.2
  ```
- 빌드하기
``` bash
python setup.py install
```