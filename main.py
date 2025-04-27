from fastapi import FastAPI
import crud

app = FastAPI()


@app.get("/")
def get_all_users():
    return crud.get_all_users()


