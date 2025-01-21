from predefined_functions.types.any import any


class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    # OUTPUT_IS_LIST = (True,)

    CATEGORY = "base"

    def notify(self, text):
        if len(text) > 1000:
            print(text)
            warntext = r"Warning: The text is too long to be displayed in the console."
            return {
                "ui": {"text": (warntext,)},
                "result": (warntext,),
            }
        else:
            return {"ui": {"text": (text,)}, "result": (text,)}
