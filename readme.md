# FastAPI
    웹 프레임워크 종류.
    openAPI 기반, 자동문서 생성.



# 동기(Synchronous)
    서버에서 요청을 보냈을 때 응답이 돌아와야 다음 동작 수행.

# 비동기(Asynchronous) 
    서버에서 요청을 보냈을 때 응답 상태와 상관없이 다음 동작을 수행.


# uvicorn
    httptools를 사용하는 ASGI(비동기 파이썬 웹 서버) web server.
    code : uvicorn main:app --reload
        main - main.py 파일.
        app - main.py 파일에서 app.
        --reload : 파일에 변화가 생기면 재시작을 의미.

# starlette, pydantic
    FastAPI 설치 시 자동으로 설치.
    Starlette - FastAPI가 사용하는 웹 프레임워크.
    Pydantic - 애너테이션 타입을 사용해서 데이터를 검증하고 설정들을 관리하는 라이브러리.
    런타임 환경에서 타입을 강제하고 타입이 유효하지 않을 때 에러를 발생시켜줌.