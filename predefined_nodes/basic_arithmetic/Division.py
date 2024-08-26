class DivideNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "dividend": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
                "divisor": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "execute"
    DESCRIPTION = "Divides two numbers"
    CATEGORY = "base/Math"

    def execute(self, dividend, divisor):
        if divisor != 0:
            return (dividend / divisor,)
        else:
            return (float("inf"),)
