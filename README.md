# Utopia-Bot-For-QQ
这是一个基于[nonebot](https://github.com/nonebot/nonebot)机器人框架与[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)客户端设计的QQ聊天机器人  
文档更新时间 2021-03-25

## 目录
1. [简介](#简介)
2. [接口使用](#接口使用)
3. [部署](#部署)
4. [功能](#功能)
5. [注意](#注意)
6. [开源许可与免责声明](#开源许可与免责声明)

## 简介
本项目完全由Python实现。依托于开源QQ机器人nonebot提供机器人服务对消息进行解析及相应，通过go-cqhttp客户端登录QQ并进行消息接收与发送。  
目前仅实现了少数计划功能  
Telegram版本的Utopia Bot正在开发中  
部署前请对API进行调试 


## 接口使用
1. 句子接口：[一言·Hitokoto](https://hitokoto.cn/)  
   本接口使用方法请查阅官方文档，这里不再赘述
2. 涩图接口：[Lolicon API](https://api.lolicon.app/#/setu)  
   使用本接口时请注意：  
   使用前请使用接口官网的提供的Telegram机器人申请apikey，请求的时候需要带上此参数。  
   本接口返回的是Pixiv图片链接而不是图片原图，所以当你发现该机器人在部署好之后无法发送图片请保证运行该机器人的服务器能正常访问Pixiv。  
   此外，本接口存在R18内容，请自行过滤并带上相关参数。  
3. 知乎日报：[知乎官方API](https://news-at.zhihu.com/api/3/stories/latest)  
   本接口为知乎日报的官方API，每次返回全部日报信息，本机器人每次发送仅选择一个发送。
4. 英语句子：[金山词霸每日英语](http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&title=2020-01-01)  
   本接口为金山词霸每日英语接口，每次返回一句英语，请注意title参数，该参数为获取句子的日期。机器人默认选取当天至当天前六百天内的任意一天进行爬取
5. 微博热搜：暂时由爬虫实现  
   一个无害的小型的网页爬虫，仅获取热搜前十，如需更多请自行修改循环次数。
6. 哔哩哔哩热门视频：[哔哩哔哩官方接口](https://api.bilibili.com/x/web-interface/popular?ps=1&pn=1)  
   哔哩哔哩的官方热榜接口。此处需要注意的是ps为每次获取的视频信息个数，pn为起始视频的实时热榜排名。因此在机器人中pn为1~50随机生成的来保证每次都能取到前50内不同的视频
## 部署
- ### 部署 go-cqhttp
- ### 部署Python环境
- ### 部署 Utopia Bot

## 功能
1. 帮助![help](pictures/help.png)
2. 一言![sentence](pictures/sentence.png)
3. 涩图![setu](pictures/setu.png)
4. 日报![daily](pictures/daily.png)
5. 英语句子![english](pictures/english.png)
6. 微博热搜![weibo](pictures/weibo.png)
7. 哔哩哔哩热门视频![bili](pictures/bili.png)

## 注意
1. 请注意，涩图接口存在R18内容，请带有r18=0参数访问接口
2. QQ机器人违反QQ使用条款，请使用新账号或小号进行部署，账号被封禁概不负责
3. 如果对go-cqhttp部署有疑问，请到原作者Git提Issue
4. 如果功能中截图无法查看，请使用全局代理后查看

## 开源许可与免责声明
本项目源码均采用MIT开源许可。源码设计仅作学习用途，严禁用于商业用途与其他违法用途。一切后果由使用者承担。