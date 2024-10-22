import json
import sys
from pathlib import Path
from typing import Dict, Any, Callable
import base64

from block_poly.b64_block import B64Block
from block_poly.block import Block
from block_poly.poly import Poly
from block_poly.coefficients import Coefficients

from sea128 import sea_encrypt, sea_decrypt
from gfmul import gfmul


def poly2block(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Convert coefficients to base64 block"""
    coefficients = arguments["coefficients"]
    result = Coefficients(coefficients)
    return {"block": result.get_b64_block()}


def block2poly(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Convert base64 block to coefficients"""
    block = arguments["block"]
    result = B64Block(block)
    return {"coefficients": result.get_coefficients()}


ACTION_PROCESSORS = {
    "poly2block": poly2block,
    "block2poly": block2poly
}


def process_testcases(input_json):
    """Process all test cases and return results"""
    responses = {}

    for test_id, test_data in input_json["testcases"].items():
        action = test_data["action"]
        arguments = test_data["arguments"]

        if action in ACTION_PROCESSORS:
            func = ACTION_PROCESSORS[action]
            responses[test_id] = func(arguments)

    return {"responses": responses}


def main():
    print("\n\n kauma gets executed \n\n")

    if len(sys.argv) != 2:
        print("Usage: ./kauma <test_file.json>", file=sys.stderr)
        sys.exit(1)

    test_file = Path(sys.argv[1])

    if not test_file.exists():
        raise f"Error: File {test_file} does not exist"

    try:
        with open(test_file) as f:
            input_data = json.load(f)

        print("Results get calculated")
        results = process_testcases(input_data)
        print(f"results: {results}")

        print(json.dumps(results))

    except Exception as e:
        raise f"Error: {e}"


if __name__ == "__main__":
    main()
