from block_poly.base import Base
import base64


class Coefficients(Base):
    """Takes in Coefficients and calculates every derived property"""
    def __init__(self, coefficients: list[int]):
        self._coefficients: list[int] = coefficients
        self._poly: int = self._calculate_poly()
        self._block: bytes = self._poly.to_bytes(self.BYTE_LEN, byteorder='little')
        self._b64_block: str = base64.b64encode(self._block).decode()

    def _calculate_poly(self) -> int:
        poly = 0
        for coefficient in self._coefficients:
            poly |= 1 << coefficient
        return poly

    def get_coefficients(self) -> list[int]:
        return self._coefficients

    def get_poly(self) -> int:
        return self._poly

    def get_block(self) -> bytes:

        return self._block

    def get_b64_block(self) -> str:

        return self._b64_block
