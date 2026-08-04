from pyspark.sql import SparkSession

print("====================================")
print("Atlas Spark Lab")
print("Smoke Test iniciado...")
print("====================================")

spark = (
    SparkSession.builder
    .appName("atlas-smoke-test")
    .master("spark://spark-master:7077")
    .getOrCreate()
)

df = spark.range(1000000)

total_1 = df.count()

print(f"Total de registros: {total_1}")

spark.stop()

print("====================================")
print("Smoke Test finalizado com sucesso!")
print("====================================")