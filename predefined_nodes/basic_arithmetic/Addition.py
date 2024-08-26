class AddNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "operand1": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
                "operand2": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                ),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "execute"
    DESCRIPTION = "Adds two numbers together"
    CATEGORY = "base/Math"

    def execute(self, operand1: float, operand2: float):
        return (operand1 + operand2,)
