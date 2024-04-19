from datetime import datetime
import datetime
import requests
import json
from pydantic import BaseModel, Field
from langchain_community.tools import BaseTool
from typing import Optional, Type
import pytz


def get_day_of_week():
    london_tz = pytz.timezone('Europe/London')
    current_date_time = datetime.datetime.now(tz=london_tz)
    return current_date_time.strftime("%A")

class GetDayOfWeekInput(BaseModel):
    """Input to get the day of the week"""

class GetDayOfWeekTool(BaseTool):
    name = "get_day_of_week"
    description = "Get current day of the week (London)."

    def _run(self):
        day_of_the_week = get_day_of_week()
        return day_of_the_week

    def _arun(self):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = GetDayOfWeekInput

