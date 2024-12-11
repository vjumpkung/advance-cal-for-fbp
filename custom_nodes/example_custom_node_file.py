class ExampleCustomNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    RETURN_TYPES = ("STRING",)
    RETURN_NAME = ("text",)
    DESCRIPTION = "Example"
    FUNCTION = "example"
    CATEGORY = "custom_node/example"

    def example(self):
        return ("Example Custom Node File",)


NODE_CLASS_MAPPINGS = {"Example Custom Node File": ExampleCustomNode}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Example Custom Node": "Example File",
}
