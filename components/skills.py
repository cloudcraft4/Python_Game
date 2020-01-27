class skill:
    def __init__(self, use_function=None, targeting=False, targeting_message=None, mana_cost=None, **kwargs):
        self.use_function = use_function
        self.targeting = targeting
        self.targeting_message = targeting_message
        self.function_kwargs = kwargs
        self.mana_cost = mana_cost
