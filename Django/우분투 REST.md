# d /rwx /r-x/r-x

d -> 파일인지 폴더인지

첫번째 rwx 파일소유자 읽고 쓰고 실행

두번째 rwx 그룹에 속하는 사람

세번째 rwx 나머지

# REST

#### REST의 구성

- 자원(Resource) -URI

- 행위(Verb)-HTTP  Method

- 표현(Representations)

  # REST 디자인 가이드

  1. URI는 정보의 자원을 표현해야한다.
  2. 자원에 대한 행위는 HTTP Method(GET,POST,PUT,DELETE)로 표현한다.

  ### 예시

  ```html
  GET /movies/show/1 (x)
  GET /movies/1 (o)
  ```

  ``` 
  GET /movies/create (x) -GET Method는 자원생성에 부적합
  POST /movies (o)
  ```

  ```
  GET /movies/2/update(x) -GET 부적합
  PUT /movies/2 (o)
  ```

  ```
  GET /movies/2/edit - 수정페이지 보여줌
  POST /movies/2/edit - 수정 작업을 수행함
  ```
