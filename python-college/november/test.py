from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/hello/{name}")
def hello(name):
    if name == "Gulnara":
        raise HTTPException(status_code=404, detail="Ne naidena potonushto ty protivniy")
    if name == "Gulnara":
        raise HTTPException(status_code=404, detail= "Ne naidena potonushto ty protivniy")
    return f"hello {name}"


@app.get("/square")
def hello(s: int):
    return s**2

