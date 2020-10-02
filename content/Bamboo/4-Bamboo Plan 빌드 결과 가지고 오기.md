# Bamboo Plan 빌드 결과 가지고 오기
* * *

## **1. Getting Started**
Bamboo의 Plan에서 빌드를 마친 후, 빌드에 대한 정보를 가지고 와서 다른 곳에 필요로 하는 경우가 있을 수 있습니다. 데이터를 가지고 온 후, 파싱하는 방법까지 알아보겠습니다.   

## **2. Jira, Bamboo 연동 방법**
- Bamboo에서 설정 페이지로 이동
![ex_screenshot](./assets//bamboo_configure.png)
- 좌측의 Application Links 페이지로 이동합니다.
![ex_screenshot](./assets//bamboo_configure_2.png)
- 사용 중인 Atlassian 링크를 입력해줍니다.
![ex_screenshot](./assets//bamboo_configure_3.png)
- 연동 정보를 확인 후, 이상 없으면 Continue 버튼을 눌러주세요.
![ex_screenshot](./assets//bamboo_configure_4.png)

## **3. 사용 방법**
Bamboo Plan Build의 결과에서 관련 Jira Issue를 가지고 오는 방법에 대해 알아보겠습니다.

- 저장소에서 Jira의 Issue Key를 커밋을 해봅니다.
    ``` bash
    git commit -m "TEST-4 테스트 중!"
    ```
- Bamboo에서 빌드 시, TEST-4라는 지라 링크를 인식하여 저장하는 지 확인해주세요. 아래 빨간 박스와 같이 인식하면 성공입니다.
![ex_screenshot](./assets//bamboo_build_result_1.png)
- 이제 Build 결과를 가지고 오겠습니다. 결과는 특정 URL을 통해 결과를 XML 포맷으로 가지고 올 수 있습니다.
    ``` bash
    ## URL 예시
    ## http://서버주소/rest/api/latest/result/Bamboo빌드 키?expand=jiraIssues
    http://192.168.100.100:8085/rest/api/latest/result/DOC-TEST-2?expand=jiraIssues
    ```
    ![ex_screenshot](./assets//bamboo_build_result_2.png)

- Jira 관련 이슈 키를 가지고 오기 위해서는 jiraIssues 라는 것을 사용해야 합니다. 아래와 같이 이슈 키 리스트를 확인할 수 있습니다.
    ``` xml
    <jiraIssues start-index="0" max-result="1" size="1">
        <issue key="TEAM-4"/>
    </jiraIssues>
    ```

- URL에 접속 후, XML 파싱 후 이슈 리스트를 가지고 오는 코드를 짜보겠습니다.
    - Gist 링크 : https://gist.github.com/gwangildev/b64fd4c80833d477d18590e0cfa73e8c
    - 소스 코드
        ``` python
        import requests
        import xml.etree.ElementTree as elemTree
        import sys
        from requests.auth import HTTPBasicAuth
        import json
        import sys

        list_issues = []
        IP  = "<BAMBOO SERVER IP>"
        ISSUE_KEY = "<JIRA ISSUE_KEY>"
        USERID  = "<BAMBOO USERID>"
        PASSWD  = "<BAMBOO PASSWD>"

        req = requests.get("http://{}/rest/api/latest/result/{}?expand=jiraIssues".format(IP, ISSUE_KEY), auth=(USERID, PASSWD))

        root = elemTree.fromstring(req.text)
        tree = elemTree.ElementTree(elemTree.fromstring(req.text))

        res = tree.find('jiraIssues')

        if res:
            tt = list(res.iter('issue'))
            for t in tt:
                key = t.get('key')
                list_issues.append(key)
            print(str(list_issues).replace("\n", "").replace("'", "\\\""))
        ```

- 소스를 작성 후, 돌려보세요!
    - 명령어
        ``` bash
        python3.8 test.py
        ```
    - 결과
    ![ex_screenshot](./assets//bamboo_build_result_3.png)
