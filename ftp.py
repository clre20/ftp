import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 定義使用者資料
users = [
    {"username": "user1", "password": "password1", "home_dir": "ftp/user1", "perm": "elradfmw"},
    {"username": "user2", "password": "password2", "home_dir": "ftp/user2", "perm": "elradfmw"},
    {"username": "t1", "password": "123", "home_dir": "ftp/t1", "perm": "elradfmw"},
]

# 創建 FTP 授權器
authorizer = DummyAuthorizer()

# 自動建立使用者目錄並配置權限
for user in users:
    # 確保目錄存在
    os.makedirs(user["home_dir"], exist_ok=True)
    
    # 設定資料夾權限（避免其他使用者訪問）
    os.chmod(user["home_dir"], 0o700)
    
    # 添加使用者
    authorizer.add_user(user["username"], user["password"], user["home_dir"], perm=user["perm"])
    print(f"已新增使用者：{user['username']}，目錄：{user['home_dir']}")

# 配置 FTPHandler
handler = FTPHandler
handler.authorizer = authorizer

# 啟動 FTP 伺服器
server = FTPServer(("0.0.0.0", 21), handler)

# 開始運行
print("FTP 伺服器已啟動，等待連線...")
server.serve_forever()
