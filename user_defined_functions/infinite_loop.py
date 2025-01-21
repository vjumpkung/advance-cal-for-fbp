class InfiniteLoop:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    RETURN_TYPES = ("STRING",)
    RETURN_NAME = ("text",)
    FUNCTION = "example"
    CATEGORY = "custom_node/example"

    def example(self):
        while True:
            pass
        return ("Example Custom Node File",)


UDF_CLASS_MAPPINGS = {"Infinite Loop": InfiniteLoop}
UDF_DISPLAY_NAME_MAPPINGS = {
    "Infinite Loop": "Infinite Loop",
}
