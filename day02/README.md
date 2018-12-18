# 오늘배운내용

# day 02

## git 설정

* `git init`: git 초기화, git으로 관리하겠다!
* `git config --global user.name 'Yun jongwon'`
* `git config --global user.email 'dmdmdkdk@daum.net'`
* `git remote add origin 주소` :원격 저장소 등록
  * `git remote set-url origin  주소`: 원격 저장소 수정

## git

* `git status` : 현재 git으로 관리되고 있는 폴더의 상태
* `git add .`:현재 폴더의 변경사항들을  commit  하기 위해서 준비
* `git commit -m "day02입니다"` : commit,변경사항 저장,메세지는 자유롭게 작성가능
* `git push -u origin master` : remote 로 등록된 원격저장소(remote repository)
  * 이후에는 `git push` 명령어만 입력해도 동작합니다.



* markdown 기록할 것입니다.
  * typora or vscode

* github student developer pack



## vscode

* ctrl+` : 터미널보기

* ctrl+/: 주석처리

* $ mv *.txt day02/dummy/  :vscode 파일옮기기



  ```
  ctrl+shift+p
  ```

  - vscode에서 shell검색

  - select default shell

  - git bash

  - 실행할 때 tab 치면 파일명 한번에 자동완성




### 파일명변경

* import os

1. `os.chdir(r'폴더주소')`

2. `os.listdir('.')`:현재 working directory의 파일목록리스트

3. `os.rename('바꾸려고 하는 원래 이름','바꿀 이름')`

4. string.replace('바꾸고자 하는 부분','그 부분을 무엇으로 바꿀지')









