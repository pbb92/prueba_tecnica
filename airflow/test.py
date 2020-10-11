from datetime import datetime, timedelta

import airflow
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

test = DAG(
    dag_id='test',
    default_args=default_args,
    schedule_interval='0 3 * * *',
)


t1 = DummyOperator(
    task_id='start',
    dag=test
)

t2 = DummyOperator(
    task_id='end',
    dag=test
)

t1 >> t2