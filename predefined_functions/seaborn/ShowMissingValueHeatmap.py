import logging
import random

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from predefined_functions.image.generate_image_path import generate_image_save_path

logging.getLogger("matplotlib.font_manager").disabled = True
matplotlib.use("agg")


class ShowMissingValueHeatMap:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
            }
        }

    CATEGORY = "seaborn"
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ()
    FUNCTION = "show_missing_values"

    def show_missing_values(self, dataframe: pd.DataFrame):
        hm = sns.heatmap(dataframe.isnull(), cbar=False, yticklabels=False)
        imgfile = generate_image_save_path()
        plt.tight_layout()
        fig = hm.get_figure()
        fig.savefig(imgfile)
        return (f"/{imgfile}",)
