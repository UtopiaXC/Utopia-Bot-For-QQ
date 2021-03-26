class config:
    # 以下为机器人的基本设置
    super_admins = {}  # 机器人默认设定，超级管理员的QQ号
    start_with = {'/', '*', '$', '%'}  # 指令标志，机器人检测到标志后才会进行指令判断
    nick_name = {''}  # 机器人昵称
    wait_time = 2  # 命令等待超时时间，整数（单位：分钟）
    bot_host = "127.0.0.1"  # 启动的WebSocket服务器的IP，一般为127.0.0.1，意为本地
    bot_port = 8765  # 启动的WebSocket服务器的端口，请与go-cqhttp内保持一致

    # 以下为部分模块的参数设置
    setu_apikey = ""