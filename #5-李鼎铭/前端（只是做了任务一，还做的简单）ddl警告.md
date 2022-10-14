#  前端（只是做了任务一，还做的简单）ddl警告

## HTML加简单的CSS

利用pycharm加了一点简单的语句所以构成了简单的静态页面。

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>碎碎念的个人页面</title>
    <style>
        h1 {color:black;}
        body {background:url('下载.png');}




</style>
</head>
<body>
    <h1><center>碎碎念的个人页面 </center></h1>
    <h2>个人介绍</h2>
    <hr>
        <p> &emsp; 你好呀，欢迎欢迎！！我是22级14班的李鼎铭，来自河北省邢台市。爱好的话，喜欢追剧（尤以美剧为主）、看国漫、听歌
            <br>爱音乐（虽然自己音乐细胞不咋地），体育是致命伤了，不过体测及格了哈哈哈，自己的定位是爱笑的乐观男吧，还是有点社恐
            <br>的。对于电脑敲代码了啥子的自己还是从小白萌新做起的吧，在做这次马拉松的时候困难还是很多的吧，不过之后还是继续努力
            <br>呗！对未来的畅想的话，当然是要进入焦糖之后快乐的玩耍了哈哈哈。</p>
    <h2>照片和头像</h2>
    <hr>

    <img src="https://img-blog.csdnimg.cn/3b20bc18639145828a1a6c3022d125f3.jpeg#pic_center"
    width="300"height="300">
    <img src="https://img-blog.csdnimg.cn/9d69f822c4e54304a9a92558f8880fa3.jpeg#pic_center"
    width="450"height="300">
    <img src="https://img-blog.csdnimg.cn/c881b23686cd4011bce3bc9e2da0f927.jpeg#pic_center"
    width="490"height="300">
    <img src="https://img-blog.csdnimg.cn/ef73e84221af45608bebbb91f91a0478.jpeg#pic_center"
    width="420"height="300">
</body><h2>学习记录</h2>
<hr>
        <p>&emsp;呜啦啦，我其实希望在这一个月里面把前端和后端都学学，无奈发现自己能力不足或者时间没有分配好，不过最后做了这么些题
        <br>我感觉也是不错的了吧，在ddl前把前端看看，因为最后几天学后端真的把我劝退了，所以我来试试前端的水，但是我绝不会之后就不
        <br>学后端了啊，之后还是继续努力呗！</p>
        <p>&emsp;HTML的话这种标记语言在使用的时候我就是看菜鸟教程就把这些简单的东西顺了下来，困难的话，至此还没遇到吧，当然希望之
        <br>后也不会遇到哈哈哈。真正的困难应该是搭建博客、学习python、爬虫的一大堆的困难吧。</p>
</html>
```

## Netlify 部署

先是将html及相关图片导入github库

  利用githubdesktop快捷导入自己的github库。

![在这里插入图片描述](https://img-blog.csdnimg.cn/e626896be4264dbe89df916a9ebe6462.png#pic_center)

这里注意HTML的文件名称是index.html，这样在部署的时候就不会出现Page Not Found（这个我之前一直出现Page Not Found的问题，后来在招新群里面找到了答案哈哈哈）之后还要把图片导入就可以啦。

![在这里插入图片描述](https://img-blog.csdnimg.cn/35883e191870462e941456b657e4d5dc.png#pic_center)

之后就是部署页面了，通过Netlify很简单的就有自己的页面了。

![在这里插入图片描述](https://img-blog.csdnimg.cn/30d2fd2973db48289b6e7c475102bd72.png#pic_center)

最后就可以得到了

![在这里插入图片描述](https://img-blog.csdnimg.cn/66f87c986fb5416b9e9ee32a4d430c05.png#pic_center)

附上我的网页链接：“[碎碎念的个人页面 (6347d63249449804ae5b5ea5--adorable-croissant-7b1c54.netlify.app)](https://6347d63249449804ae5b5ea5--adorable-croissant-7b1c54.netlify.app/)“

## PS：

临近ddl做的，确实做的很简单，我希望就是前端后端都要会做，不过先选着做了几道题之后，到这道题确实剩下的时间不多了，所以还是抱着尝试的心态看着做了做，不过有自己做的页面确实很开心，希望之后自己还能完善前端，并且做完后端。
