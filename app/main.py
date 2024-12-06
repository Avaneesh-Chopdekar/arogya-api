from fastapi import FastAPI, status
from app.db import db

app = FastAPI()


@app.get(
    "/health",
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
def health_check():
    return {"message": "Server is up and running..."}


try:
    db.get_db().command("ping")
    print("Connected to database successfully.")
except Exception as e:
    print(f"Error connecting to database: {e}")
