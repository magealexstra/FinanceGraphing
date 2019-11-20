import df_create as dfc
import Charting

if __name__ == '__main__':

    start = dfc.s_date(2019, 1, 1)
    end = dfc.e_date(2019, 3, 1)

    tsla_df = dfc.df_grab("TSLA", "yahoo", start, end)

    Charting.chart_maker("Tesla Candlestick Chart", tsla_df, "Tesla")

