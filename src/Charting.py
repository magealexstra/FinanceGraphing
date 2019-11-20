from bokeh.plotting import figure, show, output_file

hours_12 = 12*60*60*1000


def chart_maker(title, dataframe, outputname):
	p = figure(x_axis_type="datetime", width=1000, height=300, sizing_mode="scale_width")
	p.title.text = f"{title}"
	p.grid.grid_line_alpha = 0.5

	p.segment(dataframe.index, dataframe.High, dataframe.index, dataframe.Low, color="black")
	p.rect(dataframe.index[dataframe.Status == "Increase"], dataframe.Mean[dataframe.Status == "Increase"], hours_12,
								dataframe.Height[dataframe.Status == "Increase"], fill_color="blue", line_color="black")
	p.rect(dataframe.index[dataframe.Status == "Decrease"], dataframe.Mean[dataframe.Status == "Decrease"], hours_12,
								dataframe.Height[dataframe.Status == "Decrease"], fill_color="red", line_color="black")

	output_file(f"DATA\\{outputname}.html")
	show(p)