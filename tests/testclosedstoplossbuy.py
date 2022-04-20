import unittest
from clevertap import EditJson

event = {
        "solo_id": "84eba3adbf7240798c621ad41ba5e3c6",
        "event": "OPEN",
        "solo":
            {
                "id": "066670c4b1044f7e9d77c0bbbb0f0060",
                "broker": "iifl",
                "topic": "95d24dbbec0d41af921487c0992186fc",
                "status": "CLOSED",
                "lot_size": 1000,
                "entry_price": {
                    "from": 83.64,
                    "to": 83.68
                },
                "full_name": "EURINR • 29 Mar 2022 • FUT",
                "market": "equity",
                "target_price": 83.2,
                "broker_isin": "EURINR",
                "history": {
                    "0": {
                        "symbol": "EURINR",
                        "broker_code": 1762,
                        "closed_date": None,
                        "unique_identifier": "iifl-currency-fut-EURINR-20220329-None",
                        "report_url": None,
                        "broker_exchange": "N",
                        "type": "all",
                        "broker_exchange_type": "U",
                        "target_price": 83.2,
                        "market_cap": None,
                        "modification_date": 20220328131323,
                        "clients_placed_orders": 11,
                        "lot_size": 1000,
                        "total_order_value": 674227.2599999999,
                        "expiry": 20220329,
                        "id": "066670c4b1044f7e9d77c0bbbb0f0060",
                        "ins_type": "cash",
                        "open_price": 83.65,
                        "sector": None,
                        "strike_price": None,
                        "broker_isin": "EURINR",
                        "required_margin": 1992.28,
                        "stoploss_price": 83.91,
                        "entry_price": {
                            "from": 83.64,
                            "to": 83.68
                        },
                        "group_name": "iifl",
                        "strike": None,
                        "groups": None,
                        "creation_date": 20220328131323,
                        "history": None,
                        "broker": "iifl",
                        "version": 0,
                        "tags": {},
                        "closed_price": None,
                        "market": "Equity",
                        "horizon": "short_term",
                        "employee_email": "gupta.anuj@iifl.com",
                        "expire_date": None,
                        "full_name": "EURINR • 29 Mar 2022 • FUT",
                        "topic": "95d24dbbec0d41af921487c0992186fc",
                        "exchange": "nse",
                        "validity": 20220328,
                        "remarks": "",
                        "transaction": "BUY"
                    }
                },
                "unique_identifier": "iifl-currency-fut-EURINR-20220329-None",
                "closed_date": 20220329090639,
                "total_order_value": 0,
                "ins_type": "cash",
                "employee_email": "gupta.anuj@iifl.com",
                "stoploss_price": 83.91,
                "tags": {},
                "group_name": "iifl",
                "clients_placed_orders": 0,
                "version": 1,
                "broker_exchange_type": "U",
                "symbol": "EURINR",
                "closed_by": "stoploss",
                "modification_date": 20220328164937,
                "is_modified": True,
                "required_margin": 1992.28,
                "creation_date": 20220328131323,
                "transaction": "BUY",
                "broker_code": 1762,
                "horizon": "intraday",
                "open_price": 83.65,
                "broker_exchange": "N",
                "exchange": "nse",
                "expiry": 20220329,
                "remarks": "",
                "closed_price": 83.5525,
                "validity": 20220329,
                "type": "all"

            },
    }

a = EditJson(event)
payload_time = a.payload_time()
payload_time['where']['event_name']='op_Sell Completed'
payload_time['content']["title"] = 'sl triggered on'
payload_time['content']['body'] = "triggered stoploss"
payload_time['content']['platform_specific']['android']['deep_link'] = "iiflmarketsapp://gems?GEMSOLOID=84eba3adbf7240798c621ad41ba5e3c6"
payload_time['content']['platform_specific']['android']['wzrk_acts']= [{'l': 'Trade Now', 'dl': 'iiflmarketsapp://sellpage?SM=EURINR&SC=1762&EX=N&EXT=U', 'id': '1'}]
payload_time['content']['platform_specific']['android']['Cat']= "BUY"


class Test_open_status(unittest.TestCase):

    def test_body(self):
        a = EditJson(event)
        print("data: ",a.body())
        print(payload_time)
        self.assertEqual(a.body(), payload_time)


if __name__ == '__main__':
    unittest.main()



