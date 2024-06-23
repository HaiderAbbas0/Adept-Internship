from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/length-of-prompt")

def promptLen(prompt: str = Query(...)):
    return {"Prompt given": prompt, " Length of prompt": len(prompt)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2000)
