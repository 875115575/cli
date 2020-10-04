from setuptools import setup

setup(
    name = "wechat",
    version = "0.0.1",
    description = "多开微信 mac 端",
    author = "YZ",
    py_modules=['wechat'],
    platforms = "any",

    entry_points = {       
         'console_scripts': [
             'wechat = wechat:main'
            ] 
    }
)