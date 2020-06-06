"""
Testing for all DAGs
"""
import os

from airflow.models import DagBag


TEST_FOLDER = 'tests'
DAGS_FOLDER = 'dags'
# Total number of sample DAGs loaded into DagBag by default
DEFAULT_DAG_COUNT = 23


def test_dags_import():
    """
    Are all DAGs successfully imported
    Override DAG folder to point to airflow_dags/dags/
    """
    current_dir = os.getcwd()
    override_dag_dir = current_dir.replace(
        TEST_FOLDER,
        DAGS_FOLDER
    )
    dags = DagBag(dag_folder=override_dag_dir)
    # Confirm that we are not simply looking at default DAGs
    assert dags.size() > DEFAULT_DAG_COUNT
    assert len(dags.import_errors) == 0