class MultiplyNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "factor1": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
                "factor2": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "execute"
    DESCRIPTION = "Multiplies two numbers"
    CATEGORY = "base/Math"

    def execute(self, factor1, factor2):
        return (factor1 * factor2,)
