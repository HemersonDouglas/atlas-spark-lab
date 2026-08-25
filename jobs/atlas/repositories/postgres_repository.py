import os

from pyspark.sql import DataFrame, SparkSession


class PostgreSQLRepository:

    def __init__(self, spark: SparkSession, config: dict):
        self.spark = spark
        self.config = config["postgres"]

    def read(self, table_name: str) -> DataFrame:
        jdbc_url = (
            f"jdbc:postgresql://"
            f"{self.config['host']}:"
            f"{self.config['port']}/"
            f"{os.getenv('POSTGRES_DB')}"
        )

        df = (
            self.spark.read
            .format("jdbc")
            .option("url", jdbc_url)
            .option("dbtable", table_name)
            .option("user", os.getenv("POSTGRES_USER"))
            .option("password", os.getenv("POSTGRES_PASSWORD"))
            .option("driver", self.config["driver"])
            .load()
        )

        return df