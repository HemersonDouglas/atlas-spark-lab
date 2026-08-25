from pyspark.sql import SparkSession

class SparkSessionFactory:

    @staticmethod
    def create(config: dict) -> SparkSession:
        spark_config = config["spark"]

        spark = (
        SparkSession.builder
        .appName(spark_config["app_name"])
        .getOrCreate()
    )

        return spark    