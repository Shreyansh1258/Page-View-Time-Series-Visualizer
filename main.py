# main.py
from time_series_visualiser import load_and_clean_data, draw_line_plot, draw_bar_plot, draw_box_plot

def main():
    df = load_and_clean_data()
    draw_line_plot(df)
    draw_bar_plot(df)
    draw_box_plot(df)
    print("Plots generated: line_plot.png, bar_plot.png, box_plot.png")

if __name__ == "__main__":
    main()