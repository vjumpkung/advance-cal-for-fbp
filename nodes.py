# importing nodes
import importlib
import importlib.util
import logging
import os
import sys
import threading
import time
import traceback

from predefined_functions.basic_arithmetic.FloatInput import FloatInputNode
from predefined_functions.basic_arithmetic.operations import MathOperations
from predefined_functions.image.previewimage import PreviewImage
from predefined_functions.imblearn.over_sampling.SMOTE import ImblearnSmote
from predefined_functions.matplotlib.scatter_plot import CreateScatterPlot
from predefined_functions.mlxtend.frequent_patterns.apriori import MlxtendApriori
from predefined_functions.mlxtend.frequent_patterns.assosication_rules import (
    MlxtendAssosicationRules,
)
from predefined_functions.mlxtend.preprocessing.TransactionEncoder import (
    MlxtendTransactionEncoder,
)
from predefined_functions.pandas.AddColumn import PandasAddColumn
from predefined_functions.pandas.AsType import PandasAsType
from predefined_functions.pandas.CheckDataTypes import PandasCheckDtypes
from predefined_functions.pandas.ColumnStatisticsCalculate import (
    PandasColumnStatisticsCalculate,
)
from predefined_functions.pandas.CombineColumn import PandasCombineColumn
from predefined_functions.pandas.Cut import PandasCut
from predefined_functions.pandas.DropColumn import PandasDropColumn
from predefined_functions.pandas.FillNA import PandasFillNA
from predefined_functions.pandas.GetDummies import PandasGetDummies
from predefined_functions.pandas.MathOperationIntoColumn import (
    PandasMathOperationIntoColumn,
)
from predefined_functions.pandas.PandasReadFile import PandasReadFile
from predefined_functions.pandas.PandasSaveFile import PandasSaveFile
from predefined_functions.pandas.RemoveNA import PandasRemoveNA
from predefined_functions.pandas.SplitColumn import SplitColumn
from predefined_functions.pandas.ToNumeric import PandasToNumeric
from predefined_functions.pandas.ValueCount import PandasValueCounts
from predefined_functions.seaborn.ShowMissingValueHeatmap import ShowMissingValueHeatMap
from predefined_functions.sklearn.cluster.Kmeans import SklearnKmeans
from predefined_functions.sklearn.compose.ColumnTransformers import (
    SklearnColumnTransformer,
)
from predefined_functions.sklearn.impute.IterativeImputer import SklearnIterativeImputer
from predefined_functions.sklearn.linear_model.LinearRegression import (
    SklearnLinearRegression,
)
from predefined_functions.sklearn.linear_model.LogisticRegression import (
    SklearnLogisticRegression,
)
from predefined_functions.sklearn.metrics.ClassificationReport import (
    SklearnClassificationReport,
)
from predefined_functions.sklearn.metrics.ModelScore import SklearnModelScore
from predefined_functions.sklearn.model_selection.TrainTestSplit import (
    SklearnTrainTestSplit,
)
from predefined_functions.sklearn.neighbors.KNeighborsClassifier import (
    SklearnKNeighborsClassifier,
)
from predefined_functions.sklearn.predict.Predict import SklearnModelPredict
from predefined_functions.sklearn.preprocessing.FitTransformPreprocessModel import (
    SklearnFitTransformPreprocessModel,
)
from predefined_functions.sklearn.preprocessing.FitTransformPreprocessModelPandas import (
    SklearnFitTransformPreprocessModelPandas,
)
from predefined_functions.sklearn.preprocessing.LabelEncoder import SklearnLabelEncoder
from predefined_functions.sklearn.preprocessing.MinMaxScaler import SklearnMinMaxScaler
from predefined_functions.sklearn.preprocessing.OneHotEncoder import (
    SklearnOneHotEncoder,
)
from predefined_functions.sklearn.preprocessing.StandardScaler import (
    SklearnStandardScaler,
)
from predefined_functions.sklearn.preprocessing.TransformPreprocessModel import (
    SklearnTransformPreprocessModel,
)
from predefined_functions.sklearn.preprocessing.TransformPreprocessModelPandas import (
    SklearnTransformPreprocessModelPandas,
)
from predefined_functions.sklearn.tree.DecisionTree import SklearnDecisionTree
from predefined_functions.sklearn.utils.resample import FixImbalanceClass
from predefined_functions.stdin.ReadFile import ReadFile
from predefined_functions.stdout.PrintAny import PrintAny
from predefined_functions.stdout.PrintFloat import OutputFloatToStdoutNode
from predefined_functions.stdout.PrintString import OutputStringToStdoutNode
from predefined_functions.stdout.ShowText import ShowText
from predefined_functions.stdout.WriteFile import WriteFile
from predefined_functions.string.StringConcat import StringConcatNode
from predefined_functions.string.StringInput import TextInputNode
from predefined_functions.types_conversion.AnyToNpArray import AnyToNumPyArray
from predefined_functions.types_conversion.AnyToString import ConvertAnyToString
from predefined_functions.types_conversion.FloatToString import ConvertFloatToString
from predefined_functions.sklearn.preprocessing.LabelEncoderFitTransform import (
    SklearnLabelEncoderFitTransform,
)
from predefined_functions.sklearn.preprocessing.FitTransformPreprocessingModel import (
    SklearnPreprocessingModelFitTransform,
)


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


UDF_CLASS_MAPPINGS: dict = {
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
    "ShowMissingValueHeatMap": ShowMissingValueHeatMap,
    "PandasSelectDtypes": PandasCheckDtypes,
    "SklearnTrainTestSplit": SklearnTrainTestSplit,
    "PandasSplitColumn": SplitColumn,
    "SklearnLinearRegression": SklearnLinearRegression,
    "SklearnModelPredict": SklearnModelPredict,
    "SklearnModelScore": SklearnModelScore,
    "SklearnLogisticRegression": SklearnLogisticRegression,
    "SklearnFitTransformPreprocessModel": SklearnFitTransformPreprocessModel,
    "SklearnLabelEncoder": SklearnLabelEncoder,
    "PandasDropColumn": PandasDropColumn,
    "PandasFillNA": PandasFillNA,
    "PandasRemoveNA": PandasRemoveNA,
    "PandasColumnStatisticsCalculate": PandasColumnStatisticsCalculate,
    "SklearnOneHotEncoder": SklearnOneHotEncoder,
    "AnyToNumpyArray": AnyToNumPyArray,
    "SklearnColumnTransformer": SklearnColumnTransformer,
    "SklearnStandardScaler": SklearnStandardScaler,
    "SklearnTransformPreprocessModel": SklearnTransformPreprocessModel,
    "SklearnKNeighborsClassifier": SklearnKNeighborsClassifier,
    "SklearnClassificationReport": SklearnClassificationReport,
    "PandasCombineColumn": PandasCombineColumn,
    "PandasMathOperationIntoColumn": PandasMathOperationIntoColumn,
    "SklearnIterativeImputerMICE": SklearnIterativeImputer,
    "SklearnFitTransformPreprocessModelPandas": SklearnFitTransformPreprocessModelPandas,
    "SklearnTransformPreprocessModelPandas": SklearnTransformPreprocessModelPandas,
    "SklearnKmeans": SklearnKmeans,
    "SklearnMinMaxScaler": SklearnMinMaxScaler,
    "PandasAddColumn": PandasAddColumn,
    "PandasAsType": PandasAsType,
    "MlxtendApriori": MlxtendApriori,
    "MlxtendAssosicationRules": MlxtendAssosicationRules,
    "MlxtendTransactionEncoder": MlxtendTransactionEncoder,
    "PandasCut": PandasCut,
    "PandasGetDummies": PandasGetDummies,
    "SklearnDecisionTree": SklearnDecisionTree,
    "ImblearnSmote": ImblearnSmote,
    "PandasToNumeric": PandasToNumeric,
    "FixImbalanceClass": FixImbalanceClass,
    "MatPlotlibScatterPlot": CreateScatterPlot,
    "PreviewImage": PreviewImage,
    "PandasSaveFile": PandasSaveFile,
    "SklearnPreprocessingModelFitTransform": SklearnPreprocessingModelFitTransform,
}

UDF_DISPLAY_NAME_MAPPINGS = {
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
    "PandasValueCounts": "Pandas Count unique values",
    "AnyToString": "Convert Any To String",
    "ShowMissingValueHeatMap": "Show Missing Value Heatmap",
    "PandasSelectDtypes": "Pandas Select Datatypes",
    "SklearnTrainTestSplit": "Data Train Test Split",
    "PandasSplitColumn": "Pandas Split Column",
    "SklearnLinearRegression": "Linear Regression",
    "SklearnModelPredict": "Model Predict",
    "SklearnModelScore": "Genearate Model Score",
    "SklearnLogisticRegression": "Logistic Regression",
    "SklearnFitTransformPreprocessModel": "(deprecated) Fit Transform data using Preprocessing Model",
    "PandasDropColumn": "Drop Column",
    "PandasFillNA": "Fill Missing Value",
    "PandasRemoveNA": "Drop Missing Value Rows",
    "PandasColumnStatisticsCalculate": "Statistics calculate in column",
    "SklearnLabelEncoder": "Label Encoder Preprocessing Model",
    "SklearnOneHotEncoder": "One Hot Encoder Preprocessing Model",
    "AnyToNumpyArray": "Convert To NumpyArray",
    "SklearnColumnTransformer": "Column Transformer",
    "SklearnStandardScaler": "Standard Scaler Preprocessing Model",
    "SklearnTransformPreprocessModel": "(deprecated) Transform data using Preprocessing Model",
    "SklearnKNeighborsClassifier": "Known Nearest Neighbors (KNN) Model",
    "SklearnClassificationReport": "Classificaton Report",
    "PandasCombineColumn": "Combine Column(s) by math operation",
    "PandasMathOperationIntoColumn": "Math operation into column(s)",
    "SklearnIterativeImputerMICE": "MICE preprocessing method",
    "SklearnFitTransformPreprocessModelPandas": "(deprecated) Fit Transform data using Preprocessing Model (PANDAS)",
    "SklearnTransformPreprocessModelPandas": "(deprecated) Transform data using Preprocessing Model (PANDAS)",
    "SklearnKmeans": "K-Means Clustering Model",
    "SklearnMinMaxScaler": "Min-Max Scaler Preprocessing Model",
    "PandasAddColumn": "Add Column into Dataframe",
    "PandasAsType": "Pandas Dataframe AsType",
    "MlxtendApriori": "Apriori Frequent Itemset",
    "MlxtendAssosicationRules": "Generate Assosication Rules",
    "MlxtendTransactionEncoder": "Transaction Encoder Preprocessing Model",
    "PandasCut": "Pandas Cut",
    "PandasGetDummies": "Pandas Get Dummies",
    "SklearnDecisionTree": "Decison Tree Model",
    "ImblearnSmote": "Over-sampling by SMOTE",
    "PandasToNumeric": "Convert Dataframe column into Numeric",
    "FixImbalanceClass": "Fix Imbalance Class by resampling",
    "MatPlotlibScatterPlot": "Create Scatter Plot",
    "PreviewImage": "Preview Image",
    "PandasSaveFile": "Pandas Save File",
    "SklearnLabelEncoderFitTransform": "Label Encoder Fit Transform",
    "SklearnPreprocessingModelFitTransform": "Preprocessing Model Fit Transform",
}

folder_names_and_paths = {}

base_path = os.path.dirname(os.path.realpath(__file__))

folder_names_and_paths["user_defined_functions"] = (
    [os.path.join(base_path, "user_defined_functions")],
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
    module_path: str, ignore=set(), module_parent="user_defined_functions"
) -> bool:
    module_name = os.path.basename(module_path)
    if os.path.isfile(module_path):
        sp = os.path.splitext(module_path)
        module_name = sp[0]
    try:
        logging.debug("Trying to load user defined function {}".format(module_path))
        if os.path.isfile(module_path):
            # file based udf
            module_spec = importlib.util.spec_from_file_location(
                module_name, module_path
            )
        else:
            # folder based udf
            module_spec = importlib.util.spec_from_file_location(
                module_name, os.path.join(module_path, "__init__.py")
            )

        module = importlib.util.module_from_spec(module_spec)
        sys.modules[module_name] = module
        module_spec.loader.exec_module(module)

        if (
            hasattr(module, "UDF_CLASS_MAPPINGS")
            and getattr(module, "UDF_CLASS_MAPPINGS") is not None
        ):
            for name, node_cls in module.UDF_CLASS_MAPPINGS.items():
                if name not in ignore:
                    UDF_CLASS_MAPPINGS[name] = node_cls
                    node_cls.RELATIVE_PYTHON_MODULE = "{}.{}".format(
                        module_parent, get_module_name(module_path)
                    )
            if (
                hasattr(module, "UDF_DISPLAY_NAME_MAPPINGS")
                and getattr(module, "UDF_DISPLAY_NAME_MAPPINGS") is not None
            ):
                UDF_DISPLAY_NAME_MAPPINGS.update(module.UDF_DISPLAY_NAME_MAPPINGS)
            return True
        else:
            logging.warning(
                f"Skip {module_path} module for user defined function due to the lack of NODE_CLASS_MAPPINGS."
            )
            return False
    except Exception as e:
        logging.warning(traceback.format_exc())
        logging.warning(
            f"Cannot import {module_path} module for user defined function: {e}"
        )
        return False


def init_external_custom_nodes():
    base_node_names = set(UDF_CLASS_MAPPINGS.keys())
    node_paths = get_folder_paths("user_defined_functions")
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
                module_path, base_node_names, module_parent="user_defined_functions"
            )
            node_import_times.append(
                (time.perf_counter() - time_before, module_path, success)
            )

    if len(node_import_times) > 0:
        logging.info("Import times for user defined functions:")
        for n in sorted(node_import_times):
            if n[2]:
                import_message = ""
            else:
                import_message = " (IMPORT FAILED)"
            logging.info("{:6.1f} seconds{}: {}".format(n[0], import_message, n[1]))
