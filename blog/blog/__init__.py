import pyodbc
try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=LAPTOP-9424UQBS\\SQL;'
        'DATABASE=blog;'
        'UID=libslam;'
        'PWD=123456'
    )
    print("连接成功!")
except Exception as e:
    print(f"连接失败: {str(e)}")