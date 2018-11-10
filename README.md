# spike
京东、淘宝、小米商城等一系列的秒杀脚本。

>秒杀脚本是基于自动化测试库 [uiautomator2] (https://github.com/openatx/uiautomator2) 编写
。

#### 本文需要使用到的库或三方工具：

+ adb
+ uiautomator2
+ weditor
+ time

### 环境搭建

+ 安装adb

	下载 [adb](https://developer.android.com/studio/releases/platform-tools.html) 并且将其配置到环境变量，它是后面的基础。若没有配置好，后面步骤无法进行。

+ 安装 uiautomator2 

	这个是核心驱动器，先使用`pip install --pre uiautomator2`安装uiautomator2，再进行控制手机之前，先需要将打开开发者模式、usb调试的手机连接到电脑，再使用`python -m uiautomator2 init`初始化。这一步会安装一个守护进程（客户端、驱动）到手机，实先控制的目的。

+ 安装weditor

	安装`pip install --pre --upgrade weditor`，启动`python3 -m weditor`。启动之后会默认打开`http://atx.open.netease.com/`页面，这里就是一个交互式的手机控制器。这个是东西的一部分功能是实现了安卓原生`uiautomatorviewer`，并且支持点击、获取控件、发送指令的功能，能自动生成代码，大大地加快了开发速度，且功能十分强大。
	

关于环境搭建也可以查看 [这篇文章](https://testerhome.com/topics/11357) 里面已经讲述的十分清楚了.

#### 开发环境：

+ python3.6.5
+ pychram


感谢：

https://github.com/openatx/uiautomator2

https://testerhome.com/topics/11357
