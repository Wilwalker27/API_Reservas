from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Reservas",
    description="API para sistema de reservas de restaurante",
    version="1.0.0",
)