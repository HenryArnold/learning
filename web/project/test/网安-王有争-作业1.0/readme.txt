前几天听到讲师分享的一个web框架--flask，最近在学，便决定使用flask框架完成这个作业；
这里只使用了其中一个后台数据库操作功能，链接的是sqlite数据库
注：sqlite数据库不需要使用服务器。学习书籍--《Flask Web Development》

使用方法：
1. 激活虚拟环境 venv\scripts\activate
2.  ```
    (venv) $ python hello.py shell
	>>> from hello import db
	>>> db.create_all()
	#产生文件
	data.sqlite
    ```
3. 使用例子
    ---插入行---（Role, User可以自由定制）
    >>> from hello import Role, User
    >>> admin_role = Role(name='Admin') 
    >>> mod_role = Role(name='Moderator') 
    >>> user_role = Role(name='User') 
    >>> user_john = User(username='john', role=admin_role) 
    >>> user_susan = User(username='susan', role=user_role) 
    >>> user_david = User(username='david', role=user_role)
	>>> db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
	>>>db.session.commit()
	---修改行---
    >>> admin_role.name = 'Administrator' 
    >>> db.session.add(admin_role) 
    >>> db.session.commit()
	----删除行---
    >>> db.session.delete(mod_role) 
    >>> db.session.commit()
	查询行
    >>> Role.query.all() 
    [<Role u'Administrator'>, <Role u'User'>] 
    >>> User.query.all() 
    [<User u'john'>, <User u'susan'>, <User u'david'>]