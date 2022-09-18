from typing import Any, List, Optional


""" 
MODES:
Values of percentiles retrieved from a block.
Example: [25, 50, 75] = retrieves the 3 transactions at 25%, 50%, 75%
percentiles of the block (transactions are in ascending order, weighted by gas used).
"""
MODES = {
    "slow": [10, 20, 30, 40, 50],
    "normal": [10, 30, 50, 70, 90],
    "fast": [50, 60, 70, 80, 90]
}


class BaseGasFeeEstimator:
    @classmethod
    def __estimate(
        cls,
        mode: str = "normal",
    ) -> Optional[Any]:
        mode = mode.lower()
        if mode not in MODES:
            raise Exception("The mode is incorrect!")

        percentiles = MODES[mode]
        return cls._get_estimated_gas_fee_by_percentiles(percentiles)

    @classmethod
    def _get_estimated_gas_fee_by_percentiles(
        cls,
        percentiles: List[int],
        latest_block_count: int = 4
    ) -> Any:
        raise NotImplemented

    @classmethod
    def get_estimated_gas_fees_by_mode(cls) -> dict:
        """
        Loop through modes and generates something like:
        {
            "prices": {
                "slow": 1,
                "normal": 2,
                "fast": 3,
            }
        }
        """
        return {
            "prices": {mode: cls.__estimate(mode=mode) for mode in MODES.keys()}
        }
