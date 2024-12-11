class ExampleCustomNode2:
    @classmethod
    def INPUT_TYPES(cls):
        return {}

    RETURN_TYPES = ("STRING",)
    RETURN_NAME = ("text",)
    DESCRIPTION = "Example"
    FUNCTION = "example"
    CATEGORY = "custom_node/example"

    def example(self):
        return ("Example Custom Node Folder #2",)


NODE_CLASS_MAPPINGS = {"Example Custom Node Folder 2": ExampleCustomNode2}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Example Custom Node": "Example Folder #2",
}
