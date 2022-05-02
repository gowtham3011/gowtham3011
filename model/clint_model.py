from DAO.database import conection, cur
class Clint_model:
    def __init__(self,Name:str=None,
                 clint_id:str=None,
                 email_address:str=None,
                 phone_number:str=None,
                 account_balance:str=None)->None:
        self.Name=Name
        self.clint_id=clint_id
        self.email_address=email_address
        self.phone_number=phone_number
        self.account_balance=account_balance

    def create_table(self):
        TITLE = '''CREATE TABLE statergy(statergy_id VARCHAR[], statergy_name VARCHAR[],no_of_signal INTEGER,statergy_status VARCHAR[],list_of_client_placed_order VARCHAR[],no_of_order_placed INTEGER,total_value_of_order_placed INTEGER,creation_time TIMESTAMP,exit_time TIMESTAMP)'''
        k=cur.execute(TITLE),
        conection.commit(),
        conection.close()
        return (k)

l=Clint_model()
t=l.create_table()