from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_users():
    return [
        {
            "id": 1,
            "name": "Salim 1111222",
            "role": "Developer"
        },
        {
            "id": 2,
            "name": "Alex",
            "role": "DevOps"
        },
        {
            "id": 3,
            "name": "Sarah",
            "role": "Data Engineer"
        }
    ]
