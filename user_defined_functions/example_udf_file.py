class ExampleCustomNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    RETURN_TYPES = ("STRING",)
    RETURN_NAME = ("text",)
    DESCRIPTION = "Example"
    FUNCTION = "example"
    CATEGORY = "user_defined_function/example"

    def example(self):
        return ("Example UDF File",)


UDF_CLASS_MAPPINGS = {"Example_UDF_FileClass": ExampleCustomNode}
UDF_DISPLAY_NAME_MAPPINGS = {
    "Example_UDF_FileClass": "Example UDF DISPLAY_NAME_MAPPINGS",
}
