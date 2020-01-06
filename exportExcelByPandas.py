import pandas as pd
from pandas import DataFrame, Series
from sqlalchemy import create_engine
import time
 
# 开始时间
start =time.time()
# 建立链接
engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/test')
# 查询语句
sql = "select * from `csv_data2` where `XK_XDR_SHXYM` is not null and `XK_XDR_SHXYM` != '空' and `XK_XDR_SHXYM` != '无' and  `XK_XDR_SHXYM` != '-' and `XK_XDR_SHXYM` != '';"
# 读取mysql
df = pd.read_sql_query(sql, engine)
print("从mysql中读取数据成功！开始将数据导入到excel表格中...")
# 将读取的数据格式化成DataFrame类型
test_data = DataFrame.from_records(df)
# 将数据写入excle中
test_data.to_excel("/Users/wzm/Desktop/sheet3.xlsx",sheet_name='Sheet1',index=False)
print("导出成功！")
# 程序结束时间
end = time.time()
# 打印出程序的运行时间
print('Running time: {} Seconds'.format(end-start))