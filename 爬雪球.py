import requests
# res = requests.get("https://stock.xueqiu.com/v5/stock/quote.json?symbol=.IXIC&extend=detail")
# print(res.text) # 403 Forbidden

url = "https://stock.xueqiu.com/v5/stock/quote.json?symbol=.IXIC&extend=detail"
myheader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Referer" : "https://xueqiu.com/S/.IXIC",
    "Cookie" : "xq_a_token=c2aefa380b9072a563e961143570e259329d659f; xqat=c2aefa380b9072a563e961143570e259329d659f; xq_r_token=2823a23fcab28b5723fbd7c5220a4ba4cc755a52; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxODg0NDcxMiwiY3RtIjoxNzE3MDY1MTM4ODE4LCJjaWQiOiJkOWQwbjRBWnVwIn0.JifoTwvN6JvnDlspiczUaf48apjXnpieB46hNOpQej8qW3bxDGOKgQYdG0T9WkbqCpZyW5kt0vxKpp9pp_eQ-uDyKAoUEkuNyaxacFUHetNXHyOzPJ3DAmz0KEFFOF6_wSyXpARe6VY1koDtlH_SrRw0xQZ9oMYCunSc_HY9nzu6kAa4hDMfwbQcejJxTwsJ1QhNSjuqR3nkyU0_tpJSz3HuR5elQlM-J8-P1iM94QOZ0j1MxDpjgkw3jhafgT-xqzBZ94M4hXNBhZmhCkNgrESDllyh_zIpQey0w69G4zlVcaB2rNLoUYKVDqOUdW00TC7TFYLdrDxrNypNBN9JEw; cookiesu=651717065183556; u=651717065183556; Hm_lvt_1db88642e346389874251b5a1eded6e3=1717065184; device_id=88dbcd05043710b51ca336fd680d4817; is_overseas=0; s=al12fpjl9u; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1717065271"
}
res = requests.get(url,headers=myheader)    # JSON format
print(res.text)

# http 请求包里最核心的部分  get 的数据，请求体中的数据