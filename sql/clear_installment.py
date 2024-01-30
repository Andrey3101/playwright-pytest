import psycopg2
from datetime import datetime


class ClearInstallment:

    def __init__(self, conn_string):
        self.cont_string = conn_string

    def clear_client_installment(self, phone):
        try:
            conn = psycopg2.connect(self.cont_string)
            cur = conn.cursor()
            req = """DO $$
                DECLARE 
                    v_msisdn bigint = %s;
                BEGIN 
                    DELETE FROM installment.funding_operation WHERE installment_id IN (SELECT installment_id FROM installment.installment WHERE client_id IN (SELECT client_id FROM installment.client WHERE msisdn = v_msisdn));
                    DELETE FROM installment.payment WHERE installment_id IN (SELECT installment_id FROM installment.installment WHERE client_id IN (SELECT client_id FROM installment.client WHERE msisdn = v_msisdn));
                    DELETE FROM installment.installment WHERE client_id IN (SELECT client_id FROM installment.client WHERE msisdn = v_msisdn);
                    DELETE FROM installment.client WHERE msisdn = v_msisdn;
                END;
                $$;"""
            cur.execute(req, (phone,))
            conn.commit()
        except psycopg2.Error as e:
            print("I am unable to connect to the processing database:", e)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()