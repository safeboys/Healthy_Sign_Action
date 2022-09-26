# 基于Github Actions自动化打卡程序

## 程序免责声明
* 作者 ByteSys
* 创建时间 2022/09/23 19:30:00
* 修改时间 2022/09/26 09:00:00
* 版本 Healthy_Sign_Action V1.1
* 本程序仅作为学习交流使用 请自觉遵守中华人民共和国相关法律

## 使用方法
* 点击右上角 `Fork` 项目;
* `Settings` -> `Secrets` -> `Actions` 添加USERNAME、PASSWORD、Server酱Push_Key
    - `USERNAME`：学生学号
    - `PASSWORD`：登录密码
    - `PUSH_KEY`：Server酱SendKey
* 点击`Star`,程序默认将在北京时间06:30自动运行,运行结果将通过Server酱推送至微信,`Actions`可查看程序运行信息;

## 获取Server酱SendKey
* 访问https://sct.ftqq.com/ 使用微信登录
* 在上方Key&API选项里复制SendKey值
