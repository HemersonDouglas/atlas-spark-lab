
from config.settings import APP_CONFIG
from core.spark_session import SparkSessionFactory
from repositories.postgres_repository import PostgreSQLRepository
from pipelines.clientes_pipeline import ClientesPipeline


def main() -> None:
    spark = SparkSessionFactory.create(APP_CONFIG)

    try:
        repository = PostgreSQLRepository(spark, APP_CONFIG)

        pipeline = ClientesPipeline(repository)

        pipeline.run()

    finally:
        spark.stop()


if __name__ == "__main__":
    main()