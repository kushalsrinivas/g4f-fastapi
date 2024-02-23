from fastapi import FastAPI,HTTPException,status
from fastapi.params import Body
import g4f
app = FastAPI()


@app.get('/')
async def root():
    return {"message": "hello world"}


def getChat(query):
    response = g4f.ChatCompletion.create_async(
        model="gpt-4-32k-0613",
        provider= g4f.Provider.Bing,
        messages=[{"role": "user", "content": query}],
        stream=False
    )
    return response


@app.post('/chatcompletion')
async def create_post(payload: dict = Body(...)):
    if 'query' not in payload.keys():
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail=f"no query found")
    response = await getChat(payload["query"])
    return {"message": response}