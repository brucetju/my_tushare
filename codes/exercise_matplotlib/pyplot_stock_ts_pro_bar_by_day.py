#!/usr/bin/env python
#coding=utf-8

# https://blog.csdn.net/Shepherdppz/article/details/108205721

import  tushare as ts
import talib
import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
#from mplfinance import candlestick_ochl
import  mplfinance as mpf

fig = plt.figure(figsize=(20,12),dpi=100,facecolor='white')#创建fig对象

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
df = ts.pro_bar('600519.SH',start_date='2020-12-25',end_date='2021-02-26')
#df = ts.pro_bar('600519.SH',start_date='2021-02-25',end_date='2021-02-26',freq='60MIN')

'''
行索引为 0-xx
'''
for index,column in df.iterrows():
    print(index)
'''
0
1
'''

for index,row in df.iteritems():
    print(index)
'''
列名称为：
ts_code
trade_date
open
high
low
close
pre_close
change
pct_chg
vol
amount
'''

print(df)
'''
     ts_code trade_date    open  ...  pct_chg       vol        amount
0  600519.SH   20210226  2100.0  ...  -1.2660  66525.06  1.409702e+07
1  600519.SH   20210225  2209.0  ...  -1.7816  59726.43  1.298215e+07

[2 rows x 11 columns]
'''

#用trade_date当索引
df.index = df.trade_date
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
df.drop(columns=['ts_code', 'trade_date', 'pre_close', 'change', 'pct_chg', 'amount'], inplace=True)
print(df)
'''
              open     high      low    close       vol
trade_date                                             
2021-02-26  2100.0  2179.95  2067.30  2122.78  66525.06
2021-02-25  2209.0  2224.50  2121.21  2150.00  59726.43
'''

#重命名列名称
df.columns=['open', 'high', 'low', 'close', 'volume']
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

# 计算macd的数据。计算macd数据可以使用第三方模块talib（常用的金融指标kdj、macd、boll等等都有，这里不展开了），如果在金融数据分析和量化交易上深耕的朋友相信对这些指标的计算原理已经了如指掌，直接通过原始数据计算即可，以macd的计算为例如下：
exp12 = df['close'].ewm(span=12, adjust=False).mean()
exp26 = df['close'].ewm(span=26, adjust=False).mean()
macd = exp12 - exp26
signal = macd.ewm(span=9, adjust=False).mean()
histogram = macd - signal
histogram[histogram<0]= None
histogram_positive = histogram
histogram = macd - signal
histogram[histogram>=0] = None
histogram_negative = histogram
add_plot = [
            mpf.make_addplot(exp12, type='line', color='y'),
            mpf.make_addplot(exp26, type='line', color='r'),
            #mpf.make_addplot(histogram, type='bar', width=0.7, panel=2, color='dimgray', alpha=1,
            #                        secondary_y=False),
            mpf.make_addplot(histogram_positive, type='bar', width=0.7, panel=2, color='b'),
            mpf.make_addplot(histogram_negative, type='bar', width=0.7, panel=2, color='fuchsia'),
            mpf.make_addplot(macd, panel=2, color='fuchsia', secondary_y=True),
            mpf.make_addplot(signal, panel=2, color='b', secondary_y=True),
#            mpf.make_addplot(df['PercentB'], panel=1, color='g', secondary_y='auto'),
        ]

#macd_dif, macd_dea, macd_bar = talib.MACD(df['close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
#macd_bar[]

mpf.plot(df, type='candle',addplot=add_plot, volume=True, style = 'yahoo', mav=(5,10,20,30))

'''
gs = gridspec.GridSpec(4, 1, left=0.08, bottom=0.15, right=0.99, top=0.96, wspace=None, hspace=0, height_ratios=[3.5,1,1,1])
graph_KAV = fig.add_subplot(gs[0,:])
graph_VOL = fig.add_subplot(gs[1,:])
graph_MACD = fig.add_subplot(gs[2,:])
graph_KDJ = fig.add_subplot(gs[3,:])

#绘制MACD
macd_dif, macd_dea, macd_bar = talib.MACD(df['close'].values, fastperiod=12, slowperiod=26, signalperiod=9)
graph_MACD.plot(np.arange(0, len(df.index)), macd_dif, 'red', label='macd dif')  # dif
graph_MACD.plot(np.arange(0, len(df.index)), macd_dea, 'blue', label='macd dea')  # dea

bar_red = np.where(macd_bar > 0, 2 * macd_bar, 0)# 绘制BAR>0 柱状图
bar_green = np.where(macd_bar < 0, 2 * macd_bar, 0)# 绘制BAR<0 柱状图
graph_MACD.bar(np.arange(0, len(df.index)), bar_red, facecolor='red')
graph_MACD.bar(np.arange(0, len(df.index)), bar_green, facecolor='green')

graph_MACD.legend(loc='best',shadow=True, fontsize ='10')
graph_MACD.set_ylabel(u"MACD")
graph_MACD.set_xlim(0,len(df.index)) #设置一下x轴的范围
graph_MACD.set_xticks(range(0,len(df.index),15))#X轴刻度设定 每15天标一个日期


#绘制KDJ
df['K'], df['D'] = talib.STOCH(df.high.values, df.low.values, df.close.values,\
                                       fastk_period=9, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

df['J'] = 3 * df['K'] - 2 * df['D']

graph_KDJ.plot(np.arange(0, len(df.index)), df['K'], 'blue', label='K')  # K
graph_KDJ.plot(np.arange(0, len(df.index)), df['D'], 'g--', label='D')  # D
graph_KDJ.plot(np.arange(0, len(df.index)), df['J'], 'r-', label='J')  # J
graph_KDJ.legend(loc='best', shadow=True, fontsize='10')

graph_KDJ.set_ylabel(u"KDJ")
graph_KDJ.set_xlabel("日期")
graph_KDJ.set_xlim(0, len(df.index))  # 设置一下x轴的范围
graph_KDJ.set_xticks(range(0, len(df.index), 15))  # X轴刻度设定 每15天标一个日期
graph_KDJ.set_xticklabels(
[df.index.strftime('%Y-%m-%d')[index] for index in graph_KDJ.get_xticks()])  # 标签设置为日期

plt.savefig('Kline.jpg')
plt.show('Kline')
'''