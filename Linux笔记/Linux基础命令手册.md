## 一、目录操作命令
### pwd
- 功能：查看当前所在路径
- 常用示例：
  ```bash
  pwd
  # 输出：/home/centos7
### cd /
 - 切换到根目录
 - 常用实例：
  ```bash
  cd /
  # 输出： [centos7@centos7-base /]$ _
### cd ~
 - 功能：切换到当前用户家目录
 - 常用实例：
  ```bash
  cd ~
  # 输出：[centos7@centos7-base ~]$ _
### cd ..
 - 功能：返回上一级目录
 - 常用实例：
  ```base
  cd ..
  # 输出：[centos7@centos7-base home]$ _
### cd /etc
 - 功能：切换到/etc目录
 - 常用实例：
  ```bash
  cd /etc
  # 输出：[centos7@centos7-base etc]$ _
### ls
 - 功能：查看当前目录文件
 - 常用实例：
  ```bash
  ls
  # 输出：（多个文件名，此处省略）
### ls -l
 - 功能：查看详细信息
### ls -a
 - 功能：查看隐藏文件

## 二、文件操作命令
### touch test.txt
 - 功能：创建空文件
 - 常用实例：
  ```bash
  touch test.txt
  # 输出：无
### cat test.txt
 - 功能：查看文件内容
 - 常用实例：
  ```bash
  cat test.txt
  # 输出：无
### head -5 test.txt
 - 功能：查看前5行
 - 常用实例：
  ```bash
  head -5 test.txt
  # 输出：无
### tail -5 test.txt
 - 功能：查看最后5行
 - 常用实例：
  ```bash
  tail -5 test.txt
  # 输出：无
### cp test.txt /tmp/
 - 功能：复制文件到/tmp目录
 - 常用实例：
  ```bash
  cp test.txt /tmp
  # 输出：无
### cp -r dir1 /tmp/
 - 功能：复制目录
 - 常用实例：
  ```bash
  cp -r dir1 /tmp
  # 输出：无
### mv test.txt new.txt
 - 功能：重命名文件
 - 常用实例：
  ```bash
  mv test.txt new.txt
  # 输出：无
### mv new.txt /tmp/
 - 功能：移动文件
 - 常用实例；
  ```bash
  mv new.txt /tmp/
  # 输出：无
### rm /tmp/new.txt
 - 功能：删除文件
 - 常用实例：
  ```bash
  rm /tmp/new.txt
  ls /tmp/new.txt
  # 输出：no shuc file or directory

## 三、权限管理类命令
### r(读)=4
 - 对应：所有者
### w(写)=2
 - 对应：所属组
### x(执行)=1
 - 对应：其他用户
### chmod 755 test.txt
 - 功能：设置文件权限为所有者读写执行、其他用户读执行
### chmod 644 test.txt
 - 功能：设置普通文件默认权限
###chown secuser test.txt
 - 功能：修改文件所有者为secuser

## 四、系统基础信息类命令
### whoami
 - 功能：查看当前登录用户
 - 常用实例：
  ```bash
  whoami
  # 输出：centos7
### hostname
 - 功能：查看主机名
 - 常用实例：
  ```bash
  hostname
  # 输出：centos7-base
### df -h
 - 功能：查看磁盘使用情况
 - 常用实例：
  ```bash
  df -h
  # 输出：(此处省略)
### uname -a
 - 功能：查看系统内核信息
 - 常用实例：
  ```bash
  uname -a
  # 输出：Linux centos7-bash （后面详细数据省略）
### free -h
 - 功能：查看内存使用情况
 - 常用实例：
 ```bash
  free -h
  # 输出：（此处省略详细信息）