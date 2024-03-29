import dataclasses


@dataclasses.dataclass
class Company:
    name: str
    count_active_card: str
    count_members: str
    count_released_card_today: str
    cashback: str
    decline_rate_for_last_month: str
    sum_payments_for_30_days: str
    dr_7: str
    dr_30: str
