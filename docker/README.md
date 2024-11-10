## JSON转鸿蒙ArkTS（Interface/Class）的api-docker镜像

### 【可选】构建api正式包
```shell
docker build . -t samge/json2arkts -f docker/Dockerfile
```

### 【可选】上传
```shell
docker push samge/json2arkts
``` 

### 运行docker镜像
```shell
docker run -d \
--name json2arkts \
-p 7860:7860 \
--pull=always \
--restart always \
samge/json2arkts:latest
```
