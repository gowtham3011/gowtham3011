from DAO.database import conection, cur

class Statergy_model:
    def __init__(self,
                 statergy_id:str=None,
                 statergy_name:str=None,
                 no_of_Signal:int=None,
                 statergy_status:str=None,
                 no_of_order_placed:int=None,
                 total_value_of_order_placed:int=None,
                 creation_time:int=None,
                 exit_time:int=None)->None:
        super().__init__()
        self.Statergy_id = statergy_id
        self.Statergy_name = statergy_name
        self.No_of_Signal = no_of_Signal
        self.Statergy_status = statergy_status
        self.No_of_order_placed = no_of_order_placed
        self.Total_value_of_order_placed = total_value_of_order_placed
        self.creation_time = creation_time
        self.exit_time = exit_time

    def statergy_Model():
        Statergy_Model={ "Statergy_id":str,
                         "Statergy_name":str,
                         "no_of_signal":int,
                         "statergy_status":str,
                         "list_of_client_placed_order": list[str],
                         "no_of_order_placed": int ,
                         "totalvalue_of_order_placed": int,
                         "creation_time": int,
                         "exit_time":int}

        return Statergy_Model

    def insert_signal(self):
        v=Statergy_model.statergy_Model()
        value=v.values()

        Insert_signal=('''INSERT INTO statergy (statergy_id,statergy_name,no_of_signal,statergy_status,list_of_clint_placed_order,no_of_order_placed,total_value_of_order_placed,creation_time,exit_time) VALUES (%s,%s,%s,%%s,%s,%s,%s,%s,%s)''')
        k=cur.execute(Insert_signal,value)
        conection.commit()
        return (k)

k=Statergy_model()
n=k.insert_signal()
print(n)

