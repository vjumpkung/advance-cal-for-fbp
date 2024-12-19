from predefined_nodes.types.any import any


class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "any": (any,),
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("any",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "base"

    def notify(self, any):
        if len(str(any)) > 1000:
            print(str(any))
            warntext = r"Warning: The text is too long to be displayed in the console."
            return {
                "ui": {"text": (warntext,)},
                "result": (warntext,),
            }
        else:
            return {"ui": {"text": (any,)}, "result": (any,)}
