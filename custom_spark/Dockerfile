
FROM bitnami/spark:3.3

USER root

# Create jars directory and copy JDBC driver
RUN mkdir -p /opt/spark/jars
COPY postgresql-42.2.5.jar /opt/spark/jars/postgresql-42.2.5.jar

# Set Ivy cache to avoid basedir error
ENV SPARK_SUBMIT_OPTS="-Divy.cache.dir=/tmp -Divy.home=/tmp"

USER 1001
