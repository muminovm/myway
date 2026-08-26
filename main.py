import asyncio
from fastapi import FastAPI, Response, status
from fastapi.responses import FileResponse

app = FastAPI()

SUBNET_PREFIX = "192.168.198"

async def ping_ip(ip: str):
    # Запуск утилиты ping в фоновом режиме (1 пакет, таймаут 1 сек)
    proc = await asyncio.create_subprocess_exec(
        "ping", "-c", "1", "-W", "1", ip,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL
    )
    await proc.wait()
    return {"ip": ip, "status": "online" if proc.returncode == 0 else "offline"}

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/health")
def health_check(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"status": "healthy"}

@app.get("/api/printers")
async def get_printers_status():
    # Сканируем диапазоны IP (от .1 до .50 - диапазон можно расширить до 254)
    tasks = [ping_ip(f"{SUBNET_PREFIX}.{i}") for i in range(1, 51)]
    results = await asyncio.gather(*tasks)
    return {"subnet": f"{SUBNET_PREFIX}.0/24", "devices": results}
