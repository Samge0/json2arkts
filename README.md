# JSON转鸿蒙ArkTS（Interface/Class）

## 描述
一个Gradio构建的简单应用，用户输入JSON，转为鸿蒙ArkTS的接口（Interface）或类（Class）。

## [docker运行>>](docker/README.md)

`--build`参数用于构建镜像。如果首次运行后内容没有修改，可以不使用该参数。
```shell
docker compose -f docker/docker-compose.yml -p json2arkts up -d --build
```

## 源码运行

- 克隆项目
```bash
git clone https://github.com/Samge0/json2arkts.git
```

- 进入项目目录
```bash
cd json2arkts
```

- 创建虚拟环境
```bash
conda create -n json2arkts python=3.10.13 -y
```

- 安装依赖
```bash
pip install -r requirements.txt
```

- 运行
```bash
python app.py
```

## 相关截图
![image](https://github.com/user-attachments/assets/b635a728-015d-4fd0-859c-f4ccac23cd90)

---

![image](https://github.com/user-attachments/assets/7527f071-88aa-4bc8-990c-9f54df5e137a)

---

![image](https://github.com/user-attachments/assets/24d65c5e-20a1-4e2f-ba68-37b576d7752f)

---

![image](https://github.com/user-attachments/assets/cbab5f90-405f-4b6e-8af9-0ae7615a50e3)


