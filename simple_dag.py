from airflow import DAG
from airflow.operators.python import PythonOperator


with DAG("my_dag", # Dag id
start_date=datetime(2021, 1 ,1), # start date, the 1st of January 2021 
schedule_interval='@daily',  # Cron expression, here it is a preset of Airflow, @daily means once every day.
catchup=False  # Catchup 
) as dag:

test_task = PythonOperator(
task_id = "test_task",
python_callable = print("hello")

)