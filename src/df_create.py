import pandas_datareader as data
import datetime


def s_date(y, m, d):
	start = datetime.datetime(y, m, d)
	return start


def e_date(y, m, d):
	end = datetime.datetime(y, m, d)
	return end


def inc_dec(o, c):
	if c > o:
		value = "Increase"
	elif c < o:
		value = "Decrease"
	else:
		value = "Equal"
	return value


def df_grab(stockname, datasource, sdate, edate):
	dataframe = data.DataReader(name=stockname, data_source=datasource, start=sdate, end=edate)
	dataframe["Status"] = [inc_dec(o, c) for o, c in zip(dataframe.Open, dataframe.Close)]
	dataframe["Mean"] = (dataframe.Open + dataframe.Close) / 2
	dataframe["Height"] = abs(dataframe.Close - dataframe.Open)
	return dataframe
