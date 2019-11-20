import pandas_datareader as data
import datetime
from bokeh.plotting import figure, show, output_file
import pandas

hours_12 = 12*60*60*1000

start = datetime.datetime(2018, 3, 1)
end = datetime.datetime(2019, 3, 20)

dataframe = data.DataReader(name="TSLA", data_source="yahoo", start=start, end=end)
print(dataframe)


def inc_dec(o, c):
	if c > o:
		value = "Increase"
	elif c < o:
		value = "Decrease"
	else:
		value = "Equal"
	return value


dataframe["Status"] = [inc_dec(o, c) for o, c in zip(dataframe.Open, dataframe.Close)]
dataframe["Mean"] = (dataframe.Open+dataframe.Close)/2
dataframe["Height"] = abs(dataframe.Close - dataframe.Open)

# date_increase = dataframe.index[dataframe.Close > dataframe.Open]
# date_decrease = dataframe.index[dataframe.Close < dataframe.Open]


p = figure(x_axis_type="datetime", width=1000, height=300, sizing_mode="scale_width")
p.title.text = "TSLA Candlestick"
p.grid.grid_line_alpha = 0.5

p.segment(dataframe.index, dataframe.High, dataframe.index, dataframe.Low, color="black")
p.rect(dataframe.index[dataframe.Status == "Increase"], dataframe.Mean[dataframe.Status == "Increase"], hours_12,
							dataframe.Height[dataframe.Status == "Increase"], fill_color="blue", line_color="black")
p.rect(dataframe.index[dataframe.Status == "Decrease"], dataframe.Mean[dataframe.Status == "Decrease"], hours_12,
							dataframe.Height[dataframe.Status == "Decrease"], fill_color="red", line_color="black")

output_file("CS.html")
show(p)