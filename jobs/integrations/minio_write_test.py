import os

from pyspark.sql import SparkSession


APP_NAME = "atlas-minio-write-test"


def main() -> None:
    spark = (
        SparkSession.builder
        .appName(APP_NAME)
        .master("spark://spark-master:7077")
        .getOrCreate()
    )

    try:
        hadoop_conf = spark.sparkContext._jsc.hadoopConfiguration()

        hadoop_conf.set(
            "fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem"
        )

        hadoop_conf.set(
            "fs.s3a.endpoint",
            "http://minio:9000"
        )

        hadoop_conf.set(
            "fs.s3a.access.key",
            os.getenv("MINIO_ROOT_USER")
        )

        hadoop_conf.set(
            "fs.s3a.secret.key",
            os.getenv("MINIO_ROOT_PASSWORD")
        )

        hadoop_conf.set(
            "fs.s3a.path.style.access",
            "true"
        )

        hadoop_conf.set(
            "fs.s3a.connection.ssl.enabled",
            "false"
        )

        df = spark.createDataFrame(
            [
                (1, "atlas"),
                (2, "spark"),
                (3, "minio")
            ],
            ["id", "tecnologia"]
        )

        target_path = "s3a://atlas-lake/bronze/teste/"

        print(f"Escrevendo em: {target_path}")

        (
            df.write
            .mode("overwrite")
            .parquet(target_path)
        )

        print("Escrita concluída com sucesso.")

    finally:
        spark.stop()


if __name__ == "__main__":
    main()