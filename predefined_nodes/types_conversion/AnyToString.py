from predefined_nodes.types.any import any


class ConvertAnyToString:
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

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    DESCRIPTION = "Convert Any Value into String"
    FUNCTION = "convert_to_string"
    CATEGORY = "base"

    def convert_to_string(self, any):
        return (str(any),)
