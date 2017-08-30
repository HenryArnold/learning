----------------------------------
1.安装并激活虚拟环境
$pip install virtualenv
$virtualenv venv
.....
$ cd venv/Scripts/
$ activate
2.安装所需模块
pip install flask flask_wtf flask_bootstrap flask_sqlalchemy
pip install -v flask_sqlalchemy==2.0 
2. 启动服务
cd ..
cd ..
$ python hello.py
3. 本地访问
127.0.0.1:5000
---------------------------------


注：
增删改查分别对应register, delete, modify, query/login
用户拥有 register delete modify login 的权限
管理员拥有 login query delete modify 权限
管理员账号内置（root：toor）