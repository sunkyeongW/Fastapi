# FastAPI
    웹 프레임워크 종류.
    openAPI 기반, 자동문서 생성.

    boolean일 경우(True, False)의 경우 소문자,대문자 둘다 사용 가능.



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

# httpie
    http 요청을 생성하는 도구.
    http : 호스트넘버
    개발한 API를 빠르게 확인 할 수 있는 장점이 있음.

# 경로 매개변수(Path parameters)
    URL 경로에 들어가는 변수를 의미.
    URL 전체적으로 문자열로 해석됌 -> 정수형으로 명시 해줘야됌.
    경로 순서에 영향을 줌.
    
# 쿼리 매개변수(Query parameters)
    호스트 주소 뒤에 오는 변수.
    각 매개변수는 '&' 기호로 구분되고 key=values로 정의.
    = None 을 이용하면 선택적으로 변환 가능(Optional)

# 문자열 열거형
    매개변수로 enum 클래스를 상속받아 파이썬 클래스로 만듬. 

# pydantic으로 요청 본문 받기(request)
    User(class): pydantic.BaseModel을 상속하는 데이터 모델.
    입력값 : http :8000/users name=sun password=123
    출력값 :
            HTTP/1.1 200 OK                       
            content-length: 49
            content-type: application/json     
            date: Thu, 21 Jul 2022 07:32:38 GMT     
            server: uvicorn

            {                                       
                "avatar_url": null,
                "name": "sun",
                "password": "123" 
            }  

# response Model(응답)    
    response_model = class.
    응답코드 201 - status_code=201 추가.
        201의미: 요청이 성공적으로 처리되서 리소스가 만들어졌음을 의미.



    





