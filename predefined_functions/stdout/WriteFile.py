import os


class WriteFile:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "path": ("STRING",),
                "filename": ("STRING",),
                "text": (
                    "STRING",
                    {
                        "forceInput": True,
                    },
                ),
            }
        }

    CATEGORY = "utils"

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "base/stdout"
    OUTPUT_NODE = True

    def execute(self, path, filename, text):
        with open(os.path.join(path, filename), "w+", encoding="utf-8") as fp:
            fp.write(str(text[0]))
        return ()
