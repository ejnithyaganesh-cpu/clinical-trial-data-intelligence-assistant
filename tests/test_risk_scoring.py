import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

import pandas as pd

from src.risk_scoring import RiskScoring


sample_data = pd.DataFrame({
    "trial_id": [
        "CT-001",
        "CT-002",
        "CT-003"
    ],
    "adverse_event_count": [
        50,
        85,
        120
    ]
})

risk = RiskScoring()

result = risk.calculate_trial_risk(
    sample_data
)

print(result)