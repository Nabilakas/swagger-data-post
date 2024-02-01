import os
from airflow import DAG
from datetime import timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from airflow.utils.dates import days_ago

import swagger_post as util

doc="""Swagger Post"""
default_args = {
    'owner': 'Gulraiz',
    'depends_on_past': True,
    'start_date': days_ago(2),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG('swagger_data_post', 
          default_args=default_args, 
          schedule_interval='0 2 * * *',
          catchup=False,
) 
   
current_dir = os.path.dirname(__file__) 
dag.__doc__=doc


# def send_success_email(context):
#     """
#     Function to send email on successful DAG execution
#     """
#     subject = "Airflow DAG Execution Succeeded: swagger_post"
#     body = "Your DAG 'swagger_post' has successfully completed."
#     # Add more recipients if needed
#     recipients = ['developer.gulraiz@gmail.com','gulraiz0777770@gmail.com','gulraiz@dotlabs.ai','nouman@dotlabs.ai']
#     email_task = EmailOperator(
#         task_id='send_success_email',
#         to=recipients,
#         subject=subject,
#         html_content=body,
#     )
#     return email_task.execute(context=context)

# def send_failure_email(context):
#     """
#     Function to send email in case of DAG failure
#     """
#     subject = "Airflow DAG Execution Failed: swagger_post"
#     body = "Your DAG 'swagger_post' has failed. Please take necessary actions."
#     # Add more recipients if needed
#     recipients = ['developer.gulraiz@gmail.com','gulraiz0777770@gmail.com','gulraiz@dotlabs.ai','nouman@dotlabs.ai']
#     email_task = EmailOperator(
#         task_id='send_failure_email',
#         to=recipients,
#         subject=subject,
#         html_content=body,
#     )
#     return email_task.execute(context=context)


# etl_task = PythonOperator(
#     task_id='run_etl',
#     provide_context=True,
#     python_callable=dev_etl,
#     op_kwargs={},
#     on_success_callback=send_success_email,  # Adding email on success
#     on_failure_callback=send_failure_email,  # Adding email on failure
#     dag=dag
# )

etl_task = PythonOperator(
    task_id='run_etl',
    provide_context=True,
    python_callable=util.dev_etl,
    dag=dag
)




