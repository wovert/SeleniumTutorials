# 自动化测试-[零壹码博客](https://lingyima.com)

## 软件开发流程

1. 需求分析
2. 架构模块设计
3. 编码
4. 测试: 单元测试 => 集成测试 => 系统测试 => 验收

## 测试分类

1. 功能测试：检查实际的功能是否符合用户的需求
2. 性能测试：通过自动化的测试工具模拟多种正常、峰值以及异常负载条件来对系统的各项性能指标进行测试
3. 手工测试：指定case, 测试工程师一步一步去测试
4. 自动化测试：把以人为的驱动测试行为转换为机器执行的过程

## 自动化测试有点

1. 程序的回归测试更方便。程序修改比较频繁时，效果是非常明显的。
2. 运行更多繁琐的测试
3. 执行手工测试困难或不可能进行的测试
4. 更好的利用资源
5. 一致性和可重复性及测试用例的复用
6. 增加被测试软件的可靠性

## 适合自动化测试场景

1. 任务测试明确，不会频繁变动
2. 软件需求变更少
3. 项目周期长，测试脚本可以复用

## 常用测试工具

QTP：回归测试和测试同一软件的新版

Robot Framework: python编写的功能自动化测试框架，良好的可扩展性

selenium: 用于Web应用程序测试的工具，支持多平台、多浏览、多语言的去实现自动化测试

## selenium 简介

1. 开源软件
2. 支持主流浏览器：FF,Chrome,IE
3. 跨平台：windows,Linux,Mac
4. 多语言：Java, Python, Ruby，PHP, JS
5. 对 Web 支持良好，丰富简单的 API

## Web 调试工具介绍与开发环境搭建

1. 官网下载 `https://www.python.org/`

2. 安装 pip: `https://pypi.python.org/pypi/pip`;
  解压pip-version目录之后 执行 `python setup.py install`

3. 安装 selenium: `pip install -U selenium`

4. 使用selenium 打开 Firefox 浏览器

``` Python
from selenium from webdriver
borwser = webdriver.Firefox()
borwser.quit()
```

安装了python3，使用pip安装了selenium，但是在使用时，报了“selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.”

方法二：下载geckodriver.exe

下载地址：`https://github.com/mozilla/geckodriver/releases`，根据自己的电脑，下载的 win64 位的

在firefox的安装目录下，解压 `geckodriver`，然后将该路径添加到path环境变量下，不报这个错了

- Firefox 前段工具
  - firebug 先改为 **Firefox Development Edition**

``` Python
from selenium import webdriver
b = webdriver.Chrome()

```

- 安装 chrome 浏览器 webdriver
1. setup Chrome
2. [chromedriver.exe](http://npm.taobao.org/mirrors/chromedriver/)
3. chromedriver.exe 解压到 `C:\Program Files\Chrome\Application` 目录下
4. 配置环境变量

``` python
# 打开网页
b.get('http://www.baidu.com)
# 输入title
b.title
# 是否包含 百度字符串
'百度' in b.title
# 在浏览器打开地址 http://www.f.cc
b.current_url

```

## 元素定位

- 元素名称      | webdriver API
- id           | find_element_by_id()
- name         | find_element_by_name()
- class name   | find_element_by_class_name()
- tag name     | find_element_by_tag_name() 紧返回第一个标签
- link text    | find_element_by_link_text()
- partial link text | find_element_by_partial_link_text()
- xpath        | find_element_by_xpath()
- css selector | find_element_by_css_selector()

- find_element("id|name", "value")

- 元素操作
- clear() 清楚元素内容
- send_keys('追加内容') 模拟按键输入
- click() 点击
- submit() 提交表单
- back()

## webdriver 模块对浏览器进行操作

``` Python
# 窗口全屏
b.maximize_window()
```

### web

### 代码测试

### 移动(Android/IOS)

### 数据库

## 自动化工具 selenium

## 自动化测试报告整理

### log

### excel

### mail

## 测试用例
