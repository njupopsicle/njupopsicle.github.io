# 配置SSH免密登录服务器（支持跳板机）

假设你有两台Linux服务器A40和A800，但是它们只有内网地址，需要通过跳板机jump来登录. 本文介绍如何在Windows系统使用SSH来免密登录内网服务器.

### 第1步：生成ssh密钥

Windows10以上的系统通常会自带OpenSSH. 打开Powershell或cmd，输入

```shell
ssh-keygen -t rsa -C 'your_email'
```

其中`-t`指定密钥类型为`rsa`，`-C`为注释，并非必须.  命令执行后连按三个回车，`C:\Users\your_username\.ssh\`目录下会生成`id_rsa`和`id_rsa.pub`两个文件，前者为私钥，后者为公钥.

### 第2步：复制公钥到服务器

用账号密码登录跳板机jump，登录命令为

```shell
ssh -p ssh_server_port username@jumper_ip
```

`-p`后面的参数是服务器的ssh端口号，默认为22（可省略），也可能是事先配置好的端口号.

然后将公钥`id_rsa.pub`传输到跳板机jump的`~/.ssh/`目录（推荐使用FileZilla），执行`mv id_rsa.pub authorized_keys`. 注意，新用户的用户目录下可能没有`.ssh`目录，这时候只需执行`ssh localhost`命令，登录后再exit即可.

接下来如法炮制，将跳板机上的公钥复制给A40和A800服务器，由于它们共享内网，可使用下面的命令传输（保证内网服务器的`~/.ssh`目录存在）：

```shell
scp .ssh/id_rsa.pub a40_username@a40_ip:~/.ssh/id_rsa.pub
```

执行scp命令后会让你输入内网服务器的密码，然后在跳板机用账号密码登录内网服务器，将公钥改名`authorized_keys`即可.

### 第3步：配置本地ssh文件

在自己的Windows主机编辑文件`C:\Users\your_username\.ssh\config`，添加下面的信息

```
# 跳板机
Host jump
    HostName jumper_public_ip
    User jumper_username
    Port jumper_ssh_port
    IdentityFile "C:\Users\your_username\.ssh\id_rsa"

# 服务器a40
Host a40
    HostName a40_local_ip
    User a40_username
    IdentityFile "C:\Users\your_username\.ssh\id_rsa"
    ProxyCommand ssh -W %h:%p jump

# 服务器
Host a800
    HostName a800_local_ip
    User a800_username
    IdentityFile "C:\Users\your_username\.ssh\id_rsa"
    ProxyCommand ssh -W %h:%p jump
```

保存并退出，打开终端，输入命令`ssh a800_username@a800`，

![image-20231121014006994](assets/image-20231121014006994.png)

出现welcome信息和新的prompt即为成功~

![image-20231121014230826](assets/image-20231121014230826.png)
