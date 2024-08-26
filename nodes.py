# importing nodes
from predefined_nodes.basic_arithmetic.Addition import AddNode
from predefined_nodes.basic_arithmetic.Subtraction import SubtractNode
from predefined_nodes.basic_arithmetic.Multiplication import MultiplyNode
from predefined_nodes.basic_arithmetic.Division import DivideNode
from predefined_nodes.stdout.PrintFloat import OutputFloatToStdoutNode
from predefined_nodes.stdout.PrintString import OutputStringToStdoutNode
from predefined_nodes.string.StringConcat import StringConcatNode
from predefined_nodes.string.StringInput import TextInputNode
from predefined_nodes.basic_arithmetic.FloatInput import FloatInputNode
from predefined_nodes.types_conversion.FloatToString import ConvertFloatToString

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
    "FLOATValue": FloatInputNode,
    "OutputFloatToStdout": OutputFloatToStdoutNode,
    "OutputStringToStdout": OutputStringToStdoutNode,
    "TextInputNode": TextInputNode,
    "ConvertFloatToString": ConvertFloatToString,
    "StringConcatNode": StringConcatNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Add": "Addition",
    "Subtract": "Subtraction",
    "Multiply": "Multiplication",
    "Divide": "Division",
    "FLOATValue": "Float Value Input",
    "OutputFloatToStdout": "Print Float into Console",
    "OutputStringToStdout": "Print String into Console",
    "TextInputNode": "String Value Input",
    "ConvertFloatToString": "Convert Float To String",
    "StringConcatNode": "Combine String",
}


def init_external_custom_nodes():
    base_node_names = set(NODE_CLASS_MAPPINGS.keys())
    logging.debug("Loading Custom Node will Do later")
