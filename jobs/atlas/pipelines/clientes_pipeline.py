from pyspark.sql import DataFrame

from repositories.postgres_repository import PostgreSQLRepository


class ClientesPipeline:

    TABLE_NAME = "public.clientes"

    def __init__(self, repository: PostgreSQLRepository):
        self.repository = repository

    def extract(self) -> DataFrame:
        df = self.repository.read(self.TABLE_NAME)

        return df

    def run(self) -> None:
        df = self.extract()

        print("\n===== SCHEMA =====")
        df.printSchema()

        print("\n===== DADOS =====")
        df.show(truncate=False)

        print(f"\nTotal de registros: {df.count()}")