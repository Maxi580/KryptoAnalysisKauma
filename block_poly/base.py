from abc import ABC, abstractmethod


class Base(ABC):
    BYTE_LEN = 16

    @abstractmethod
    def get_coefficients(self) -> list[int]:
        pass

    @abstractmethod
    def get_poly(self) -> int:
        pass

    @abstractmethod
    def get_block(self) -> bytes:
        pass

    @abstractmethod
    def get_b64_block(self) -> str:
        pass
