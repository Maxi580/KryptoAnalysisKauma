from block_poly.block import Block
from block_poly.coefficients import Coefficients
from block_poly.b64_block import B64Block
from block_poly.poly import Poly

from gfmul import gfmul
from sea128 import sea_encrypt, sea_decrypt
from fde import encrypt_fde, decrypt_fde


def test_poly_2_block():
    coefficients = [12, 127, 9, 0]
    result = Coefficients(coefficients)
    assert result.get_b64_block() == "ARIAAAAAAAAAAAAAAAAAgA=="


def test_block_2_poly():
    b64_block = "ARIAAAAAAAAAAAAAAAAAgA=="
    result = B64Block(b64_block)
    assert result.get_coefficients() == [0, 9, 12, 127]


def test_gfmul():
    a = "ARIAAAAAAAAAAAAAAAAAgA=="
    b = "AgAAAAAAAAAAAAAAAAAAAA=="

    a_poly = B64Block(a).get_block()
    b_poly = B64Block(b).get_block()

    result = gfmul(a_poly, b_poly)

    b64_result = Block(result).get_b64_block()

    assert b64_result == "hSQAAAAAAAAAAAAAAAAAAA=="


def test_sea128_encrypt():
    test_key = "istDASeincoolerKEYrofg=="
    test_plaintext = "yv66vvrO263eyviIiDNEVQ=="

    byte_test_key = B64Block(test_key).get_block()
    byte_test_plaintext = B64Block(test_plaintext).get_block()

    byte_result = sea_encrypt(byte_test_key, byte_test_plaintext)
    b64_result = Block(byte_result).get_b64_block()

    assert b64_result == "D5FDo3iVBoBN9gVi9/MSKQ=="


def test_sea_128_decrypt():
    test_key = "istDASeincoolerKEYrofg=="
    test_ciphertext = "D5FDo3iVBoBN9gVi9/MSKQ=="

    byte_test_key = B64Block(test_key).get_block()
    byte_test_ciphertext = B64Block(test_ciphertext).get_block()

    byte_result = sea_decrypt(byte_test_key, byte_test_ciphertext)
    b64_result = Block(byte_result).get_b64_block()

    assert b64_result == "yv66vvrO263eyviIiDNEVQ=="


def test_fde_encrypt():
    key = "B1ygNO/CyRYIUYhTSgoUysX5Y/wWLi4UiWaVeloUWs0="
    tweak = "6VXORr+YYHrd2nVe0OlA+Q=="
    input = "/aOg4jMocLkBLkDLgkHYtFKc2L9jjyd2WXSSyxXQikpMY9ZRnsJE76e9dW9olZIW"

    byte_key = B64Block(key).get_block()
    byte_tweak = B64Block(tweak).get_block()
    byte_input = B64Block(input).get_block()

    solution = encrypt_fde(byte_key, byte_tweak, byte_input)
    b64_solution = Block(solution).get_b64_block()

    assert b64_solution == "mHAVhRCKPAPx0BcufG5BZ4+/CbneMV/gRvqK5rtLe0OJgpDU5iT7z2P0R7gEeRDO"


def test_fde_decrypt():
    key = "B1ygNO/CyRYIUYhTSgoUysX5Y/wWLi4UiWaVeloUWs0="
    tweak = "6VXORr+YYHrd2nVe0OlA+Q=="
    input = "lr/ItaYGFXCtHhdPndE65yg7u/GIdM9wscABiiFOUH2Sbyc2UFMlIRSMnZrYCW1a"

    byte_key = B64Block(key).get_block()
    byte_tweak = B64Block(tweak).get_block()
    byte_input = B64Block(input).get_block()

    solution = decrypt_fde(byte_key, byte_tweak, byte_input)
    b64_solution = Block(solution).get_b64_block()

    assert b64_solution == "SGV5IHdpZSBrcmFzcyBkYXMgZnVua3Rpb25pZXJ0IGphIG9mZmVuYmFyIGVjaHQu"