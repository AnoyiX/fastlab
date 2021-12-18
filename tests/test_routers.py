from fastlab.routers import HealthRouter

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
app.include_router(HealthRouter)


client = TestClient(app)
response = client.get("/health")
assert response.status_code == 200
