from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from database import Base, engine
from routers import auth, turnos, servicios, barberos

load_dotenv()

app = FastAPI(
    title="JMS Barber Shop API",
    description="Sistema de gestión de turnos para barbería",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(turnos.router)
app.include_router(servicios.router)
app.include_router(barberos.router)


@app.get("/")
def read_root():
    return {"message": "JMS Barber Shop API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
