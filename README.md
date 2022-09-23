# 基于Github Actions自动化打卡程序

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
