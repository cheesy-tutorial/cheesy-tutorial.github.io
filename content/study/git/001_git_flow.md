---
title: "001 Git Flow"
metaTitle: "카카오톡 개발 커뮤니티 오픈 채팅방 리스트 모음집"
metaDescription: "카카오톡 개발 커뮤니티 오픈 채팅방 리스트 정리 되어 있음"
---

# 1. Getting Started
Git Flow에 대해 정리되어 있습니다.
<br/>

# 2. Git Flow 이란
- GitFlow는 Vincent Driessen 이라는 개발자가 처음 제시한 Git 기반 협업 Flow입니다. 프로젝트의 규모가 클수록 Git WorkFlow를 사용하여 적용을 하고 있으며 더 나아가 CI/CD와 같은 도구에서도 이를 사용하고 있다.

<br/>

**2-1. 작동 원리**
- GitFlow는 Branch 분기 단위로 이루어진다. GitFlow의 필수 Branch는 아래와 같으며 아래 브랜치를 사용하여 Flow를 이룬다.
  - 브랜치 명   

    |브랜치 이름|내용|비고|
    |---|---------------------|-----|
    |master|Git 저장소 기본 브랜치|-|
    |develop|개발 브랜치|-|
    |release|릴리즈 브랜치|사용할 떄도 있고 안할때도 있음|
    |feature|기능 개발 브랜치|-|
    |bugfix|버그 수정 브랜치|-|

  <br/>
  
  - 브랜치 명 규칙
    - master, develop, release 브랜치는 이름이 고정되어 있음
    - feature, bugfix 브랜치는 경우에 따라 이름이 변경됨
  
  <br/>
  
  - Git Flow 예시 (Release 브랜치를 사용하지 않을 때)
    - User 삭제 API 기능을 추가할 때 (feature/api-user-remove 브랜치)
      ![ex_screenshot](./assets//api-v1.png)