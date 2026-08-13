# 项目名称：Z2U 自动化测试框架

> 基于 Playwright + Pytest + Allure 的 Web 自动化测试项目

---

## 📖 项目简介

本框架用于 新Z2U 平台的测试环境核心流程及回归测试，覆盖订单、支付、用户中心等模块，旨在提升发布前的质量验证效率。

---

## 🛠 技术栈与环境要求

- **编程语言**：Python 3.8.3+
- **核心框架**：Pytest（测试用例管理）+ Playwright（浏览器自动化）
- **报告体系**：Allure（美观的测试报告）
- **配置管理**：PyYAML（测试数据与配置文件解析）

---

## 🚀 快速开始（环境搭建）

### 1. 克隆代码

```bash
git clone https://github.com/dxq0467-spec/NewZ2UTest.git
cd Z2UTest
```

### 2. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

### 3. 安装 Playwright 浏览器内核（必须执行）

```bash
playwright install
```

### 4. 配置 Allure 环境（可选，用于生成报告）

- **MacOS**：`brew install allure`
- **Windows**：`scoop install allure` 或 [手动下载](https://github.com/allure-framework/allure2/releases)
- 验证是否安装成功：`allure --version`

---

## ▶️ 运行测试用例

### 运行全部用例
```bash
pytest
```
### 运行指定模块（例如订单模块）
```bash
pytest Tests/order/
```
### 运行带标记的用例（例如冒烟测试）
```bash
pytest -m smoke
```
### 并行运行（加速执行）
```bash
pytest -n auto
```

---

## 📊 生成与查看 Allure 报告

### 1. 执行测试并收集原始数据

```bash
pytest --alluredir=./allure-results
```

### 2. 生成并打开 HTML 报告

```bash
allure generate ./allure-results -o ./allure-report --clean --lang zh --name "Z2U自动化测试报告"
```
```bash
allure open ./allure-report
```
---

## 📁 项目目录结构

```text
Z2UTest/
├── Config/               # 全局配置文件
├── Pages/                # 页面对象（POM 设计模式）
├── Tests/                # 测试用例（含 conftest.py）
├── Utils/                # 工具函数（如读取 YAML）
├── Data/                 # 测试数据（YAML 文件）
├── Base/                 # 基础类/公共方法封装
├── User/                 # 用户数据（JSON 格式）
├── reports/              # Allure 测试报告
│   ├── allure-results/   # 原始测试数据
│   └── allure-report/    # 生成的 HTML 报告
├── requirements.txt      # Python 依赖清单
├── pytest.ini            # Pytest 配置文件
└── README.md             # 项目说明文档
```
