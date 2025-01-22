class FloatInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": ("FLOAT", {})}}

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("value",)
    DESCRIPTION = "Value input"
    FUNCTION = "execute"
    CATEGORY = "base/Math"

    def execute(self, value):
        return (value,)
