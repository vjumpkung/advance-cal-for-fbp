class OutputFloatToStdoutNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": (
                    "FLOAT",
                    {
                        "forceInput": True,
                    },
                )
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    DESCRIPTION = "print float into console"
    FUNCTION = "execute"
    CATEGORY = "base/stdout"
    OUTPUT_NODE = True

    def execute(self, value):
        print(value)
        return ()
