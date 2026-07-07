"""
customer-satisfaction-survey-skill: Client SDK
Groups raw feedback ratings to evaluate customer health and product CSAT metrics.
"""
from __future__ import annotations
from typing import Optional


class CustomerSatisfactionSurveyClient:
    """
    SDK for NPS analytics.
    """

    def calculate_nps(self, scores: list[int]) -> dict:
        total = len(scores)
        if total == 0:
            return {"nps_score": 0, "percentage_promoters": 0.0, "percentage_detractors": 0.0}

        promoters = sum(1 for s in scores if s >= 9)
        detractors = sum(1 for s in scores if s <= 6)
        passives = total - promoters - detractors

        prom_pct = (promoters / total) * 100
        detr_pct = (detractors / total) * 100

        nps = int(round(prom_pct - detr_pct))

        return {
            "nps_score": nps,
            "percentage_promoters": round(prom_pct, 1),
            "percentage_detractors": round(detr_pct, 1),
            "percentage_passives": round((passives / total) * 100, 1),
            "total_responses": total,
        }
