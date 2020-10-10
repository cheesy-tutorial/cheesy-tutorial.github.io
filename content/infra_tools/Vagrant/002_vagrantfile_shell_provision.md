---
title: "Vagrantfile Shell Provision 적용하기"
metaTitle: "카카오톡 개발 커뮤니티 오픈 채팅방 리스트 모음집"
metaDescription: "카카오톡 개발 커뮤니티 오픈 채팅방 리스트 정리 되어 있음"
---

# 1. Vagrantfile에 추가하기
- Vagrantfile
    ``` ruby
        config.vm.provision "shell", inline: <<-SHELL
            sudo yum update -y
            sudo yum install httpd -y
        SHELL        
    ```
    ![ex_screenshot](./assets//vagrantfile_shell.png)

# 2. Vagrant 재시작
``` bash
vagrant reload --provision
```
![ex_screenshot](./assets//vagrantfile_shell_up.png)