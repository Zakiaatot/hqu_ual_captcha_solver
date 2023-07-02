# HQU_UAL_CAPTCHA_SOLVER

## 华侨大学统一验证登录canvas滑动验证码解决方案 opencv

## 使用example

POST:

```json
{
    "bigImage": "base64  DATA",
    "smallImage": "base64 DATA",
    "canvasWidth": 280
}
```

RETURN:

```json
{
    "code":200,
    "msg": "computedValue"
}
```
