---
title: "003 Git 유저 정보 설정"
metaTitle: "Git을 내 컴퓨터에 설치하고 처음 사용자 설정하는 방법에 대해 정리되어 있음"
metaDescription: "Git을 내 컴퓨터에 설치하고 처음 사용자 설정하는 방법에 대해 정리되어 있음"
---

# 1. Getting Started
Git을 설치하고 개발자 (본인)의 정보를 저장하는 방법에 대해 정리되어 있습니다. 저장 방법은 아래와 같습니다.
  - 사용자 정보 모든 저장소에 Global 저장
  - 필요한 저장소에서만 사용자 정보 저장하기
첫번째는 내가 사용하는 컴퓨터에 저장된 모든 저장소에 사용되는 개발자 정보를 입력하는 방법입니다. 그리고  두번째는 필요한 저장소에서만 개발자 정보를 입력하는 방법입니다.
<br/>
<br/>

# 2. 사용자 정보 Global 저장
``` bash
# 예시
# git config --global user.name "Your Name"
# git config --global user.email you@example.com
git config --global user.name "Leonardo DiCaprio"
git config --global user.email "LeonardoDiCaprio@gmail.com"
```
<br/>
<br/>

# 3. 특정 저장소에서 사용자 정보 저장
``` bash
# 예시
# git config --local user.name "Your Name"
# git config --local user.email you@example.com
git config --local user.name "Leonardo DiCaprio"
git config --local user.email "LeonardoDiCaprio@gmail.com"
```