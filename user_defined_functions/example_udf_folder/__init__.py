from .example_udf_1 import ExampleUDF1  # relative path
from user_defined_functions.example_udf_folder.example_udf_2 import (
    ExampleUDF2,
)  # absolute path


UDF_CLASS_MAPPINGS = {"ExampleUDF1": ExampleUDF1, "ExampleUDF2": ExampleUDF2}
UDF_DISPLAY_NAME_MAPPINGS = {
    "ExampleUDF1": "Example UDF 1",
    "ExampleUDF2": "Example UDF 2",
}
