class MathOperations:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "operand": (["+", "-", "*", "/", "//", "**", "%"],),
                "a": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
                "b": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "execute"
    DESCRIPTION = "Math Operations"
    CATEGORY = "base/Math"

    def execute(self, a: float, b: float, operand: str):
        return (
            eval(
                f"{a}{operand}{b}",
            ),
        )
