# 设置基础镜像
FROM python:3.10-slim-buster

# 配置代理
ARG PROXY
ENV http_proxy=${PROXY} https_proxy=${PROXY}

# 将工作目录设置为 /app
WORKDIR /app

# 复制当前目录中的所有文件到 /app
COPY . .

# 安装所需的 Python 包
RUN pip install -r requirements.txt

# 声明容器监听的端口
EXPOSE 7860

# 清空代理
ENV http_proxy='' https_proxy=''

# 运行应用程序
ENTRYPOINT ["python", "app.py"]
