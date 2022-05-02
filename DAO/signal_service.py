from DAO.database import conection, cur
from DAO.Statergy_service import Statergy_service
from model.signal_model import signal_model

class signal_service(signal_model):
    def Add_signal(self):
        exists=Statergy_service.exists()
        checking_statergy_id = "SELECT * from statergy WHERE Statergy_id = %S"
        cur.execute(checking_statergy_id, (self.statergy_id,))
        get_statergy = cur.fetchone()
        print (get_statergy)



k=signal_service()
n=k.insert_signal()



