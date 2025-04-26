from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API online com FastAPI!"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print("Webhook recebido:", data)

    return {"status": "Recebido com sucesso", "data": data}
