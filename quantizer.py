from decimal import Decimal

DECIMAL_ZERO_2DP = Decimal('0.00')
DECIMAL_ZERO_8DP = Decimal('0.00000000')
DECIMAL_ZERO_10DP = Decimal('0.0000000000')


def quantize(value, dp: int=DECIMAL_ZERO_10DP):
    value = Decimal(value)
    if dp in (DECIMAL_ZERO_2DP, DECIMAL_ZERO_8DP, DECIMAL_ZERO_10DP,):
        return value.quantize(dp)
    elif isinstance(dp, int) and dp <= 10:
        return Decimal(f"0.{'0' * dp}")


def quantize_two(value):
    if not value:
        return DECIMAL_ZERO_2DP
    value = Decimal(value)
    value = value.quantize(DECIMAL_ZERO_2DP)
    return value


def quantize_eight(value):
    if not value:
        # Will match 0 as well as False and None
        return DECIMAL_ZERO_8DP
    value = Decimal(value)
    value = value.quantize(DECIMAL_ZERO_8DP)
    return value


def quantize_ten(value):
    if not value:
        return DECIMAL_ZERO_10DP
    value = Decimal(value)
    value = value.quantize(DECIMAL_ZERO_10DP)
    return value
