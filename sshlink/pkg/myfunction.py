"""
作用：'sshlink -[lsfh] severName'命令对服务器进行访问
arg参数如下：
-l: 显示可用的服务器名字
-s: 使用ssh命令进行连接服务器
-f: 使用sftp命令进行连接服务器
-h: 显示帮助信息
－-help: 显示帮助信息
"""
import sys
import os

argv = sys.argv
BASE_URL = '/Users/yz/.ssh'      # 存放私钥的路径

serverName = {
    'ali': ('47.94.15.201', 'Mac_YN.pem')
}

def sshlink():
    if len(argv) == 1:    # 没有参数的时候显示帮助信息
        print(__doc__)
    elif argv[1] == '-l':    # 显示所有的可用服务器名
        print('Servers can be used: ', ' '.join(serverName.keys()))
    elif argv[1] == '-s':    # 使用ssh进行连接
        if len(argv) == 3 and argv[2] and argv[2] in serverName:
            sshcmd = list()
            sshcmd.append('ssh root@' + serverName[argv[2]][0])
            sshcmd.append('-i')
            sshcmd.append(os.path.join(BASE_URL, serverName[argv[2]][1]))
            os.system(' '.join(sshcmd))
        else:
            print("Need Server Name: ", ' '.join(serverName.keys()))
    elif argv[1] == '-f':    #使用sftp进行连接
        if len(argv) == 3 and argv[2] and argv[2] in serverName:
            sftpcmd = list()
            sftpcmd.append('sftp -i')
            sftpcmd.append(os.path.join(BASE_URL, serverName[argv[2]][1]))
            sftpcmd.append('root@' + serverName[argv[2]][0])
            os.system(' '.join(sftpcmd))
        else:
            print("Need Server Name: ", ' '.join(serverName.keys()))
    elif argv[1] == '--help' or argv[1] == '-h':
        print(__doc__)
        print("Servers can be used: ", ' '.join(serverName.keys()))
    else:
        print("Only support -l, -s, -f, --help")