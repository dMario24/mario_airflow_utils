import sys
import mario_airflow_utils


def test_ping():
    sys.argv = ['foo', '10']
    mario_airflow_utils.ping()

