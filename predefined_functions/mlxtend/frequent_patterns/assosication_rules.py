from mlxtend.frequent_patterns import association_rules


class MlxtendAssosicationRules:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "min_threshold": ("FLOAT", {"min": 0, "max": 1}),
                "metric": (["confidence", "lift"], {"defaultVal": "confidence"}),
            }
        }

    CATEGORY = "mlxtend/frequent_patterns"

    RETURN_NAMES = ("dataframe",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "ar"

    def ar(self, dataframe, min_threshold, metric):

        frequent_itemsets = association_rules(
            dataframe,
            num_itemsets=len(dataframe),
            metric=metric,
            min_threshold=min_threshold,
        )

        return (frequent_itemsets,)
