class signal_model:
    def __init__(self,signal_id:str=None,
                 signal_name:str=None,
                 price:int=None,
                 quantity:int=None,
                 signal_status:str=None)->None:

        self.signal_id=signal_id
        self.signal_name=signal_name
        self.price=price
        self.quantity=quantity
        self.signal_status=signal_status