class StringConcatNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_1": (
                    "STRING",
                    {
                        "forceInput": True,
                    },
                ),
                "text_2": (
                    "STRING",
                    {
                        "forceInput": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "concat_string"
    CATEGORY = "base"

    def concat_string(self, text_1: str, text_2: str):
        return (text_1 + text_2,)
