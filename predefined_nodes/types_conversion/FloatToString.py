from time import sleep


class ConvertFloatToString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_number": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                )
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    DESCRIPTION = "Convert Float Value into String"
    FUNCTION = "convert_to_string"
    CATEGORY = "base"

    def convert_to_string(self, float_number):
        sleep(5)
        return (str(float_number),)
