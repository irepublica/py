import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import time
import datetime
import os

api_key = 'JMA480FCU4N62TAW'
price = TimeSeries(key=api_key, output_format='pandas')
indicator = TechIndicators(key=api_key, output_format='pandas')

date = str(datetime.datetime.now().date())
path = os.getcwd() + "\\Under5M_Under7\\" + date
try:
    os.mkdir(path)
except FileExistsError:
    os.chdir(path)
finally:
    os.chdir(path)

#   tickers
Under5M_Under7 = ['AAME', 'ACY', 'ADTX', 'AEY', 'AINC', 'AKER', 'ALIM', 'AMRH', 'AMS', 'ANCN', 'ANPC', 'ANTE', 'ANVS',
                  'ANY', 'APEX', 'APOP', 'APWC', 'ARMP', 'ARTL', 'ARTW', 'ATIF', 'AVCT', 'AWX', 'AXR', 'AYRO', 'BDR',
                  'BGI', 'BIMI', 'BKEP', 'BLIN', 'BNSO', 'BOSC', 'BPTH', 'BRN', 'BWAY', 'CARV', 'CELP', 'CGA', 'CGIX',
                  'CHCI', 'CLEU', 'CLPS', 'CLRO', 'CLWT', 'CNFR', 'CODA', 'CPAH', 'CREG', 'CTIB', 'CYAN', 'CYCC',
                  'DRAD', 'DUOT', 'EARS', 'EDNT', 'EDRY', 'EDSA', 'EDTK', 'EFOI', 'EKSO', 'ELSE', 'ELTK', 'ENOB',
                  'ESEA', 'EVK', 'EYEG', 'FAMI', 'FAT', 'FFHL', 'FORK', 'FRAN', 'FREE', 'FTSI', 'FWP',
                  'GBR', 'GRIL', 'GTEC', 'GWGH', 'HHT', 'HIHO', 'HOFV', 'HQI', 'ICD', 'IDXG', 'IHT', 'IKNX', 'IMTE',
                  'INDO', 'IPDN', 'ISNS', 'JAKK', 'JAN', 'JP', 'JRSH', 'JVA', 'KBSF', 'KFFB', 'KLR', 'KOSS', 'KXIN',
                  'LEDS', 'LGHL', 'LMB', 'LMFA', 'LTBR', 'LWAY', 'LYL', 'MARPS', 'MDGS', 'MDIA', 'MDJH', 'MEDS', 'MFH',
                  'MICT', 'MOSY', 'MOXC', 'MTR', 'MTSL', 'MXC', 'MYO', 'NCTY', 'NRBO', 'NSPR', 'NSYS', 'NTN', 'NTZ',
                  'NURO', 'NVFY', 'NVIV', 'NWGI', 'OBLG', 'OCC', 'OPHC', 'OSN', 'OXBR', 'PBTS', 'PECK', 'PFIN', 'PHCF',
                  'PHIO', 'PIXY', 'PNBK', 'POLA', 'PPSI', 'PSTV', 'PXS', 'RCON', 'RELV', 'RENN', 'REV', 'REXN', 'RHE',
                  'RMCF', 'RNGR', 'RYCE', 'SCKT', 'SFET', 'SGLB', 'SGMA', 'SIF', 'SINO', 'SJ', 'SKYS', 'SMIT', 'SNES',
                  'SOS', 'SSNT', 'SSY', 'TAIT', 'TATT', 'TCCO', 'TCON', 'THMO', 'TLF', 'TMBR', 'TRT',
                    'TSRI', 'USEG', 'UUU', 'VNCE', 'VVPR', 'WAFU', 'WHLM', 'WIMI', 'WISA', 'WVVI', 'YTEN', 'ZKIN',
                  'AHPI', 'AUVI', 'BNTC', 'CHNR', 'DSS', 'FLUX', 'HCDI', 'HX', 'IPWR', 'KZIA', 'MITO', 'MNPR', 'MYT',
                  'NAOV', 'NETE', 'NNDM', 'OLB', 'QLGN', 'SMLP', 'SQNS', 'TAOP', 'TYHT', 'VRME', 'WINT'
                  ]

'''
for ticker in Under5M_Under7:
    try:
        daily_price, daily_price_info = price.get_daily(symbol=ticker, outputsize='full')
        rsi, rsi_info = indicator.get_rsi(symbol=ticker, interval='daily', time_period=14, series_type='close')
        sma20, sma20_info = indicator.get_sma(symbol=ticker, interval='daily', time_period=20, series_type='close')
        sma50, sma50_info = indicator.get_sma(symbol=ticker, interval='daily', time_period=50, series_type='close')
        sma200, sma200_info = indicator.get_sma(symbol=ticker, interval='daily', time_period=200, series_type='close')

        sma20 = sma20.rename(columns={'SMA': 'sma20'})
        sma50 = sma50.rename(columns={'SMA': 'sma50'})
        sma200 = sma200.rename(columns={'SMA': 'sma200'})

        daily_final = pd.concat([daily_price, rsi, sma20, sma50, sma200], axis=1)
        daily_final = daily_final.rename(
            columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume',
                 'RSI': 'rsi'})

        daily_final.to_csv('Under5M_Under7/Daily/{0}_daily.csv'.format(ticker))
        time.sleep(60)
    except:
        print(ticker)
        continue

'''
for ticker in Under5M_Under7:
    try:
        intraday_price, intraday_price_info = price.get_intraday(symbol=ticker, interval='1min', outputsize='full')
        vwap, vwap_info = indicator.get_vwap(symbol=ticker, interval='1min')

        intraday_final = pd.concat([intraday_price, vwap], axis=1)
        intraday_final = intraday_final.rename(
            columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume',
                 'VWAP': 'vwap'})

        intraday_final.to_csv('{0}_intraday.csv'.format(ticker))
        time.sleep(60)
    except:
        print(ticker)
        continue


