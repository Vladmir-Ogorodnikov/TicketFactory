from fastapi import APIRouter
from api.shemas import HealthResponse

health_router = APIRouter()

@health_router.get("/health", tags = ["system"])
def get_health() -> HealthResponse:

    return HealthResponse(
        status = "ok",
        service = "cinema-booking-api",
        version = "1.0.0"
    )


