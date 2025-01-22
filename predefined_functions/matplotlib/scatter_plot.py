import matplotlib.pyplot as plt
import random
from predefined_functions.types.list import list_types


class CreateScatterPlot:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {"X": (list_types,), "Y": (list_types,)}}

    CATEGORY = "matplotlib"

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("plot_result",)
    FUNCTION = "show_scatter_plot"

    def show_scatter_plot(self, X, Y):
        plot = plt.scatter(X, Y)
        imgfile = f"temp/{hex(hash(random.randint(1000000,9999999)))[2:]}.png"
        plt.tight_layout()
        fig = plot.get_figure()
        fig.savefig(imgfile)
        return (f"/{imgfile}",)
