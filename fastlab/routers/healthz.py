from fastapi import APIRouter

HealthzRouter = APIRouter()


@HealthzRouter.get("/healthz")
async def healthz():
    return ''
