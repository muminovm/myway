from fastapi import FastAPI, Response, status

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "SysAdmin API v2.0 is running!"}

@app.get("/health")
def health_check(response: Response):
    # Если сервер работает нормально, возвращаем 200 OK
    response.status_code = status.HTTP_200_OK
    return {"status": "healthy"}
