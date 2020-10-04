from setuptools import setup

setup(
    name = "sshlink",
    version = "0.0.1",
    description = "SSH 快速连接服务器",
    author = "YZ",
    packages = [str('pkg')],
    platforms = "any",

    entry_points = {       
         'console_scripts': [
             'sshlink = pkg.myfunction:sshlink'
            ] 
    }
)