class ExampleUDF1:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    DESCRIPTION = "Example"
    FUNCTION = "example"
    CATEGORY = "user_defined_function/example"

    def example(self):
        return ("Example Custom Node Folder #1",)
