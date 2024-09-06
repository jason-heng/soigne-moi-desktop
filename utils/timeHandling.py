from datetime import datetime, timezone
from tzlocal import get_localzone

def to_local_datetime(date_time):
    # Convert to timezone-aware datetime
    local_tz = get_localzone()
    time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%fZ")
    time = time.replace(tzinfo=timezone.utc)
    
    # Convert UTC time to the local timezone
    local_time = time.astimezone(local_tz)
    
    return local_time.date()
