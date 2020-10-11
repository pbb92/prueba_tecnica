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

n = 5
task_n = []
for x in range(n):
    t = DummyOperator(
        task_id="task_{}".format(x+1),
        dag=test
    )
    task_n.append(t)

for task_odd in task_n[0::2]:
    for task_even in task_n[1::2]:
        task_odd >> task_even
