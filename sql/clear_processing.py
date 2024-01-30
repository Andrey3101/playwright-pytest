import psycopg2


class ClearProcessing:

    def __init__(self, conn_string):
        self.cont_string = conn_string

    def clear_client(self, phone):
        try:
            conn = psycopg2.connect(self.cont_string)
            cur = conn.cursor()
            req = """
            DO $$ 
            DECLARE 
                v_msisdn bigint = %s;
            BEGIN 
                DELETE FROM processing.esia_request WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn);
                DELETE FROM processing.smev_request WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn);
                DELETE FROM processing.client_token WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn);
                DELETE FROM processing.client_notification_type WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn);
                UPDATE processing.invoice SET payment_tool_id = NULL WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn);
                DELETE FROM processing.transaction_receipt_item WHERE transaction_receipt_id IN (SELECT id FROM processing.transaction_receipt WHERE transaction_id IN (SELECT id FROM processing.transaction WHERE payment_id IN (SELECT id FROM processing.payment WHERE invoice_id IN (SELECT id FROM processing.invoice WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn)))));
                DELETE FROM processing.transaction_receipt WHERE transaction_id IN (SELECT id FROM processing.transaction WHERE payment_id IN (SELECT id FROM processing.payment WHERE invoice_id IN (SELECT id FROM processing.invoice WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn))));
                DELETE FROM processing.transaction WHERE payment_id IN (SELECT id FROM processing.payment WHERE invoice_id IN (SELECT id FROM processing.invoice WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn)));
                DELETE FROM processing.payment WHERE invoice_id IN (SELECT id FROM processing.invoice WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn));
                DELETE FROM processing.payment_tool WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn);
                DELETE FROM processing.invoice WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn);
                DELETE FROM processing.sms WHERE client_confirmation_id IN (SELECT id FROM processing.client_confirmation WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn));
                DELETE FROM processing.client_confirmation WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn);
                DELETE FROM processing.client_session WHERE client_id IN (SELECT id FROM processing.client WHERE msisdn = v_msisdn);
                DELETE FROM processing.client WHERE msisdn = v_msisdn;
            END; 
            $$;
            """
            cur.execute(req, (phone,))
            conn.commit()
        except psycopg2.Error as e:
            print("I am unable to connect to the processing database:", e)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()