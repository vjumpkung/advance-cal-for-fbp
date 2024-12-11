class ExampleCustomNode1:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    RETURN_TYPES = ("STRING",)
    RETURN_NAME = ("text",)
    DESCRIPTION = "Example"
    FUNCTION = "example"
    CATEGORY = "custom_node/example"

    def example(self):
        return ("Example Custom Node Folder #1",)


NODE_CLASS_MAPPINGS = {"Example Custom Node Folder 1": ExampleCustomNode1}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Example Custom Node": "Example Folder #1",
}
