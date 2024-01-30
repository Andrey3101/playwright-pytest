import psycopg2
from datetime import datetime


class ProcessingSql:

    def __init__(self, conn_string):
        self.cont_string = conn_string

    def get_client(self, number):
        try:
            conn = psycopg2.connect(self.cont_string)
        except:
            print("I am unable to connect to the processing database")
        cur = conn.cursor()
        req = "select id from processing.client where msisdn = {0}".format(number)
        cur.execute(req)
        rows = cur.fetchall()
        return rows

    def update_client(self, number):
        try:
            conn = psycopg2.connect(self.cont_string)
            cur = conn.cursor()
        except:
            print("I am unable to connect to the processing database")
        h_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.000")
        req = "UPDATE processing.client_confirmation SET confirmed = true, h_date = %s WHERE msisdn = %s"
        cur.execute(req, (h_date, number))
        conn.commit()
        cur.close()
        conn.close()

    def client_confirmation(self, client_id):
        try:
            conn = psycopg2.connect(self.cont_string)
        except:
            print("I am unable to connect to the processing database")
        cur = conn.cursor()
        req = "select try_count, resend_try_count, confirmed, enabled from processing.client_confirmation where client_id = {0} order by c_date desc".format(client_id)
        cur.execute(req)
        rows = cur.fetchall()
        return rows[0]