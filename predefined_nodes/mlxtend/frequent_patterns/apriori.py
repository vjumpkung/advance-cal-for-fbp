from mlxtend.frequent_patterns import apriori


class MlxtendApriori:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "dataframe": ("PD_DATAFRAME",),
                "min_support": ("FLOAT", {"min": 0, "max": 1}),
            }
        }

    CATEGORY = "mlxtend/frequent_patterns"

    RETURN_NAMES = ("dataframe",)

    RETURN_TYPES = ("PD_DATAFRAME",)

    FUNCTION = "ap"

    def ap(self, dataframe, min_support):

        frequent_itemsets = apriori(
            dataframe, min_support=min_support, use_colnames=True
        )

        return (frequent_itemsets,)
