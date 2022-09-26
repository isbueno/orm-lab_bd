from sqlachemy import create_engine, inspect


URL = "mysql+mysqlconnector://root:polimataIFSP.email23@localhost"


def main():
    engine = create_engine(url=URL)

    print("Database List Using SQLAlchemy")
    print("+++++++++++++++++++++++++++++++")
    insp = inspect(engine)
    db_list = insp.get_schema_names()
    print(db_list)

    print("Database List Using SHOW DATABASES command")
    print("+++++++++++++++++++++++++++++++")

    with engine.connect() as connection:
        result_set = connection.execute("SHOW DATABASES")
        for row in result_set:
            print(row[0])

    print("\nTable List in the World Database")
    print("+++++++++++++++++++++++++++++++")

    with engine.connect() as connection:
        connection.execute("USE WORLD;")
        result_set = connection.execute("SHOW TABLES")
        for row in result_set:
            print(row[0])

        print('\n\n')
        print(result_set)


if __name__ == "__main__":
    main()
