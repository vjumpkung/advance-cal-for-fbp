class AnyType(str):
    """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

    def __eq__(self, _) -> bool:
        return True

    def __ne__(self, __value: object) -> bool:
        return False


any = AnyType("*")


class PrintAny:
    @classmethod
    def INPUT_TYPES(cls):
        return {"optional": {"any": (any,)}}

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    DESCRIPTION = "print into console"
    FUNCTION = "execute"
    CATEGORY = "base/stdout"
    OUTPUT_NODE = True

    def execute(self, any=None):
        print(any)
        return ()
