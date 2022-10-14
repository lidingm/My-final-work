---
#3 Linux / WSL
---

## #1 在虚拟机软件中安装配置 Ubuntu 发行版

   首先当然是从网上寻找教程，了解到装用虚拟机首先需要下载 vmware，也了解到vmware是一款运行在windows系统上的虚拟机软件,可以虚拟出一台计算机硬件,方便安装各类操作系统。

   从官网上找到vmware下载，![img](https://img-blog.csdnimg.cn/030293d4339d4be09b34c0e2d3820227.png#pic_center)



其次选择免费的player![img](https://img-blog.csdnimg.cn/79fd70fee7204baa9b92111277a62dce.png#pic_center)

然后下载就成功了~![img](https://img-blog.csdnimg.cn/f0f0a6a5e9cf4e3b8efe7f7b36f9ffca.png#pic_center)

   之后下载Ubuntu的虚拟机，官网上找到最新版本的，![img](https://img-blog.csdnimg.cn/dfce51f44565424986a542deb677190d.png#pic_center)

下载后即可在vmware中创建虚拟机，![img](https://img-blog.csdnimg.cn/20d5439fd8ad42ad99026f9a741bc4ad.png#pic_center)        选择对应Ubuntu文件路径即可，之后在配置完硬盘内存（我给了10个G），选择地区中国shanghai，不断点击continue和next后，在等待较长时间的加载，Ubuntu 发行版就安装好了。![img](https://img-blog.csdnimg.cn/72aca540faa84af8ae2bacb2574713b5.png#pic_center).

## #2 通过 `VScode` 的 `Remote` 插件连接至你的虚拟机 

​    首先在VScode中安装Remote-ssh的插件![img](https://img-blog.csdnimg.cn/f844002750ad4ba2bfed71af06a330cb.png#pic_center)

之后进入虚拟机，用ifconfig来获取虚拟机的ip，之后再通过VScode进行连接，发现输入ifconfig不可以，系统提示我需要sudo apt install net-tools,不过也不可以，在网上再继续查问题，之后发现应该首先在虚拟机设置中的网络适配器设置成桥接模式，![img](https://img-blog.csdnimg.cn/c1e5337b813c45f0a0b0460ed804422b.png#pic_center)



之后在虚拟机中的终端输入sudo apt-get updage,sudo apt-get upgrade，之后再输入sudo apt install net-tools和ifconfig，之后成功获取ip。

   高兴的我连忙在打开vscode试了试,

![img](https://img-blog.csdnimg.cn/4db50267862c425c8217135a1b643d1d.jpeg#pic_center)结果![img](https://img-blog.csdnimg.cn/bb77c9c98f4c4ef1ab01d78a1510d3cd.jpeg#pic_center)

发现试图写入的管道不存在。不断在网上寻找相关的问题，之后参考了教程https://blog.csdn.net/weixin_44197719/article/details/119888235和https://blog.csdn.net/lxw983520/article/details/99497271 

使用指令![img](https://img-blog.csdnimg.cn/c8b38932cda54a31a9cae99b4dc8d9c6.png#pic_center)修改内容等，相当于重新来过一次。![img](https://img-blog.csdnimg.cn/d4fb72282799494c83eb6c0c8de7cc59.png#pic_center)终于获得成功：![img](https://img-blog.csdnimg.cn/247676fc519a41f88daf780dace13c34.png#pic_center)

## #3 配置好基于 `SSH` 密钥的免密的远程服务器登陆

   进入C盘的用户中.ssh文件已经更新，密钥已经不是使用github的密钥了，之后我就立马尝试密钥免密登录。之后参考教程http://t.csdn.cn/MqZXn。在#2中我查找教程发现了sftp命令可以指定ip和文件路径之后进行发送，这个工具可以连接服务器并上传文件，之后在D盘建立了kkk.txt的文档，之后利用sftp成功发送到我的虚拟机![img](https://img-blog.csdnimg.cn/f4bb4289150145849e1b43a0bcb28d76.jpeg#pic_center)

![img](https://img-blog.csdnimg.cn/21070dac775a47cfb0289ec40ddf5891.jpeg#pic_center)

不过发现直接执行传送的文件地址不对，这样直接将公钥传送肯定是不对了，之后在网上发现了指定路径的发送方式，利用put -r C:\Users\李鼎铭\.ssh\id_rsa.pub /home/jiaotang/.ssh的指令的成功传送到对应路径，![img](https://img-blog.csdnimg.cn/8915ffe99b5049aca8c223df63621e68.jpeg#pic_center)，之后再输入cat id_rsa.pub >> authorized_keys ，（>>是追加的意思，我也才知道哈哈哈)，![img](https://img-blog.csdnimg.cn/193a2b75e264451d93714c37e312361e.jpeg#pic_center)

之后也就成功了。

   成功实现免密远程服务器登录：![img](https://img-blog.csdnimg.cn/d9f1bfc23cbb4aedb20a0c300e54dfab.jpeg#pic_center)

由图可见，不再需要password了。



### 个人感想

  第一，应该就是寻找问题的过程，从github建博客开始，真的感受到了擅用浏览引擎的力量，各类教程五花八门，就比如我建博客时看的教程还有18年的，这能建出来才怪，同样的，再利用VScode连接虚拟机的时候，参考的一个教程根本没有讲清楚，只是说用ifconfig调出来虚拟机ip，根本没说再虚拟机上也需要开启ssh连接，之后在其他教程上结合，成功实现。所以我发现我经常用的网站就是IT社区CSDN，所以我赶脚这个挺好的哈哈哈，然后还在努力学习搜索引擎中。

   第二，就是了解为什么需要虚拟机，从网上了解到：1. 因为安全，怕电脑中毒；2. 因为体验不同的系统；3. 因为学习、做实验；4. 因为流氓软件；5. 因为某些软件需要特殊环境；6. 工作需要。

   其次就是为什么要本地连接到虚拟机上，因为可以传文件啊，这样就可以实现以上虚拟机的用处。而ssh免密登录就可以省去频繁输入密码的麻烦，更加便利嘛。

  第三，就是做题的时候各种指令，端口，环境变量，等等等等，小白真的是困难，所以我赶脚我的路还是挺长的吧。也可以看到，我在使用新电脑时，用户名是我的中文名字，而不是英文，这确实是一个致命伤，因为有中文在运行指令是确实有隐患，这个曾被我认为是全过程的错误，不过最后还是好的，这个在之后一定不能再用中文了。

