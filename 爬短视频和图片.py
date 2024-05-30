import requests

response = requests.get('http://img.netbian.com/file/2024/0527/000426jUv2G.jpg')
with open ('1.jpg', 'wb') as f:
    f.write(response.content)