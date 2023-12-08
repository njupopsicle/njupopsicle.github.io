# 如何让深度学习程序后台运行

我们通常在笔记本上用SSH连接远程服务器做深度学习. 这样如果SSH连接断了，终端被kill掉，深度学习程序也会随之终止，带来许多麻烦. Linux系统上有一个软件screen可以让python程序后台运行，这样即使断网也不会有什么影响. 执行命令

```shell
apt update
apt install screen
```

来安装screen. 使用下面的命令创建并进入一个screen会话

```shell
screen -S session_name
```

在screen会话中执行深度学习脚本

```shell
python train.py
```

按ctrl+A,ctrl+D退出会话，回到终端. 用命令 `screen -ls`查看现有的screen会话，`screen -r session_name`回到会话.
