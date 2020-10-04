import os

def creat_new_client():
    os.system("nohup /Applications/WeChat.app/Contents/MacOS/WeChat > /dev/null 2>&1 &")

def main():
    creat_new_client()

if __name__ == "__main__":
    main()