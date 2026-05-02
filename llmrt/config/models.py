from pydantic import BaseModel
from datetime import datetime

class Finding(BaseModel):
    payload: str
    success: bool
    response: str
    model: str
    attack_type: str
    owasp_id: str
    severity: str
    attempts: int = 0

class ScanResult(BaseModel):
    list_of_findings: list[Finding]
    scan_time: datetime
    model: str
    total_findings: int
    total_passed: int
    total_failed: int
    risk_score: float