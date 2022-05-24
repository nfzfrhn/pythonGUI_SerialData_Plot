import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Matplotlib Demo')

        # prepare data
        data = {
            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26
        }
        languages = data.keys()
        popularity = data.values()

        # create a figure to hold the chart. It takes two argument: size in inches and dots per inches. In this example, it creates a 600x400 pixel figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object that connects the figure object with a Tkinter's Canvas object. Note that FigureCanvasTkAgg object is not Canvas
        # object but contains a Canvas object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create a matplotlib's built in toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == '__main__':
    app = App()
    app.mainloop()