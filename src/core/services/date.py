import datetime
import re
from typing import Union

import dateutil.parser


def get_now():
    return datetime.datetime.now().isoformat()


def validate_date(date: Union[str, datetime.datetime]):
	if isinstance(date, datetime.datetime):
		return date

	try:            
		regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
		match_iso8601 = re.compile(regex).match
		
		if match_iso8601( date ) is not None:
			return dateutil.parser.isoparse(date)
	except:
		raise Exception('Invalid date.')
	

	# if isinstance(date, datetime.datetime):
	# 	return date

	# try:
	# 	return datetime.date.fromisoformat(date)
	# except ValueError:
	# 	raise Exception('Invalid date.')


def add_days(date: Union[str, datetime.datetime], amount: int):
	date_object = validate_date(date)

	answer = date_object + datetime.timedelta(days=amount)

	return answer.isoformat()

def sub_days(date: Union[str, datetime.datetime], amount: int):
	date_object = validate_date(date)

	answer = date_object - datetime.timedelta(days=amount)

	return answer.isoformat()


