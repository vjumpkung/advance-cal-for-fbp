# importing nodes
from predefined_nodes.basic_arithmetic.operations import MathOperations
from predefined_nodes.stdout.PrintFloat import OutputFloatToStdoutNode
from predefined_nodes.stdout.PrintString import OutputStringToStdoutNode
from predefined_nodes.string.StringConcat import StringConcatNode
from predefined_nodes.string.StringInput import TextInputNode
from predefined_nodes.basic_arithmetic.FloatInput import FloatInputNode
from predefined_nodes.types_conversion.FloatToString import ConvertFloatToString
from predefined_nodes.stdout.PrintAny import PrintAny
from predefined_nodes.stdout.ShowText import ShowText
from predefined_nodes.stdin.ReadFile import ReadFile
from predefined_nodes.stdout.WriteFile import WriteFile
from predefined_nodes.pandas.PandasReadFile import PandasReadFile
from predefined_nodes.pandas.ValueCount import PandasValueCounts
from predefined_nodes.types_conversion.AnyToString import ConvertAnyToString

import traceback
import importlib
import importlib.util
import logging
import threading
import time
import sys
import os


class InterruptProcessingException(Exception):
    pass


interrupt_processing_mutex = threading.RLock()

interrupt_processing = False


def interrupt_current_processing(value=True):
    global interrupt_processing
    global interrupt_processing_mutex
    with interrupt_processing_mutex:
        interrupt_processing = value


def processing_interrupted():
    global interrupt_processing
    global interrupt_processing_mutex
    with interrupt_processing_mutex:
        return interrupt_processing


def throw_exception_if_processing_interrupted():
    global interrupt_processing
    global interrupt_processing_mutex
    with interrupt_processing_mutex:
        if interrupt_processing:
            interrupt_processing = False
            raise InterruptProcessingException()


def before_node_execution():
    throw_exception_if_processing_interrupted()


NODE_CLASS_MAPPINGS: dict = {
    "MathOperations": MathOperations,
    "FLOATValue": FloatInputNode,
    "OutputFloatToStdout": OutputFloatToStdoutNode,
    "OutputStringToStdout": OutputStringToStdoutNode,
    "TextInputNode": TextInputNode,
    "ConvertFloatToString": ConvertFloatToString,
    "StringConcatNode": StringConcatNode,
    "Print into console": PrintAny,
    "ShowText": ShowText,
    "ReadFile": ReadFile,
    "WriteFile": WriteFile,
    "PandasReadFile": PandasReadFile,
    "PandasValueCounts": PandasValueCounts,
    "AnyToString": ConvertAnyToString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MathOperations": "Math Operations",
    "FLOATValue": "Float Value Input",
    "OutputFloatToStdout": "Print Float into Console",
    "OutputStringToStdout": "Print String into Console",
    "TextInputNode": "String Value Input",
    "ConvertFloatToString": "Convert Float To String",
    "StringConcatNode": "Combine String",
    "Print into console": "Print",
    "ShowText": "Show Text",
    "ReadFile": "Read File from path",
    "WriteFile": "Write string into text file.",
    "PandasReadFile": "Pandas Read File",
    "PandasValueCounts": "Pandas Count unique values in specific column",
    "AnyToString": "Convert Any To String",
}

folder_names_and_paths = {}

base_path = os.path.dirname(os.path.realpath(__file__))

folder_names_and_paths["custom_nodes"] = (
    [os.path.join(base_path, "custom_nodes")],
    set(),
)


def get_module_name(module_path: str) -> str:
    base_path = os.path.basename(module_path)
    if os.path.isfile(module_path):
        base_path = os.path.splitext(base_path)[0]
    return base_path


def get_folder_paths(folder_name: str) -> list[str]:
    return folder_names_and_paths[folder_name][0][:]


def load_custom_node(
    module_path: str, ignore=set(), module_parent="custom_nodes"
) -> bool:
    module_name = os.path.basename(module_path)
    if os.path.isfile(module_path):
        sp = os.path.splitext(module_path)
        module_name = sp[0]
    try:
        logging.debug("Trying to load custom node {}".format(module_path))
        if os.path.isfile(module_path):
            # file based custom node
            module_spec = importlib.util.spec_from_file_location(
                module_name, module_path
            )
        else:
            # folder based custom node
            module_spec = importlib.util.spec_from_file_location(
                module_name, os.path.join(module_path, "__init__.py")
            )

        module = importlib.util.module_from_spec(module_spec)
        sys.modules[module_name] = module
        module_spec.loader.exec_module(module)

        if (
            hasattr(module, "NODE_CLASS_MAPPINGS")
            and getattr(module, "NODE_CLASS_MAPPINGS") is not None
        ):
            for name, node_cls in module.NODE_CLASS_MAPPINGS.items():
                if name not in ignore:
                    NODE_CLASS_MAPPINGS[name] = node_cls
                    node_cls.RELATIVE_PYTHON_MODULE = "{}.{}".format(
                        module_parent, get_module_name(module_path)
                    )
            if (
                hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS")
                and getattr(module, "NODE_DISPLAY_NAME_MAPPINGS") is not None
            ):
                NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
            return True
        else:
            logging.warning(
                f"Skip {module_path} module for custom nodes due to the lack of NODE_CLASS_MAPPINGS."
            )
            return False
    except Exception as e:
        logging.warning(traceback.format_exc())
        logging.warning(f"Cannot import {module_path} module for custom nodes: {e}")
        return False


def init_external_custom_nodes():
    base_node_names = set(NODE_CLASS_MAPPINGS.keys())
    node_paths = get_folder_paths("custom_nodes")
    node_import_times = []
    for custom_node_path in node_paths:

        possible_modules = os.listdir(os.path.realpath(custom_node_path))
        if "__pycache__" in possible_modules:
            possible_modules.remove("__pycache__")

        for possible_module in possible_modules:

            module_path = os.path.join(custom_node_path, possible_module)
            if (
                os.path.isfile(module_path)
                and os.path.splitext(module_path)[1] != ".py"
            ):
                continue
            if module_path.endswith(".disabled"):
                continue
            time_before = time.perf_counter()
            success = load_custom_node(
                module_path, base_node_names, module_parent="custom_nodes"
            )
            node_import_times.append(
                (time.perf_counter() - time_before, module_path, success)
            )

    if len(node_import_times) > 0:
        logging.info("Import times for custom nodes:")
        for n in sorted(node_import_times):
            if n[2]:
                import_message = ""
            else:
                import_message = " (IMPORT FAILED)"
            logging.info("{:6.1f} seconds{}: {}".format(n[0], import_message, n[1]))
