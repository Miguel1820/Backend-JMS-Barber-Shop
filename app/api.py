from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, db

app = FastAPI()

@app.get("/appointments")
def get_appointments(db: Session = Depends(db.get_db)):
    return db.query(models.Appointment).all()

@app.post("/appointments")
def create_appointment(appointment: models.Appointment, db: Session = Depends(db.get_db)):
    db.add(appointment)
    db.commit()
    return {"message": "Appointment created"}

@app.get("/services")
def get_services(db: Session = Depends(db.get_db)):
    return db.query(models.Service).all()

@app.get("/static/{image_id}")
def get_image(image_id: str):
    return {"message": f"Serving image {image_id}"}
