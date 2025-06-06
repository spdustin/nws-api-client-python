"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from datetime import datetime
import sys


def parse_datetime(datetime_string: str) -> datetime:
    """
    Convert a RFC 3339 / ISO 8601 formatted string into a datetime object.
    Python versions 3.11 and later support parsing RFC 3339 directly with
    datetime.fromisoformat(), but for earlier versions, this function
    encapsulates the necessary extra logic.
    """
    # Python 3.11 and later can parse RFC 3339 directly
    if sys.version_info >= (3, 11):
        return datetime.fromisoformat(datetime_string)
    
    # For Python 3.10 and earlier, a common ValueError is trailing 'Z' suffix,
    # so fix that upfront.
    if datetime_string.endswith("Z"):
        datetime_string = datetime_string[:-1] + "+00:00"

    return datetime.fromisoformat(datetime_string)
