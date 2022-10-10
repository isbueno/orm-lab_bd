from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

URL = "mysql+mysqlconnector://root:password@localhost:3306/orm_bd"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id_pessoa = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)


def main():
    engine = create_engine(url=URL)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        pessoa = Pessoa(nome="John Snow")
        id_pessoa = pessoa.id_pessoa
        session.add(pessoa)

    with Session.begin() as session:
        pessoa.nome = "John Snow Two"
        id_pessoa = pessoa.id_pessoa
        session.add(pessoa)

    with Session.begin() as session:
        pessoa.nome = input()
        id_pessoa = pessoa.id_pessoa
        session.add(pessoa)


if __name__ == "__main__":
    main()
