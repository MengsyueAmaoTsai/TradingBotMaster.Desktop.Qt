from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
TOTAL_COLUMNS = 14


@dataclass(frozen=True)
class TradingViewCsvRecord:
    trade_no: int
    comment: str
    type: str
    time: datetime
    price: float
    quantity: float
    realized_pnl: float
    realized_pnl_in_percent: float
    cumulative_pnl: float 
    cumulative_pnl_in_percentage: float 
    run_up: float
    run_up_in_percentage: float
    drawdown: float
    drawdown_in_percentage: float

file_path = Path("data/trading-view/TV-PL-Binance_ETHUSDT.P-M15-0001_List_of_Trades_2024-01-13_14c27.csv")

def get_trading_view_records(path: Path) -> list[TradingViewCsvRecord]:
    records: list[TradingViewCsvRecord] = []

    with open(path, mode='r', encoding="utf-8") as raw_data:
        
        rows: list[str] = raw_data.readlines()

        # Remove header
        _ = rows.pop(0)
        
        rows.reverse()

        for row in rows:
            parts = row.split(',')

            # Skip opening position record.
            if (parts[3] == "" or parts[5] == ""):
                continue
            
            trade_no = int(parts[0])
            comment = parts[1]
            type = parts[2]
            time = datetime.strptime(parts[3], "%Y-%m-%d %H:%M")
            price = float(parts[4])
            quantity = float(parts[5])
            
            realized_pnl = float(parts[6])
            realized_pnl_in_percentage = float(parts[7])
            cumulative_pnl = float(parts[8])
            cumulative_pnl_in_percentage = float(parts[9])
            run_up = float(parts[10])
            run_up_in_percentage = float(parts[11])
            drawdown = float(parts[12])
            drawdown_in_percentage = float(parts[13])

            record = TradingViewCsvRecord(
                trade_no=trade_no, 
                comment=comment, 
                type=type,
                time=time,
                price=price,
                quantity=quantity,
                realized_pnl=realized_pnl,
                realized_pnl_in_percent=realized_pnl_in_percentage,
                cumulative_pnl=cumulative_pnl,
                cumulative_pnl_in_percentage=cumulative_pnl_in_percentage,
                run_up=run_up,
                run_up_in_percentage=run_up_in_percentage,
                drawdown=drawdown,
                drawdown_in_percentage=drawdown_in_percentage)
            records.append(record)

    return records

