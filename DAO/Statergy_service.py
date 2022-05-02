from DAO.database import conection, cur
from model.statergy_model import Statergy_model
import datetime
statergy=Statergy_model.statergy_Model()
class Statergy_service(Statergy_model):
    def exists(self):
        cur.execute("select exists (SELECT statergy_id from statergy WHERE statergy_id =" + self.Statergy_id + ")")
        exists = cur.fetchone()[0]
        print(exists)
        cur.close()
        return exists

    def Create_statergy(self):
        exists = False
        exists=self.exists()
        if(exists==False):
            print ("statergy id Not exist")
            self.Create_New_statergy()
        else:
            print ("the statergy id exist")

        return exists

    def Create_New_statergy(self):
        statergy_status= "open"
        creation_time=self.Creation_time()
        statergy["statergy_id"]=self.Statergy_id
        statergy["statergy_name"]=self.Statergy_name
        statergy["statergy_status"]= statergy_status
        statergy["creation_time"]=creation_time

        return statergy


    def Creation_time(self):
        Date_time = datetime.datetime
        data_format = "%Y%m%d%H%M%S"
        creation_time = Date_time.now().strftime(data_format)
        return creation_time

    def Exit_time(self):
        Date_time = datetime.datetime
        data_format = "%Y%m%d%H%M%S"
        exit_time = Date_time.now().strftime(data_format)
        return exit_time

    def get_statergy_details(self):
        statergy_detail="SELECT * from statergy"
        cur.execute(statergy_detail)
        Detail=cur.fetchall()
        conection.commit()
        return Detail

    def get_statergy_using_statergy_id(statergy_id):

        checking_statergy_id =("SELECT statergy_id from statergy WHERE statergy_id = " + str(statergy_id))
        cur.execute(checking_statergy_id)
        get_statergy = cur.fetchall()
        for row in get_statergy:
            value={row[0]}
        conection.commit()
        conection.close
        return value

    def Exit_statergy(self):
        exists=self.exists()
        if(exists==True and statergy["statergy_status"]!="CLOSED"):
            Exit_time=self.exit_time()
            signal["signal_status"]="closed"
            statergy["exit_time"] = Exit_time

        else:
            print ("statergy id not available for Exit")




g=Statergy_service()
n=g.Create_statergy()

print (n)
