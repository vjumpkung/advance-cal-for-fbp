# importing nodes
from predefined_nodes.basic_arithmetic.Addition import AddNode
from predefined_nodes.basic_arithmetic.Subtraction import SubtractNode
from predefined_nodes.basic_arithmetic.Multiplication import MultiplyNode
from predefined_nodes.basic_arithmetic.Division import DivideNode
from predefined_nodes.basic_arithmetic.operations import MathOperations
from predefined_nodes.stdout.PrintFloat import OutputFloatToStdoutNode
from predefined_nodes.stdout.PrintString import OutputStringToStdoutNode
from predefined_nodes.string.StringConcat import StringConcatNode
from predefined_nodes.string.StringInput import TextInputNode
from predefined_nodes.basic_arithmetic.FloatInput import FloatInputNode
from predefined_nodes.types_conversion.FloatToString import ConvertFloatToString
from predefined_nodes.numpy.ndarray import createNumpy1DArray
from predefined_nodes.stdout.PrintAny import PrintAny
from predefined_nodes.stdout.ShowText import ShowText
from predefined_nodes.stdin.ReadFile import ReadFile
from predefined_nodes.stdout.WriteFile import WriteFile

import logging
import threading


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


NODE_CLASS_MAPPINGS: dict = {
    "Add": AddNode,
    "Subtract": SubtractNode,
    "Multiply": MultiplyNode,
    "Divide": DivideNode,
    "MathOperations": MathOperations,
    "FLOATValue": FloatInputNode,
    "OutputFloatToStdout": OutputFloatToStdoutNode,
    "OutputStringToStdout": OutputStringToStdoutNode,
    "TextInputNode": TextInputNode,
    "ConvertFloatToString": ConvertFloatToString,
    "StringConcatNode": StringConcatNode,
    "Print into console": PrintAny,
    "create numpy 1d array": createNumpy1DArray,
    "ShowText": ShowText,
    "ReadFile": ReadFile,
    "WriteFile": WriteFile,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Add": "Addition",
    "Subtract": "Subtraction",
    "Multiply": "Multiplication",
    "Divide": "Division",
    "MathOperations": "Math Operations",
    "FLOATValue": "Float Value Input",
    "OutputFloatToStdout": "Print Float into Console",
    "OutputStringToStdout": "Print String into Console",
    "TextInputNode": "String Value Input",
    "ConvertFloatToString": "Convert Float To String",
    "StringConcatNode": "Combine String",
    "Print into console": "Print",
    "create numpy 1d array": "create np 1D array",
    "ShowText": "Show Text",
    "ReadFile": "Read File from path",
    "WriteFile": "Write string into text file.",
}


def init_external_custom_nodes():
    base_node_names = set(NODE_CLASS_MAPPINGS.keys())
    logging.debug("Loading Custom Node will Do later")
