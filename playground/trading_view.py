from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

TOTAL_COLUMNS = 14


@dataclass(frozen=True)
class TradingViewCsvRecord:
    trade_no: int
    type: str
    comment: str
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

    @classmethod
    def from_raw_data(cls, raw_data: list[str]) -> "TradingViewCsvRecord":
        return TradingViewCsvRecord(
            trade_no=int(raw_data[0]),
            type=raw_data[1],
            comment=raw_data[2],
            time=datetime.strptime(raw_data[3], "%Y-%m-%d %H:%M"),
            price=float(raw_data[4]),
            quantity=float(raw_data[5]),
            realized_pnl=float(raw_data[6]),
            realized_pnl_in_percent=float(raw_data[7]),
            cumulative_pnl=float(raw_data[8]),
            cumulative_pnl_in_percentage=float(raw_data[9]),
            run_up=float(raw_data[10]),
            run_up_in_percentage=float(raw_data[11]),
            drawdown=float(raw_data[12]),
            drawdown_in_percentage=float(raw_data[13]),
        )


file_path = Path(
    "data/trading-view/TV-PL-Binance_ETHUSDT.P-M15-0001_List_of_Trades_2024-01-13_14c27.csv"
)


def get_trading_view_records(path: Path) -> list[TradingViewCsvRecord]:
    records: list[TradingViewCsvRecord] = []

    with open(path, encoding="utf-8") as raw_data:
        rows: list[str] = raw_data.readlines()
        _ = rows.pop(0)
        rows.reverse()

        for row in rows:
            raw_data = row.split(",")

            if raw_data[3] == "" or raw_data[5] == "":
                continue

            records.append(TradingViewCsvRecord.from_raw_data(raw_data))

    return records
