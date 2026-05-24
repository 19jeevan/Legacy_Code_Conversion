from pydantic import BaseModel
from typing import List


class EvaluationResult(BaseModel):
    coverage_score: float
    risk_level: str
    manual_review_items: List[str]