---
title: "Bamboo"
metaTitle: "Syntax Highlighting is the meta title tag for this page"
metaDescription: "This is the meta description for this page"
---

## 리눅스에서 설치하기
1-1. 공식 홈페이지에서 Bamboo 설치 파일 다운로드   
Bamboo 설치 파일은 https://www.atlassian.com/ko/software/bamboo/download 링크에서 다운로드 가능합니다. 가이드에서는 리눅스에서 설치할 것이기 때문에 tar.gz archive 버전을 사용하였습니다.   
![ex_screenshot](./assets//bamboo_install.png)
1-2. 다운로드한 파일 압축 해제   
압축 해제 명령을 사용하여 파일을 압축 해제합니다.
- 명령어
    ``` bash
    # tar -xvf <다운로드 파일명>
    tar -xvf atlassian-bamboo-7.0.3.tar.gz
    ```
1-3. 압축 해제 후, 폴더 이동
정상적으로 압축 해제가 진행되었으면, 새로 생성된 폴더를 확인할 수 있습니다. 폴더로 이동하겠습니다.
![ex_screenshot](./assets//bamboo_uncompression.png)
- 명령어
    ``` bash
    cd atlassian-bamboo-7.0.3
    ```
1-4. Bamboo 실행하기
Bamboo 실행 방법은 ./bin/ 폴더에 들어있는 스크립트를 실행해주면 됩니다. ./bin/ 폴더 내에는 여러 동작을 하는 스크립트가 들어있습니다.
- 명령어
    ``` bash
    # Bamboo 서비스 실행
    ./bin/start-bamboo.sh
    ```
- JRE 설치가 되어있지 않아 실행되지 않을 때
![ex_screenshot](./assets//bamboo_start_jre_failed.png)
Bamboo는 JAVA를 사용하여 동작하기 때문에 JDK 혹은 JRE가 기본으로 설치되어 있어야 합니다. 위와 같은 오류가 발생했을 경우 아래 명령어를 실행하여 설치를 진행합니다.
``` bash
sudo apt-get install default-jre
```
![ex_screenshot](./assets//bamboo_jre_install.png)
설치가 모두 종료되었으면 다시 스크립트를 실행해보겠습니다.
![ex_screenshot](./assets//bamboo_start.png)

## 초기 생성 과정
Plan을 만들기 전, 프로젝트를 먼저 만들어보겠습니다. 프로젝트 명은 Test로 작업해보겠습니다.      
### 프로젝트 만들기
1. 프로젝트는 메인 홈페이지에서 Create 버튼을 통해 만들 수 있습니다.  
![ex_screenshot](./assets//bamboo_project_create.png)
2. 프로젝트 명 입력 후 생성   
프로젝트 명을 입력 후, 생성해보겠습니다. (Test로 진행하였습니다)
![ex_screenshot](./assets//bamboo_project_create_2.png)

3. 프로젝트 생성 성공!
Test 프로젝트가 성공적으로 생성되었습니다!
![ex_screenshot](./assets//bamboo_project_create_3.png)

### Plan 만들기
작업 과정을 만들기 위해 다음으로 Plan을 만들어보겠습니다.
1. Plan 생성 하기
Plan은 Project와 동일한 방법으로 생성할 수 있습니다.
![ex_screenshot](./assets//bamboo_plan_create.png)
2. Plan 초기 설정
![ex_screenshot](./assets//bamboo_plan_new_configure.png)
필요한 초기 설정 정보들을 입력합니다. 
- Project and build plan name   
    - Plan name : Plan 이름 설정
    - Plan Key : Plan Key 설정 (자동으로 입력됩니다.)
    - Plan Description : Plan 설명 가이드 입력
- Link repository to new build plan
    - 저장소 링크하기   

2-1. 저장소 링크 방법
Github에서 사용 중인 저장소를 Bamboo의 Plan과 링크해보겠습니다. 
- Link new repository 설정
![ex_screenshot](./assets//bamboo_plan_new_configure_2.png)
- Github 저장소 찾기
Github와 연결을 위해 계정과 패스워드 및 저장소 이름을 입력해주세요
![ex_screenshot](./assets//bamboo_project_configure_3.png)
계정 입력 후, Load Repositories 버튼을 클릭하면 계정에 사용 중인 저장소 리스트를 가지고 올 수 있습니다.
- Github 저장소 입력 후 저장
![ex_screenshot](./assets//bamboo_new_repository.png)   
저장소 설정 후, 저장 해주세요.

### Job 설정
Job은 Agent Environment 또는 Docker Container 환경에서 설정할 수 있습니다.
|이름|내용|비고|
|------|---|---|
|Agent Environment|Bamboo 실행 Host 환경||
|Docker Container|Bamboo 서버의 Docker Container 환경||   
이 환경 중에서 Agent Environment 환경을 사용해보겠습니다.   
1. Task 생성
Add Task 버튼을 클릭하여 원하는 작업을 생성해보겠습니다. 
npm을 사용하여 빌드를 진행하는 과정을 만들어보겠습니다.
- npm 과정 생성
Bamboo Plan으로 npm task type을 사용할 수 있습니다. npm으로 검색하여 눌러보세요!
![ex_screenshot](./assets//bamboo_npm_task_type.png)   
- npm install
![ex_screenshot](./assets//bamboo_npm_install.png)   
- npm run build
![ex_screenshot](./assets//bamboo_npm_run_build.png)   
- 작업 후, Save And Continue 버튼 클릭
Plan 초기 생성 작업이 완료되었습니다.

## Plan 돌려보기
Plan 설정이 완료되었으면, 설정한 작업대로 정상적으로 동작하는지 확인을 해봐야됩니다. 생성한 Plan은 enable이 되어있지 않은 상태이기 때문에 enable을 먼저 해주겠습니다.   
### Plan enable   
![ex_screenshot](./assets//bamboo_plan_enable.png)   
enable을 클릭하면 Plan enable이 진행됩니다.

### Plan 동작하기 (Run)
이제 동작 (Run)할 준비가 모두 되었습니다. 이제 Run을 해보겠습니다.   
![ex_screenshot](./assets//bamboo_plan_run.png) 
Plan 시작
![ex_screenshot](./assets//bamboo_plan_start.png) 
Plan 성공 시
Plan 동작이 성공적으로 해냈습니다. 만약 실패했더라면 실패한 단계를 수정해주세요
![ex_screenshot](./assets//bamboo_build_success.png) 

