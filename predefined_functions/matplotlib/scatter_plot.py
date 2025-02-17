import matplotlib.pyplot as plt
from predefined_functions.types.list import list_types
from predefined_functions.image.generate_image_path import generate_image_save_path


class CreateScatterPlot:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {"X": (list_types,), "Y": (list_types,)}}

    CATEGORY = "matplotlib"

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("plot_result",)
    FUNCTION = "show_scatter_plot"

    def show_scatter_plot(self, X, Y):

        plt.clf()
        plot = plt.scatter(X, Y)

        imgfile = generate_image_save_path()

        plt.tight_layout()
        fig = plot.get_figure()
        fig.savefig(imgfile)

        return (f"/{imgfile}",)
