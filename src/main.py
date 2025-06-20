from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .controllers import reservation_controller, table_controller

app = FastAPI(
    title="API de Reservas",
    description="API para sistema de reservas de restaurante",
    version="1.0.0",
) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir as rotas
app.include_router(
    reservation_controller.router,
    prefix="/reservations",
    tags=["reservations"]
)

app.include_router(
    table_controller.router,
    prefix="/tables",
    tags=["tables"]
)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Reservas"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)