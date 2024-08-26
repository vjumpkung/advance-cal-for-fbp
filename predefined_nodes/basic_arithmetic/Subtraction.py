class SubtractNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "minuend": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
                "subtrahend": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "subtract"
    DESCRIPTION = "Subtracts two numbers"
    CATEGORY = "base/Math"

    def subtract(self, minuend, subtrahend):
        return (minuend - subtrahend,)
