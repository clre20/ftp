# FTP 伺服器

本專案示範如何使用 [pyftpdlib](https://github.com/giampaolo/pyftpdlib) 建立一個簡單且可擴展的 FTP 伺服器。程式碼自動根據預先定義的使用者資料建立家目錄、設定權限，方便連線與檔案傳輸。

## 特色

- **自動建立使用者家目錄**  
  根據 `users` 清單中定義的每個使用者，程式會建立對應的目錄（若尚不存在），並設定權限為 `0o700`，資料僅限使用者本人存取。

- **靈活的權限管理**  
  每位使用者的存取權限可由 `perm` 參數自訂（例如：`elradfmw` 能夠進行列出、讀取、寫入、刪除等操作）。

## 安裝

使用 pip 安裝 pyftpdlib：

```bash
pip install pyftpdlib
```

## 使用方法

1. 將本專案程式碼下載至本地端。
2. 根據需求修改 `users` 清單中的使用者資訊（包括使用者名稱、密碼、家目錄與權限）。
```python
# 定義使用者資料
users = [
    {"username": "user1", "password": "password1", "home_dir": "ftp/user1", "perm": "elradfmw"},
    {"username": "user2", "password": "password2", "home_dir": "ftp/user2", "perm": "elradfmw"},
    {"username": "t1", "password": "123", "home_dir": "ftp/t1", "perm": "elradfmw"},
]
```
3. 執行程式以啟動 FTP 伺服器：

   ```bash
   python ftp.py
   ```

4. 啟動成功後，終端機會顯示類似訊息：

   ```txt
   已新增使用者：user1，目錄：ftp/user1
   已新增使用者：user2，目錄：ftp/user2
   已新增使用者：t1，目錄：ftp/t1
   FTP 伺服器已啟動，等待連線...
   ```

