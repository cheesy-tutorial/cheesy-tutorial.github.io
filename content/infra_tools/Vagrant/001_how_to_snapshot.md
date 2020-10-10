---
title: "Snapshot 만들기"
metaTitle: "카카오톡 개발 커뮤니티 오픈 채팅방 리스트 모음집"
metaDescription: "카카오톡 개발 커뮤니티 오픈 채팅방 리스트 정리 되어 있음"
---

# 1. Getting Started
- Vagrant Snapshot (스냅샷) 저장하는 방법에 대해 저장되어 있음
<br/>

# 2. 사용 방법
- Snapshot 저장하기
    - 현재 시간으로 Snapshot 저장하기
        - 저장 이름 포맷
            ```bash
            ## push_<타임스탬프>
            push_1588776571_8185
            ```
        - 명령어
            ```bash
            vagrant snapshot push
            ```
        - 결과
            ![ex_screenshot](./assets//vagrant_snapshot_push.png)

    - Snapshot 이름 지정하여 저장하기
        - 명령어
            ``` bash
            # vagrant snapshot save '가상머신 ID' 'Snapshot 이름'
            vagrant snapshot save bf66842 'Snapshot_Test'
            ```
        - 결과
            ![ex_screenshot](./assets//vagrant_snapshot_save.png)

- Snapshot List 확인하기
    - 명령어
        ```bash
        vagrant snapshot list
        ```
    - 결과
        ![ex_screenshot](./assets//vagrant_snapshot_list.png)

- Snapshot 복구하기 (Restore)
    - 명령어
        ``` bash
        vagrant snapshot restore <Snapshot ID>
        ```
    - 결과
        ![ex_screenshot](./assets//vagrant_snapshot_restore.png)

