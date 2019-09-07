import matplotlib.pyplot as plt
import numpy as np
import tushare as ts
import mpl_finance as mpf
import tkinter.messagebox
import tkinter

from tkinter import *

from datetime import datetime
from matplotlib import ticker
from matplotlib.gridspec import GridSpec
from argparse import ArgumentParser
from Config import *

global config
config = ConfigObj()


def main():
    ts.set_token('c0e0d746982d06f1062c9dce9b12d308821aaa9cf86b3e9242e1b1dc')
    disp(config.flush_rate,config.code,config.start,config.end)

def disp(rate,code,start,end):
    pro = ts.pro_api()
    df = pro.daily(ts_code=code, start_date=start, end_date=end)
    df = df.sort_values(by='trade_date', ascending=True)
    prices = df[['open', 'high', 'low', 'close']]
    dates = df['trade_date']
    candleData = np.column_stack([list(range(len(dates))), prices])

    plt.ion()
    plt.figure(figsize=(6,12))
    gs = GridSpec(3,2)
    ax1 = plt.subplot(gs[2,:])
    ax2 = plt.subplot(gs[0,:])
    def format_date(x, pos):
        if x < 0 or x > len(dates.values) - 1:
            return ''
        return dates.values[int(x)]

    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    mpf.candlestick_ohlc(ax1, candleData, width=0.5, colorup='r', colordown='g')
    ax1.set_title('K line image')

    ax2_dates = []
    ax2_prices= []
    while True:
        plt.cla()
        ax2.set_title('RealTime every '+ str(config.flush_rate) + 's')
        data = ts.get_realtime_quotes('sz')  # Single stock symbol
        ax2_dates.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        ax2_prices.append(float(data['price']) + np.random.random())
        ax2.grid()
        ax2.plot(ax2_dates, ax2_prices, '-r',linestyle=':')
        for tick in ax2.get_xticklabels():
            tick.set_rotation(90)
            tick.set_horizontalalignment('right')
        plt.pause(rate)


if __name__ == '__main__':
    main()