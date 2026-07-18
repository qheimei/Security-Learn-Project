import requests

url="http://localhost:11434/api/generate"
data={"model":"llama3:8b","prompt":"请用中文简单介绍一下什么是渗透测试","stream":False}
response=requests.post(url,json=data,timeout=90,proxies={"http":None,"https":None})
print(response.status_code)
result=response.json()
print(result["response"])