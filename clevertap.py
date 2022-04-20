from initialising.values import fields
from initialising.input import Giving_data
import datetime
fut="FUT"
currency="CURRENCY"
Commodity="COMMODITY"
equity="EQUITY"
call="CALL"
put="PUT"
cash="CASH"
intraday="INTRADAY"
target="target"
stoploss="stoploss"
expire="expire"
researcher="researcher"
buy="BUY"
sell="SELL"

class EditJson:
    def __init__(self,solo):
        self.solo=solo

    def Soloid(self):

        solo_id = self.solo['solo_id']
        return solo_id

    def creationdate(self):

        date = self.solo['solo']['creation_date']
        return date

    def Edit_profile(self):


        Horizon= str.upper(self.solo['solo']['horizon'])
        Market=str.upper( self.solo['solo']['market'])
        Ins_type=str.upper(self.solo['solo']['ins_type'])
        if Market== currency :
            output={
                "name": "Currency",
                "operator": "equals",
                "value": "y"
            }
            return output
        elif Market== Commodity:
            output={
                "name": "Commodity",
                "operator": "equals",
                "value": "y"
            }
            return output

        elif Market == equity:

            if Ins_type==fut:
                output = {
                    "name": "Equity Future",
                    "operator": "equals",
                    "value": "y"
                }
                return output

            elif Ins_type == call or Ins_type==put:
                output = {
                    "name": "Equity Option",
                    "operator": "equals",
                    "value": "y"
                }
                return output

            elif Ins_type==cash:
                if Horizon == "SHORT_TERM" or Horizon=="LONG_TERM":
                    output = {
                        "name": "Delivery Cash",
                        "operator": "equals",
                        "value": "y"
                    }
                    return output
                elif Horizon == intraday:
                    output = {
                        "name": "Intraday Cash",
                        "operator": "equals",
                        "value": "y"
                    }
                    return output
        else:
            return ("values are MISSING")


    def body(self):

        In_Solo_ = (self.solo['solo'])
        Payload =self.payload()
        Payload_with_time=self.payload_time()

        if In_Solo_['status'] =='OPEN':

            Payload['content']['title']='gems to collect today'
            Payload['content']['body']='fresh_notification'
            Payload['content']['platform_specific']['android']['deep_link']=y = "iiflmarketsapp://gems?GEMSOLOID="+self.solo['solo_id']
            Payload['content']['platform_specific']['android']['wzrk_acts'] = [{"l":"Trade Now","dl":y,"id":"1"}]
            Payload['content']['platform_specific']['android']['Cat'] = In_Solo_["transaction"]
            return Payload

        elif In_Solo_['status']=='PENDING':
            Payload['content']['title'] = 'Update on your Gem'
            Payload['content']['body'] = 'fresh_notification'
            Payload['content']['platform_specific']['android']['deep_link']=y = "iiflmarketsapp://gems?GEMSOLOID=" + self.solo['solo_id']
            Payload['content']['platform_specific']['android']['wzrk_acts'] = [{"l": "Trade Now", "dl": y, "id": "1"}]
            Payload['content']['platform_specific']['android']['Cat'] = In_Solo_["transaction"]
            return Payload

        elif In_Solo_['status']=='CLOSED':
            if In_Solo_['closed_by']==target:
                Payload_with_time['content']['title']='awsome hit on symbol'
                Payload_with_time['content']['body'] = "target reached"
                Payload_with_time['content']['platform_specific']['android']['deep_link'] = "iiflmarketsapp://gems?GEMSOLOID="+self.solo['solo_id']
                Payload_with_time['content']['platform_specific']['android']['wzrk_acts'] = self.trade()
                Payload_with_time['content']['platform_specific']['android']['Cat']=In_Solo_["transaction"]
                return (Payload_with_time)


            elif In_Solo_['closed_by']== stoploss:
                Payload_with_time['content']['title']='sl triggered on'
                Payload_with_time['content']['body'] = "triggered stoploss"
                Payload_with_time['content']['platform_specific']['android']['deep_link'] = "iiflmarketsapp://gems?GEMSOLOID="+self.solo['solo_id']
                Payload_with_time['content']['platform_specific']['android']['wzrk_acts'] = self.trade()
                Payload_with_time['content']['platform_specific']['android']['Cat']=In_Solo_["transaction"]
                return Payload_with_time

            elif In_Solo_['closed_by']== expire:
                Payload_with_time['content']['title']='date closed'
                Payload_with_time['content']['body'] = "signal expired"
                Payload_with_time['content']['platform_specific']['android']['deep_link'] = "iiflmarketsapp://gems?GEMSOLOID="+self.solo['solo_id']
                Payload_with_time['content']['platform_specific']['android']['wzrk_acts'] = self.trade()
                Payload_with_time['content']['platform_specific']['android']['Cat']=In_Solo_["transaction"]
                return (Payload_with_time)

            elif In_Solo_['closed_by']== researcher:
                Payload_with_time['content']['title']='closed by researcher'
                Payload_with_time['content']['body'] = "closed by researcher"
                Payload_with_time['content']['platform_specific']['android']['deep_link'] = "iiflmarketsapp://gems?GEMSOLOID="+self.solo['solo_id']
                Payload_with_time['content']['platform_specific']['android']['wzrk_acts'] =self.trade()
                Payload_with_time['content']['platform_specific']['android']['Cat']=In_Solo_["transaction"]
                return Payload_with_time

    def trade(self):

        In_Solo_ = (self.solo['solo'])

        if In_Solo_["transaction"]==sell:
            y=[{"l":"Trade Now","dl":"iiflmarketsapp://Buypage?SM="+(In_Solo_['symbol'])+"&SC="+str(In_Solo_['broker_code'])+"&EX="+(In_Solo_["broker_exchange"])+"&EXT="+(In_Solo_["broker_exchange_type"]),"id":"1"}]
            return y
        elif In_Solo_["transaction"]==buy:
            y = [{"l": "Trade Now", "dl": "iiflmarketsapp://sellpage?SM=" + (In_Solo_['symbol']) + "&SC=" + str(In_Solo_['broker_code']) + "&EX=" + (In_Solo_["broker_exchange"]) + "&EXT=" + (In_Solo_["broker_exchange_type"]), "id": "1"}]
            return y

    def event_name(self):

        In_Solo_ = (self.solo['solo'])

        if In_Solo_["transaction"]==sell:
            y="OP_Buy Completed"
            return y
        elif In_Solo_["transaction"]==buy:
            y="op_Sell Completed"
            return y

    def timedate():
        current_time=datetime.datetime
        data_format = "%Y%m%d%H%M%S"
        to = datetime.datetime.now().strftime(data_format)
        return to


    def payload(self):
         clever ={  "name": "IIFL IDEAS Campaign",
                    "skip_estimate": True,
                    "estimate_only": False,
                    "target_mode": "push",
                    "where": {
                                "common_profile_properties": {
                                                                "profile_fields": [
                                                                        self.Edit_profile()
                                                                ]

                                }
                    },
                    "respect_frequency_caps": False,
                    "content": {
                        "title": "IIFL IDEAS",
                        "body": "data",
                        "platform_specific": {
                                "ios": {
                                    "mutable-content": "true",
                                    "Cat": "NCA",
                                    "SR": "CVT"
                                },
                                "android": {
                                    "default_sound": True,
                                    "wzrk_cid": "iiflMarkets_channel",
                                    "deep_link":
                                    "iiflmarketsapp://gems?GEMSOLOID=34cef13ce2e24736896d97c9cade5407",
                                    "wzrk_acts": [{"l":"Trade Now","dl":"iiflmarketsapp://gems?GEMSOLOID=34cef13ce2e24736896d97c9cade5407","id":"1"}],
                                    "Cat": "GEM",
                                    "SR":"CVT",
                                    "ttl":24
                                }
                          },
                    }
                }
         return clever

    def payload_time(self):
       expire_date= {
                "name": "Gemrush Campaign test",
                "skip_estimate": False,
                "estimate_only": False,
                "target_mode":"push",
                "where": {
                            "event_name": self.event_name(),
                            "event_properties": [
                                {
                                    "name": "GEMID",
                                    "operator": "equals",
                                    "value": self.Soloid()
                                }
                                ],
                            "from": self.creationdate(),
                            "to": EditJson.timedate(),
                            },
                "respect_frequency_caps": False,
                "content": {
                    "title": "IIFL Ideas",
                    "body": "Test Personal",
                    "platform_specific": {
                        "ios": {
                            "mutable-content": "true",
                            "Cat": "GEM",
                            "SR":"CVT"
                        },
                        "android": {
                            "default_sound": True,
                            "wzrk_cid": "iiflMarkets_channel",
                            "deep_link": "iiflmarketsapp://gems?GEMSOLOID=34cef13ce2e24736896d97c9cade5407",
                            "wzrk_acts": [{"l":"TradeNow","dl":"iiflmarketsapp://gems?GEMSOLOID=34cef13ce2e24736896d97c9cade5407","id":"1"}],
                                "Cat": "GEM",
                                "SR":"CVT",

                                "ttl":24
                            }
                        }
                        },
                    "devices": [
                                "ios",
                                "android"
                                ],
                    "when": "now"
                    }
       return expire_date
v=Giving_data.give_data()
a=EditJson(v)
print(a.body())