from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://postgres:Mark1147%40@127.0.0.1:5432/Hacking"
)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print(result.fetchone())
        print("SQLALCHEMY CONNECTED")
except Exception as e:
    print(repr(e))