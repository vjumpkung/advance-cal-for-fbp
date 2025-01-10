import pandas as pd


class PandasReadFile:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "path": (
                    "STRING",
                    {"select_file_path": True},
                ),
                "filetype": (["CSV", "EXCEL", "JSON"],),
            }
        }

    CATEGORY = "pandas"

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "read_file"

    def read_file(self, path, filetype):
        if filetype == "CSV":
            df = pd.read_csv(path)
        elif filetype == "EXCEL":
            df = pd.read_excel(path)
        elif filetype == "JSON":
            df = pd.read_json(path)

        return (df,)
