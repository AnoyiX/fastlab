from fastlab.routers import HealthzRouter

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
app.include_router(HealthzRouter)


client = TestClient(app)
response = client.get("/healthz")
assert response.status_code == 200
