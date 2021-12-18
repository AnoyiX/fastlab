from fastapi import APIRouter

HealthRouter = APIRouter()


@HealthRouter.get("/health")
async def healthz():
    return ''
