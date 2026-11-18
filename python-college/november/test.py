from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/hello/{name}")
def hello(name: str):
    if name == "Gulnara":
        raise HTTPException(status_code=404, detail="Stranitsa ne naidena potonushto ty protivniy")
    return f"Hello {name}"

@app.get("/square")
def square(s: int):
    return s/0

