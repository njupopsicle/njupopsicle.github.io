# 如何手动给docker容器分配IP地址

```shell
docker network create --subnet='192.168.0.0/24' net_name #创建子网，指定其CIDR和子网名称
docker network disconnect bridge container_name #断开container的桥接网络
docker network connect --ip=192.168.0.3 net_name container_name #将container连接到新建net并指定ip
```
