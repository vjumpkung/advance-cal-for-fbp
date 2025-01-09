import matplotlib.pyplot as plt
import random
from PIL import Image


class CreateScatterPlot:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {"X": ("NDARRAY",), "Y": ("NDARRAY",)}}

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
        # img = Image.open(imgfile)
        # img.show()
        return (f"/{imgfile}",)
