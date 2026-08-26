from fastapi import FastAPI, Response, status
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/health")
def health_check(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"status": "healthy"}
