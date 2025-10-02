from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts import ingest, preprocess, train_model, evaluate, graph

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

with DAG('mlops_end_to_end_pipeline_docker_airflow',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    t1 = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest.main
    )

    t2 = PythonOperator(
        task_id='preprocess',
        python_callable=preprocess.main
    )

    t3 = PythonOperator(
        task_id='train_model',
        python_callable=train_model.main
    )

    t4 = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate.main
    )

    t5 = PythonOperator(
        task_id='graph_model',
        python_callable=graph.main
    )

    t1 >> t2 >> t3 >> t4 >> t5