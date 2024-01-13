from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class TradingViewCsvRecord:
    sequence_number: int
    comment: str
    type: str
    time: datetime
    price: float
    quantity: float
    profit: float
    profit_in_percent: float
    cumulative_profit: float 



TOTAL_COLUMNS = 14

file = "data/trading-view/TV-PL-Binance_ETHUSDT.P-M15-0001_List_of_Trades_2024-01-13_14c27.csv"

trade_raw_data = []

with open(file, mode='r', encoding="utf-8") as raw_data:
    rows: list[str] = raw_data.readlines()
    
    for row in rows:
        parts = row.split(',')
        
        if len(parts) != TOTAL_COLUMNS:
            continue

        if (parts[-1].isspace()):
            continue    
                    
        trade_raw_data.append(row)

if trade_raw_data:
    trade_raw_data.reverse()
    trade_raw_data.pop()
    
for trade in trade_raw_data:
    print(trade)


    