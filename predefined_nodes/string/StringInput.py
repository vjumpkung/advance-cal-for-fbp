class TextInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"text": ("STRING", {"multiline": True})}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "execute"
    DESCRIPTION = "Text input"
    CATEGORY = "base"

    def execute(self, text):
        return (text,)
