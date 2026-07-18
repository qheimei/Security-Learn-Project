**## 一、目录操作命令**

**### pwd**

\- 功能：查看当前所在路径

\- 常用示例：

&#x20; ```bash

&#x20; pwd

&#x20; **# 输出：/home/centos7**

**### cd /**

&#x20;- 切换到根目录

&#x20;- 常用实例：

&#x20; ```bash

&#x20; cd /

&#x20; **# 输出： \[centos7@centos7-base /]$ \_**

**### cd \~**

&#x20;- 功能：切换到当前用户家目录

&#x20;- 常用实例：

&#x20; ```bash

&#x20; cd \~

&#x20; **# 输出：\[centos7@centos7-base \~]$ \_**

**### cd ..**

&#x20;- 功能：返回上一级目录

&#x20;- 常用实例：

&#x20; ```base

&#x20; cd ..

&#x20; **# 输出：\[centos7@centos7-base home]$ \_**

**### cd /etc**

&#x20;- 功能：切换到/etc目录

&#x20;- 常用实例：

&#x20; ```bash

&#x20; cd /etc

&#x20; **# 输出：\[centos7@centos7-base etc]$ \_**

**### ls**

&#x20;- 功能：查看当前目录文件

&#x20;- 常用实例：

&#x20; ```bash

&#x20; ls

&#x20; **# 输出：（多个文件名，此处省略）**

**### ls -l**

&#x20;- 功能：查看详细信息

**### ls -a**

&#x20;- 功能：查看隐藏文件



**## 二、文件操作命令**

**### touch test.txt**

&#x20;- 功能：创建空文件

&#x20;- 常用实例：

&#x20; ```bash

&#x20; touch test.txt

&#x20; **# 输出：无**

**### cat test.txt**

&#x20;- 功能：查看文件内容

&#x20;- 常用实例：

&#x20; ```bash

&#x20; cat test.txt

&#x20; **# 输出：无**

**### head -5 test.txt**

&#x20;- 功能：查看前5行

&#x20;- 常用实例：

&#x20; ```bash

&#x20; head -5 test.txt

&#x20; **# 输出：无**

**### tail -5 test.txt**

&#x20;- 功能：查看最后5行

&#x20;- 常用实例：

&#x20; ```bash

&#x20; tail -5 test.txt

&#x20; **# 输出：无**

**### cp test.txt /tmp/**

&#x20;- 功能：复制文件到/tmp目录

&#x20;- 常用实例：

&#x20; ```bash

&#x20; cp test.txt /tmp

&#x20; **# 输出：无**

**### cp -r dir1 /tmp/**

&#x20;- 功能：复制目录

&#x20;- 常用实例：

&#x20; ```bash

&#x20; cp -r dir1 /tmp

&#x20; # 输出：无

\### mv test.txt new.txt

&#x20;- 功能：重命名文件

&#x20;- 常用实例：

&#x20; ```bash

&#x20; mv test.txt new.txt

&#x20; **# 输出：无**

**### mv new.txt /tmp/**

&#x20;- 功能：移动文件

&#x20;- 常用实例；

&#x20; ```bash

&#x20; mv new.txt /tmp/

&#x20; **# 输出：无**

**### rm /tmp/new.txt**

&#x20;- 功能：删除文件

&#x20;- 常用实例：

&#x20; ```bash

&#x20; rm /tmp/new.txt

&#x20; ls /tmp/new.txt

&#x20; **# 输出：no shuc file or directory**



**## 三、权限管理类命令**

**### r(读)=4**

&#x20;- 对应：所有者

**### w(写)=2**

&#x20;- 对应：所属组

**### x(执行)=1**

&#x20;- 对应：其他用户

**### chmod 755 test.txt**

&#x20;- 功能：设置文件权限为所有者读写执行、其他用户读执行

**### chmod 644 test.txt**

&#x20;- 功能：设置普通文件默认权限

**###chown secuser test.txt**

&#x20;- 功能：修改文件所有者为secuser



**## 四、系统基础信息类命令**

**### whoami**

&#x20;- 功能：查看当前登录用户

&#x20;- 常用实例：

&#x20; ```bash

&#x20; whoami

&#x20; **# 输出：centos7**

**### hostname**

&#x20;- 功能：查看主机名

&#x20;- 常用实例：

&#x20; ```bash

&#x20; hostname

&#x20; **# 输出：centos7-base**

**### df -h**

&#x20;- 功能：查看磁盘使用情况

&#x20;- 常用实例：

&#x20; ```bash

&#x20; df -h

&#x20; # 输出：(此处省略)

**### uname -a**

&#x20;- 功能：查看系统内核信息

&#x20;- 常用实例：

&#x20; ```bash

&#x20; uname -a

&#x20; # 输出：Linux centos7-bash （后面详细数据省略）

**### free -h**

&#x20;- 功能：查看内存使用情况

&#x20;- 常用实例：

&#x20;```bash

&#x20; free -h

&#x20; # 输出：（此处省略详细信息）

