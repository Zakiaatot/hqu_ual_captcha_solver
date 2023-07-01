from captchaSolver import detect_displacement
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CaptchaData(BaseModel):
    bigImage: str
    smallImage: str
    canvasWidth: int


class ReturnData(BaseModel):
    code: int
    msg: str


@app.get("/")
async def root():
    return ReturnData(code=400, msg='Please use post!')


@app.post("/")
async def solver(captchaData: CaptchaData):
    res = detect_displacement(captchaData.smallImage,
                              captchaData.bigImage, captchaData.canvasWidth)
    return ReturnData(code=res['code'], msg=res['msg'])
