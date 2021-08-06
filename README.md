# <center>终端调试输出小程序</center>



## 介绍

很多开发调试过程中, 开发者会面临print输出来debug代码问题; 以往会使用直接print函数打印，如果遇到多条数据打印，则使用for循环这种迭代方式。但都会存在一个问题，会将terminal满屏打满调试信息，可能个别情况下，我们仅需要的调试信息只有最新的输出的一条，如果每次print, terminal终端上只显示最新的一条，这样就会变的很简洁。  给大家介绍的这个 `terminal-debug-print` 小工具，就是解决调试中上述描述的问题。




## 使用

```shell
python tprint.py
```

