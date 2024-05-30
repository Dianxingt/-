# Pyhon 爬虫初步

response = requests.get("https://www.baidu.com/")    # send get request and get the response
print(response)
print(response.status_code)   # 200 means success
print(response.headers)   
print(response.text)    # html of the website, 被做了反爬，就得不出来真正的html, 百度会对非浏览器的请求进行反扒
print(response.content) # bytes of the website， 用于视频和图片

数据包格式
get / https
头                 request没有浏览器给的那么多头！！区别！！只有几个
空行

response = requests.get("https://www.baidu.com/",headers=myheader) headers即可增加get的头部分（浏览器会检测这个部分来防止非浏览器）

myheader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Referer" : "https://xueqiu.com/S/.IXIC",
    "Cookie" : "xq_a_token=c2aefa380b9072a563e961143570e259329d659f; xqat=c2aefa380b9072a563e961143570e259329d659f; xq_r_token=2823a23fcab28b5723fbd7c5220a4ba4cc755a52; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxODg0NDcxMiwiY3RtIjoxNzE3MDY1MTM4ODE4LCJjaWQiOiJkOWQwbjRBWnVwIn0.JifoTwvN6JvnDlspiczUaf48apjXnpieB46hNOpQej8qW3bxDGOKgQYdG0T9WkbqCpZyW5kt0vxKpp9pp_eQ-uDyKAoUEkuNyaxacFUHetNXHyOzPJ3DAmz0KEFFOF6_wSyXpARe6VY1koDtlH_SrRw0xQZ9oMYCunSc_HY9nzu6kAa4hDMfwbQcejJxTwsJ1QhNSjuqR3nkyU0_tpJSz3HuR5elQlM-J8-P1iM94QOZ0j1MxDpjgkw3jhafgT-xqzBZ94M4hXNBhZmhCkNgrESDllyh_zIpQey0w69G4zlVcaB2rNLoUYKVDqOUdW00TC7TFYLdrDxrNypNBN9JEw; cookiesu=651717065183556; u=651717065183556; Hm_lvt_1db88642e346389874251b5a1eded6e3=1717065184; device_id=88dbcd05043710b51ca336fd680d4817; is_overseas=0; s=al12fpjl9u; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1717065271"
}

post  /trans http
请求头
空行
请求体 i=你好&from=zh-CHS&to=EN

  response = requests.post(url, data={
    "q": word,
    "from": "Auto",
    "to": "Auto"
  })

  post请求中 data是 请求体 ， para用于参数 
