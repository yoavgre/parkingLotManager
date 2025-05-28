from datetime import datetime, timedelta

COST_PER_HOUR = 10

def calculate_fee(entry_time: datetime, exit_time: datetime):
    duration = exit_time - entry_time
    minutes = duration.total_seconds() / 60
    increments = -(-minutes // 15)  # Ceiling division
    fee = (increments / 4) * COST_PER_HOUR  # $10/hour, prorated per 15 min
    return duration, fee
