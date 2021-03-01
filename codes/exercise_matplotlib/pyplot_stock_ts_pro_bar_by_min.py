#!/usr/bin/env python
#coding=utf-8

# https://blog.csdn.net/Shepherdppz/article/details/108205721

import  tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
#from mplfinance import candlestick_ochl
import  mplfinance as mpf

#从文件里得到数据
ts.set_token('d2a8b7cc2699fe78afeb938990126811bfa2664b9919082551c33984')

'''
复权行情：
接口参数

名称	类型	必选	描述
ts_code	str	Y	证券代码
start_date	str	N	开始日期 (格式：YYYYMMDD)
end_date	str	N	结束日期 (格式：YYYYMMDD)
asset	str	Y	资产类别：E股票 I沪深指数 C数字货币 F期货 FD基金 O期权，默认E
adj	str	N	复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None
freq	str	Y	数据频度 ：1MIN表示1分钟（1/5/15/30/60分钟） W:week， M:month D日线 ，默认D
ma	list	N	均线，支持任意周期的均价和均量，输入任意合理int数值
'''
#df = ts.pro_bar('600519.SH',start_date='2021-02-25',end_date='2021-02-26')
df = ts.pro_bar('600519.SH',start_date='2021-02-24',end_date='2021-02-26',freq='60MIN')

'''
行索引为 0-xx
'''
for index,column in df.iterrows():
    print(index)
'''
0
1
2
3
4
'''

for index,row in df.iteritems():
    print(index)
'''
列名称为：
ts_code
trade_time
open
close
high
low
vol
amount
trade_date
pre_close
'''

print(df)
'''
     ts_code           trade_time     open  ...        amount  trade_date  pre_close
0  600519.SH  2021-02-25 15:00:00  2144.00  ...  3.720642e+09    20210225    2145.00
1  600519.SH  2021-02-25 14:00:00  2190.69  ...  2.625482e+09    20210225    2191.00
2  600519.SH  2021-02-25 11:30:00  2198.98  ...  1.407182e+09    20210225    2198.90
3  600519.SH  2021-02-25 10:30:00  2208.00  ...  5.019868e+09    20210225    2209.00
4  600519.SH  2021-02-25 09:30:00  2209.00  ...  2.089714e+08    20210225    2189.00
5  600519.SH  2021-02-24 15:00:00  2191.95  ...  4.098837e+09    20210224    2190.28
6  600519.SH  2021-02-24 14:00:00  2200.00  ...  3.569044e+09    20210224    2200.50
7  600519.SH  2021-02-24 11:30:00  2228.00  ...  4.884939e+09    20210224    2226.95
8  600519.SH  2021-02-24 10:30:00  2310.00  ...  5.466576e+09    20210224    2307.99
9  600519.SH  2021-02-24 09:30:00  2307.99  ...  1.756380e+08    20210224        NaN

[10 rows x 10 columns]
'''

#用trade_date当索引
df.index = df.trade_time
print(df)
'''
              ts_code trade_date    open  ...  pct_chg       vol        amount
trade_date                                ...                                 
20210226    600519.SH   20210226  2100.0  ...  -1.2660  66525.06  1.409702e+07
20210225    600519.SH   20210225  2209.0  ...  -1.7816  59726.43  1.298215e+07

[2 rows x 11 columns]
'''

#20210225->2021-02-25,更新Timestamp格式
df = df.rename(index = pd.Timestamp)
print(df)
'''
              ts_code trade_date    open  ...  pct_chg       vol        amount
trade_date                                ...                                 
2021-02-26  600519.SH   20210226  2100.0  ...  -1.2660  66525.06  1.409702e+07
2021-02-25  600519.SH   20210225  2209.0  ...  -1.7816  59726.43  1.298215e+07

[2 rows x 11 columns]
'''

#删除不用的列
df.drop(columns=['ts_code', 'trade_time', 'trade_date', 'pre_close', 'amount'], inplace=True)
print(df)
'''
              open     high      low    close       vol
trade_date                                             
2021-02-26  2100.0  2179.95  2067.30  2122.78  66525.06
2021-02-25  2209.0  2224.50  2121.21  2150.00  59726.43
'''

#重命名列名称
df.columns=['open', 'close', 'high', 'low', 'volume']
print(df)
'''
              open     high      low    close    volume
trade_date                                             
2021-02-26  2100.0  2179.95  2067.30  2122.78  66525.06
2021-02-25  2209.0  2224.50  2121.21  2150.00  59726.43
'''

#数据排序，依据时间从前到后
df.sort_index(inplace=True)
print(df)
'''
              open     high      low    close    volume
trade_date                                             
2021-02-25  2209.0  2224.50  2121.21  2150.00  59726.43
2021-02-26  2100.0  2179.95  2067.30  2122.78  66525.06
'''

#mpf.plot(df, type='candle', volume=True, style = 'yahoo', mav=(5,10,20,30))