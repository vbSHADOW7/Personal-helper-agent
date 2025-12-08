from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict


def get_utc_time() -> Dict[str, str]:
    """
    Return the current time in UTC.

    Returns:
        dict: A dictionary with multiple time formats:
            - utc_iso: Full ISO8601 timestamp in UTC
            - date: YYYY-MM-DD
            - time: HH:MM:SS
    """
    now = datetime.now(timezone.utc)
    return {
        "utc_iso": now.isoformat(),
        "date": now.date().isoformat(),
        "time": now.time().strftime("%H:%M:%S"),
    }
