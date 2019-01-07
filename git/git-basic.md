# Git & GitHub

##  Git에 내 정보 설정

- `$ git config --global user.name 'jong won' ` : 이름 설정
- `$ git config --global user.email 'dmdmdkdk@daum.net'                            ` : 이메일 설정
- ` git config --global --list` : 정보 설정 확인

## Git repo를 처음 생성한 경우

- `git init`: git 초기화. 지금 폴더를 git으로 관리하겠다!(관리하려는 폴더 안에서 입력)
- `git remote add origin 주소`:원격 저장소(remote repository) 주소 등록
  * `git remote set-url origin 주소`:원격저장소 수정
  * 

## Git repo clone 한 경우

- ` git clone 주소 만들폴더이름`: 이 주소로 부터 내용 내려받기

  - 이 경우에는 `git init, git remote add origin`  주소를 하지 않아도 이미 다 되어있다.


#  Git commit & push

- `git status`:현재 폴더의 git 상태 확인

- `git add .` : 현재 폴더의 변경사항들을 commit하기 위하여 준비 `.` 대신에 특정 파일 이름도 가능
- `git commit -m '메세지'`: commit, 변경사항저장
- `git push -u origin master ` : remote로 등록된 원격저장소에 commit한 것들 올리기
  - 이 후에는 git push만 입력해도 동작. `git clone`을 한 경우에도 해당

# Git&GitHub 재설정

``` bash
# Git 이름, 이메일 재설정
git config --global user.name 'jongwon'
git config --global user.email 'dmdmdkdk@daum.net'

#GitHub 로그인 정보 초기화
git credential reject
protocol=https
host=github.com
```