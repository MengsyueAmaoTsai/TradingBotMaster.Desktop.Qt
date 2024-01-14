from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
from trading_view import get_trading_view_records
from enum import Enum

records = get_trading_view_records(
    Path(
        "data/trading-view/TV-PL-Binance_ETHUSDT.P-M15-0001_List_of_Trades_2024-01-13_14c27.csv"
    )
)


class TradeType(Enum):
    BUY = "Buy"
    SELL = "Sell"


@dataclass(frozen=True)
class Execution:
    """ """

    time: datetime
    trade_type: TradeType
    quantity: float
    price: float


for record in records:
    trade_type = (
        TradeType.BUY if record.type in ("Entry Long", "Exit Short") else TradeType.SELL
    )

    execution = Execution(
        time=record.time,
        trade_type=trade_type,
        quantity=record.quantity,
        price=record.price,
    )

    print(execution)
