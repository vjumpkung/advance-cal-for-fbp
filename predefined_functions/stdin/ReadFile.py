class ReadFile:
    @classmethod
    def INPUT_TYPES(self):
        return {"required": {"path": ("STRING", {"select_file_path": True})}}

    CATEGORY = "utils"

    RETURN_TYPES = ("STRING",)

    FUNCTION = "read_file"

    def read_file(self, path):
        f = r""

        with open(path, "r", encoding="utf-8") as fp:
            f = fp.read()

        return (f,)
