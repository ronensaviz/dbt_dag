from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'ssh_ls_command',
    default_args=default_args,
    description='A simple DAG to run ssh ls command',
    schedule_interval=timedelta(days=1),
)

# Define the Bash command
#ssh_command = 'ssh -i /opt/airflow/ssh_key omid@34.122.66.108 "ls -la"'
ssh_command = 'ssh -o StrictHostKeyChecking=no -i /opt/airflow/ssh_key omid@34.122.66.108 "ls -la"'
#ssh_command = 'ssh -o StrictHostKeyChecking=no -i /opt/airflow/marketing/marketing omid@34.122.66.108 "ls -la"'
#ssh_command = 'ssh -vvv -i /opt/airflow/marketing omid@34.122.66.108 "ls -la"'
# Define the task
run_ssh_command = BashOperator(
    task_id='run_ssh_ls',
    bash_command=ssh_command,
    dag=dag,
)

# Set the task in the DAG
run_ssh_command
