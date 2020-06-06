"""
Test DAG for initial setup
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


def hello_world() -> None:
    """
    Print hello world
    """
    print("Hello World!")


default_args = {
    'depends_on_past': False,
    'start_date': days_ago(2),
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    schedule_interval='@once',
)

t1 = PythonOperator(
    task_id='print_task',
    python_callable=hello_world,
    dag=dag,
)

t1