# useful tips that do not focus on a specific dataset
# We’ll use generic filenames like large_dataset.csv in the code examples

# Consider PySpark for Big Data Processing

from pyspark.sql import SparkSession

# Start a Spark session
spark = SparkSession.builder.appName("MovieRatings").getOrCreate()

# Load the dataset into a Spark DataFrame
df = spark.read.csv('movie_ratings.csv', header=True, inferSchema=True)

# Perform transformations (e.g., group by genre and calculate average rating)
df_grouped = df.groupBy('genre').mean('rating')

# Show the result
df_grouped.show()
