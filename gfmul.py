from block_poly.b64_block import B64Block
from block_poly.block import Block
from block_poly.poly import Poly

FIELD_SIZE = 128
REDUCTION_POLYNOM = (1 << 128) | (1 << 7) | (1 << 2) | (1 << 1) | 1


def gfmul(a_block: bytes, b_block: bytes) -> bytes:
    """Does bit multiplication, but reduces carry if it is bigger than the Reduction Polynom of gf128, so that
       the result can never be bigger than the Reduction Polynom."""
    a_poly = Block(a_block).get_poly()
    b_poly = Block(b_block).get_poly()

    if not (0 <= a_poly < (1 << FIELD_SIZE)) or not (0 <= b_poly < (1 << FIELD_SIZE)):
        raise ValueError(f"Inputs must be non-negative integers less than 2^{FIELD_SIZE}")

    result = 0
    # Normally FIELD_SIZE, but len b should work as well, because if b only has 0s nothing should happen
    for i in range(len(bin(b_poly)[2:])):
        if b_poly & (1 << i):
            result ^= a_poly

        if a_poly & (1 << (FIELD_SIZE - 1)):
            a_poly = (a_poly << 1) ^ REDUCTION_POLYNOM
        else:
            a_poly <<= 1

    if not (0 <= result < (1 << FIELD_SIZE)):
        raise ValueError(f"Result must be non-negative integers less than 2^{FIELD_SIZE}")

    return Poly(result).get_block()
