FROM apache/airflow:2.8.1

USER root
RUN apt-get update && apt-get install -y vim

# Copy the Python scripts and requirements file
COPY requirements.txt /requirements.txt
COPY scripts /opt/airflow/scripts

USER airflow

# Install the required libraries
RUN pip install --no-cache-dir -r /requirements.txt

