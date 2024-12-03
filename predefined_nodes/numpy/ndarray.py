import numpy as np


class createNumpy1DArray:
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "ipt": ("STRING", {"defaultVal": "1,2,3"}),
            }
        }

        return inputs

    RETURN_TYPES = ("NDARRAY",)
    RETURN_NAME = ("numpy",)
    DESCRIPTION = "Crate Numpy 1D Array"
    FUNCTION = "create_numpy_1d_array"
    CATEGORY = "numpy"

    def create_numpy_1d_array(self, ipt):
        lst = list(map(int, ipt.split(",")))
        return (np.array(lst),)
