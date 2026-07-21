# 批量端口查询Shell脚本
## 创建Shell脚本文件
脚本逻辑：
- 定义目标IP地址变量
- 定义需要检测的端口列表
- 使用循环遍历端口列表
- 通过nc命令检测端口是否开放
- 输出端口开放/关闭的对应结果

## 给脚本添加可执行权限

## 运行脚本，测试本地IP的指定端口连通性

## 调试脚本语法错误，优化输出格式

## 脚本源码：

target_ip="192.168.213.128"
port_list=(22 80 3306 8080 6379)
echo "========端口扫描开始========"
for port in ${port_list[@]}
do
    nc -zv -w 1 $target_ip $port > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "$target_ip : $port"
    else
        echo "$target_ip : $port"
    fi
done
echo "========端口扫描结束========"
 