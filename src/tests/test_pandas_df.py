import unittest
from pandas.testing import assert_frame_equal
import pandas as pd
from src.utilities.pandas_df import mutliply_df_by_10

class TestHelpers(unittest.TestCase):
    def test_multiply_by_10_should_give_a_df_with_values_mutliplied_by_10(self):
        # arrange
        df = pd.DataFrame({
            'col_1': [1, 2, 3]
        })
        expected_df = pd.DataFrame({
            'col_1': [10, 20, 30]
        })
        # act
        actual_df = mutliply_df_by_10(df)
        # assert
        assert_frame_equal(expected_df, actual_df)

if __name__ == "__main__":
    unittest.main()