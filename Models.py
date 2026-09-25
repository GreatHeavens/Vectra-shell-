from typing import List, Optional
from pydantic import BaseModel, Field

# --- Hand-off 1: Ingestion Output (Person 2 -> Person 3 & 4) ---
class FunctionMetadata(BaseModel):
    name: str
    start_line: int
    end_line: int
    calls: List[str] = []
    parameters: List[str] = []

class CodeMetadata(BaseModel):
    scan_id: str
    file_path: str
    language: str
    dependencies: List[str] = []
    functions: List[FunctionMetadata] = []

# --- Hand-off 2: Threat Intelligence Output (Person 3 -> Person 4) ---
class VulnerabilityMatch(BaseModel):
    cve_id: str
    cwe_id: str
    severity: str
    cvss_score: float
    summary: str

class ThreatIntelReport(BaseModel):
    scan_id: str
    matched_vulnerabilities: List[VulnerabilityMatch] = []

# --- Hand-off 3: Final AI Security Finding (Person 4 -> Person 5) ---
class SecurityFinding(BaseModel):
    scan_id: str
    rule_id: str
    severity: str  # e.g., "CRITICAL", "HIGH", "MEDIUM"
    confidence: str  # e.g., "HIGH", "LOW"
    reachability: str  # "REACHABLE" or "UNREACHABLE"
    title: str
    description: str
    file_path: str
    line_number: int
    remediation: str
