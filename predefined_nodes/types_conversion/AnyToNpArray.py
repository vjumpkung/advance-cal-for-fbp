from predefined_nodes.types.any import any
import numpy as np
import pandas as pd


class AnyToNumPyArray:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "any": (
                    any,
                    {
                        "forceInput": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("NDARRAY",)
    RETURN_NAMES = ("np_array",)
    FUNCTION = "convert_to_list"
    CATEGORY = "types_conversion"

    def convert_to_list(self, any):

        if isinstance(any, pd.DataFrame):
            return (any.to_numpy(),)
        elif isinstance(any, pd.Series):
            return (any.to_numpy(),)

        return (any,)
