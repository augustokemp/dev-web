from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import QueuePool

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    poolclass=QueuePool,
    pool_pre_ping=True,
    connect_args={"options": "-c timezone=gmt+3"},
    pool_size=100,
    max_overflow=20,
    pool_timeout=10,
    pool_recycle=1800,  # 30 minutes
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def execute_query(db: Session, query: str):
    cursor = db.execute(query)
    if 'RETURNING' in query.upper():
        db.commit()
    result = cursor.fetchall()

    resultados = []
    for rowproxy in result:
        d = {}
        for column, value in rowproxy._asdict().items():
            d = {**d, **{column: value}}

        resultados.append(d)
    cursor.close()
    return resultados


def execute_query_indexed(db: Session, query: str):
    """
        Executa a query e retorna um dicionario indexado pelo primeiro campo da query
    """
    cursor = db.execute(query)
    key = list(cursor.keys())[0]
    result = cursor.fetchall()

    resultados = {}
    for rowproxy in result:
        row_dict = rowproxy._asdict()

        if not resultados.get(row_dict[key]):
            resultados[row_dict[key]] = []

        resultados[row_dict[key]].append(row_dict)

    cursor.close()
    return resultados


def execute_sql(db: Session, query: str):
    """
    Executa uma query sem retorno de resultados.
    """
    cursor = db.execute(query)
    db.commit()
    cursor.close()
    return True
