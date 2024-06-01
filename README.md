获取企查查上地级市的一些数据

# 文件说明
|file or folder|descriprion|
|-|-|
|data|存储数据文件夹|
|requests_version|使用requests库的实现，尚未完成|
|main.ipynb|使用selenium库的实现|
|provinces.json|中国省、直辖市、自治区列表，不含港澳台|

# 准备
1. Python环境
```
conda create --name qcc python=3.9.19
conda activate qcc
pip install -r requirements.txt
```
2. Selenium使用以及安装浏览器Driver（以Chrome为例）
[selenium使用](https://blog.csdn.net/wenxiaoba/article/details/128654854)
注意chromedriver版本问题，[较新版本的chromedriver](https://blog.csdn.net/weixin_42486623/article/details/132734585)
[关于新版本selenium定位元素报错：‘WebDriver‘ object has no attribute ‘find_element_by_id‘等问题](https://blog.csdn.net/m0_49076971/article/details/126233151)

# 使用
运行`main.ipynb`

