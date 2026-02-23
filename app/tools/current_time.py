from langchain.tools import tool
from datetime import datetime
from zoneinfo import ZoneInfo  # built-in in Python 3.9+

@tool
def current_time(query: str) -> str:
    """
    Returns the current local time in a given city or timezone.
    Example input: "Asia/Karachi" or "UTC"
    """
    try:
        tz = ZoneInfo(query)
    except Exception:
        tz = ZoneInfo("UTC")  # fallback to UTC if invalid timezone
    now = datetime.now(tz)
    return f"The current time in {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z')}"