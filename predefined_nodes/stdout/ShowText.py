class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "base"

    def notify(self, text):
        if len(str(text)) > 1000:
            print(str(text))
            warntext = r"Warning: The text is too long to be displayed in the console."
            return {
                "ui": {"text": (warntext,)},
                "result": (warntext,),
            }
        else:
            return {"ui": {"text": text}, "result": (text,)}
