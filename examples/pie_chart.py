import pandas as pd
import matplotlib.pyplot as plt
from predefined_functions.image.generate_image_path import generate_image_save_path


class PieChart:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {"SERIES": ("PD_SERIES",)}}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("plot_result",)
    FUNCTION = "create_pie_chart"
    CATEGORY = "udf/matplotlib"

    def create_pie_chart(self, SERIES: pd.Series):

        plot = SERIES.plot.pie()

        imgfile = generate_image_save_path()

        plt.tight_layout()

        plot_result = plot.get_figure()
        plot_result.savefig(imgfile)

        return (f"/{imgfile}",)


UDF_CLASS_MAPPINGS = {"PieChart": PieChart}
UDF_DISPLAY_NAME_MAPPINGS = {
    "PieChart": "Pie Chart",
}
