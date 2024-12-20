import logging
import random

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from PIL import Image

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
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "show_missing_values"
    OUTPUT_NODE = True

    def show_missing_values(self, dataframe: pd.DataFrame):
        hm = sns.heatmap(dataframe.isnull(), cbar=False, yticklabels=False)
        imgfile = f"temp/{hex(hash(random.randint(1000000,9999999)))[2:]}.png"
        plt.tight_layout()
        fig = hm.get_figure()
        fig.savefig(imgfile)
        img = Image.open(imgfile)
        img.show()
        return ()
