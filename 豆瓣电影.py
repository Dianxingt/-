import requests
# url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0"

# response = requests.get(url)

# print(response.text)    # empty

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0"

myheader = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Referer" : "https://movie.douban.com/"
}

# get j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0 http
# ...... 改变第一行的请求参数 
myparams = {
    "type":"movie",
    "tag" : "豆瓣高分",
    "page_limit":50,
    "page_start":0
}
response = requests.get(url,headers=myheader,params=myparams)
print(":::",response.text)
