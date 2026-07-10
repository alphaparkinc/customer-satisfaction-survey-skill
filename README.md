# genpark-customer-satisfaction-survey-skill

> **GenPark AI Agent Skill** -- Net Promoter Score (NPS) metrics dashboard.

## Quick Start

```python
from client import CustomerSatisfactionSurveyClient
client = CustomerSatisfactionSurveyClient()
res = client.calculate_nps([10, 10, 10, 2])
print(res["nps_score"])
```
