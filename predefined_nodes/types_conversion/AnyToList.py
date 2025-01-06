from predefined_nodes.types.any import any
import numpy as np


class AnyToList:
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
    RETURN_NAMES = ("list",)
    FUNCTION = "convert_to_list"
    CATEGORY = "types_conversion"

    def convert_to_list(self, any):
        return (np.array(any),)
