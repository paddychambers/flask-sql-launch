from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://dbpgf12437636:ZR)ciRAnv]S62yF0mM9r5N@serverless-us-east4.sysp0000.db2.skysql.com/paddy-chambers-llsg?charset=utf8mb4",
        connect_args={"ssl": {"ssl_ca": "skysql_chain.pem"}})

try:
  with engine.connect() as conn:
      result = conn.execute(text("SELECT 1"))
      print("Connection OK:", result.scalar())
except Exception as e:
  print("Connection failed:", e)