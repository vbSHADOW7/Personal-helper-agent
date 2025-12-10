from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict


def get_utc_time() -> Dict[str, str]:

    now = datetime.now(timezone.utc)
    return {
        "utc_iso": now.isoformat(),
        "date": now.date().isoformat(),
        "time": now.time().strftime("%H:%M:%S"),
    }
