from fastapi import FastAPI
from vodex.routers import items, clock_in
from vodex.database import initialize_database
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await initialize_database()  # Await the database initialization

app.include_router(items.router)
app.include_router(clock_in.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI CRUD Application"}

@app.get("/health")
async def health_check():
    return {"status": "Healthy"}

if __name__ == "__main__":
    uvicorn.run("vodex.main:app", host="127.0.0.1", port=8000, reload=True)

