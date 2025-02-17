from dataclasses import dataclass
from typing import Optional, List, Dict
from .aggs import Agg
from .quotes import LastQuote
from .trades import LastTrade


@dataclass
class SnapshotMin:
    "Most recent minute bar."
    accumulated_volume: Optional[float] = None
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    close: Optional[float] = None
    volume: Optional[float] = None
    vwap: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return SnapshotMin(
            d.get("av", None),
            d.get("o", None),
            d.get("h", None),
            d.get("l", None),
            d.get("c", None),
            d.get("v", None),
            d.get("vw", None),
        )


@dataclass
class Snapshot:
    "Contains the most up-to-date market data for all traded ticker symbols."
    day: Optional[Agg] = None
    last_quote: Optional[LastQuote] = None
    last_trade: Optional[LastTrade] = None
    min: Optional[SnapshotMin] = None
    prev_day: Optional[Agg] = None
    ticker: Optional[str] = None
    todays_change: Optional[float] = None
    todays_change_percent: Optional[float] = None
    updated: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return Snapshot(
            day=None if "day" not in d else [Agg.from_dict(d["day"])],
            last_quote=None
            if "last_quote" not in d
            else [LastQuote.from_dict(d["last_quote"])],
            last_trade=None
            if "last_trade" not in d
            else [LastTrade.from_dict(d["last_trade"])],
            min=None if "min" not in d else [SnapshotMin.from_dict(d["min"])],
            prev_day=None if "prev_day" not in d else [Agg.from_dict(d["prev_day"])],
            ticker=d.get("ticker", None),
            todays_change=d.get("todays_change", None),
            todays_change_percent=d.get("todays_change_percent", None),
            updated=d.get("updated", None),
        )


@dataclass
class DayOptionContractSnapshot:
    "Contains data for the most recent daily bar in an options contract."
    change: Optional[float] = None
    change_percent: Optional[float] = None
    close: Optional[float] = None
    high: Optional[float] = None
    last_updated: Optional[int] = None
    low: Optional[float] = None
    open: Optional[float] = None
    previous_close: Optional[float] = None
    volume: Optional[float] = None
    vwap: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return DayOptionContractSnapshot(**d)


@dataclass
class OptionDetails:
    "Contains details for an options contract."
    contract_type: Optional[str] = None
    exercise_style: Optional[str] = None
    expiration_date: Optional[str] = None
    shares_per_contract: Optional[float] = None
    strike_price: Optional[float] = None
    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OptionDetails(**d)


@dataclass
class OptionLastQuote:
    "Contains data for the most recent quote in an options contract."
    ask: Optional[float] = None
    ask_size: Optional[float] = None
    bid: Optional[float] = None
    bid_size: Optional[float] = None
    last_updated: Optional[int] = None
    midpoint: Optional[float] = None
    timeframe: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OptionLastQuote(**d)


@dataclass
class OptionGreeks:
    "Contains data for the greeks in an options contract."
    delta: Optional[float] = None
    gamma: Optional[float] = None
    theta: Optional[float] = None
    vega: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return OptionGreeks(**d)


@dataclass
class UnderlyingAsset:
    "Contains data for the underlying stock in an options contract."
    change_to_break_even: Optional[float] = None
    last_updated: Optional[int] = None
    price: Optional[float] = None
    ticker: Optional[str] = None
    timeframe: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return UnderlyingAsset(**d)


@dataclass
class OptionContractSnapshot:
    "Contains data for the snapshot of an option contract of a stock equity."
    break_even_price: Optional[float] = None
    day: Optional[DayOptionContractSnapshot] = None
    details: Optional[OptionDetails] = None
    greeks: Optional[OptionGreeks] = None
    implied_volatility: Optional[float] = None
    last_quote: Optional[OptionLastQuote] = None
    open_interest: Optional[float] = None
    underlying_asset: Optional[UnderlyingAsset] = None

    @staticmethod
    def from_dict(d):
        return OptionContractSnapshot(
            break_even_price=d.get("break_even_price", None),
            day=None
            if "day" not in d
            else [DayOptionContractSnapshot.from_dict(d["day"])],
            details=None
            if "details" not in d
            else [OptionDetails.from_dict(d["details"])],
            greeks=None if "greeks" not in d else [OptionGreeks.from_dict(d["greeks"])],
            implied_volatility=d.get("implied_volatility", None),
            last_quote=None
            if "last_quote" not in d
            else [OptionLastQuote.from_dict(d["last_quote"])],
            open_interest=d.get("open_interest", None),
            underlying_asset=None
            if "underlying_asset" not in d
            else [UnderlyingAsset.from_dict(d["underlying_asset"])],
        )


@dataclass
class OrderBookQuote:
    "Contains data for a book bid or ask."
    price: Optional[float] = None
    exchange_shares: Optional[Dict[str, float]] = None

    @staticmethod
    def from_dict(d):
        return OrderBookQuote(
            d.get("p", None),
            d.get("x", None),
        )


@dataclass
class SnapshotTickerFullBook:
    "Contains the current level 2 book of a single ticker. This is the combined book from all of the exchanges."
    ticker: Optional[str] = None
    bids: Optional[List[OrderBookQuote]] = None
    asks: Optional[List[OrderBookQuote]] = None
    bid_count: Optional[float] = None
    ask_count: Optional[float] = None
    spread: Optional[float] = None
    updated: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return SnapshotTickerFullBook(
            ticker=d.get("ticker", None),
            bids=None
            if "bids" not in d
            else [OrderBookQuote.from_dict(o) for o in d["bids"]],
            asks=None
            if "asks" not in d
            else [OrderBookQuote.from_dict(o) for o in d["asks"]],
            bid_count=d.get("bid_count", None),
            ask_count=d.get("ask_count", None),
            spread=d.get("spread", None),
            updated=d.get("updated", None),
        )
