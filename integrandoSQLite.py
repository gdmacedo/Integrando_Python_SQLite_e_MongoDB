from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column, create_engine, inspect, select, func, Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    Nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    contas = relationship(
    "Conta", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, name={self.Nome}, cpf={self.cpf}, endereco={self.endereco}"

class Conta(Base):
    __tablename__ = "contas"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    saldo = Column(Float)
    id_cliente = Column(Integer, ForeignKey("clientes.id"), nullable=True)

    user = relationship("Cliente", back_populates="contas")

    def __repr__(self):
        return f"id={self.id}, tipo={self.tipo}, agencia={self.agencia}, numero={self.num}, saldo={self.saldo}"

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelaas no banco de dados
Base.metadata.create_all(engine)

# depreciado - será removido em futuros release
# print(engine.table_names())

inspector_engine = inspect(engine)
print(inspector_engine.has_table("contas"))
print(inspector_engine.get_table_names())
print(inspector_engine.default_schema_name)

with Session(engine) as session:
    Isabel = Cliente(
        Nome= "Isabel",
        cpf= "12345854589",
        endereco= "São José do Rio Preto",
        contas=[Conta(tipo="Corrente", agencia= "dadada", num=32, saldo=444)]
    )

    Lia = Cliente(
        Nome="Eliana",
        cpf="123456789",
        endereco="sorocaba",
        contas=[Conta(tipo="Poupança", agencia="tada", num=48, saldo=150)]
    )
    Ana = Cliente(
        Nome="AnaLúcia",
        cpf="4152637895",
        endereco="Vila Olimpia",
        contas=[Conta(tipo="Corrente", agencia="taad", num=13, saldo=900)]
    )
    session.add_all([Isabel, Lia, Ana])

    session.commit()

order_stmt = select(Cliente).order_by(Cliente.Nome.desc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(order_stmt):
    print(result)

stmt_count = select(func.count('*')).select_from(Cliente)
print('\nTotal de instâncias em User')
for result in session.scalars(stmt_count):
    print(result)
