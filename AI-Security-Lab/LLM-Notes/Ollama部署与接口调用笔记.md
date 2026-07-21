## 一、Ollama安装步骤与模型拉取命令

- 官网下载windows客户端：https://ollama.com/download
- 完成后打开PowerShell，执行模型拉取命令：ollama pull llama3:8b
- 在端口继续验证模型：ollama list
- 启动模型交互：ollama run llama3:8b
- 输入测试基础对话：请简单介绍一下什么是渗透测试
- 确认模型正常回复后输入/bye退出交互模式

## 二、本地API接口地址、请求参数说明

- 本地API接口地址：http://localhost:11434/api/generate （Ollama默认本地API）
- 请求体：model（模型名）、prompt（提示词）、stream（设为false关闭流式输出）

## 三、Python调用的完整流程与踩坑记录

Python代码的核心逻辑：
- 导入requests库
- 定义接口地址
- 构造请求体
- 发送POST请求，解析返回的JSON结果，打印模型回复内容
- 运行脚本，验证能正常获取模型回复，调试报错并记录问题
流程记录：
- 保证Ollama后台运行和已经下载了requests库、pyhton3的状况下，在文件的路径下打开PowerShell，输入：python ollama_basic_call.py
- 第一次运行结果：Read timed out（Read timeout=30）。说明读取超时，可以修改时间的限制更长，如timeout=90。修改完成后保存再次运行。
- 第二次运行结果：TypeError: 'method' object is not subscriptable。在检查完后发现脚本中有错误：result=response.json，修改为：result=response.json()。继续输入运行命令。
- 第三次运行结果：Read timed out。仍然读取超时，再次修改脚本，在timeout限制的后面加上：proxies={"http":None,"https":None}。保存后运行。
- 第四次运行结果成功输出llama3的渗透测试英文回答。
扩展：让回复内容为中文。修改脚本的提示词为“请用中文简单回答什么是渗透测试”，保存后运行，得到中文形式的渗透测试回答。

## 四、脚本

import requests

url="http://localhost:11434/api/generate"
data={"model":"llama3:8b","prompt":"请用中文简单介绍一下什么是渗透测试","stream":False}
response=requests.post(url,json=data,timeout=90,proxies={"http":None,"https":None})
print(response.status_code)
result=response.json()
print(result["response"])

