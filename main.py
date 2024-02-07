import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get("/")
def on_route():
    return "200 ON"


@app.get("/example/")
def example():
    return "Example"


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)