import os

from pyspark.sql import SparkSession


APP_NAME = "atlas-postgres-read"


def main() -> None:
    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .master("spark://spark-master:7077")
        .getOrCreate()
    )

    try:
        jdbc_url = (
            f"jdbc:postgresql://postgres:5432/"
            f"{os.getenv('POSTGRES_DB')}"
        )

        df = (
            spark.read
            .format("jdbc")
            .option("url", jdbc_url)
            .option("dbtable", "public.clientes")
            .option("user", os.getenv("POSTGRES_USER"))
            .option("password", os.getenv("POSTGRES_PASSWORD"))
            .option("driver", "org.postgresql.Driver")
            .load()
        )

        print("\n===== SCHEMA =====")
        df.printSchema()

        print("\n===== DADOS =====")
        df.show(truncate=False)

        print(f"\nTotal de registros: {df.count()}")

    finally:
        spark.stop()


