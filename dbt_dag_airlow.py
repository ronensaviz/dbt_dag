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
    'docker_dbt_workflow',
    default_args=default_args,
    description='A DAG to build and run a Docker container for DBT',
    schedule_interval=timedelta(days=1),
)

# Define the SSH and Docker commands
ssh_command = """
ssh -o StrictHostKeyChecking=no -i /opt/airflow/ssh_key omid@34.122.66.108 << EOF
cd /home/omid/google_analytics_4
docker build -t my-dbt-image .
docker rm -f my-dbt-container || true
docker run --name my-dbt-container my-dbt-image
EOF
"""

# Define the task
docker_dbt_task = BashOperator(
    task_id='docker_dbt_workflow_task',
    bash_command=ssh_command,
    dag=dag,
)

# Set the task in the DAG
docker_dbt_task
