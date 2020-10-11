from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

from datetime import datetime


class TimeDiff(BaseOperator):

    @apply_defaults
    def __init__(
            self,
            diff_date: str,
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.diff_date = diff_date

    def execute(self, context):
        start_date = datetime.today()
        diff = (self.diff_date - start_date).days
        return abs(diff)
