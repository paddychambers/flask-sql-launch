from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:HruewmqYXONlznzmaggmlmsjsSqbVLgz@shortline.proxy.rlwy.net:48246/railway",
        connect_args={"ssl": {"ssl_ca": "skysql_chain.pem"}})

with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM spendings"))
      rows = result.mappings().all()
      print(rows)