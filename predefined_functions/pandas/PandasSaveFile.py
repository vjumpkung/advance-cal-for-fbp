import os
import pandas as pd


class PandasSaveFile:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "path": ("STRING",),
                "filename": ("STRING",),
                "dataframe": ("PD_DATAFRAME",),
            }
        }

    CATEGORY = "utils"

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "execute"
    OUTPUT_NODE = True

    def execute(self, path, filename, dataframe: pd.DataFrame):
        dataframe.to_csv(os.path.join(path, filename), index=False)

        return ()
