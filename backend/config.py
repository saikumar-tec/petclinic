from sqlalchemy.engine import URL

SQLALCHEMY_DATABASE_URI = URL.create(
    "mssql+pyodbc",
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_SERVER,
    port=int(DB_PORT),
    database=DB_NAME,
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes",
    },
)