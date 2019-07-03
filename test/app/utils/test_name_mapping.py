import unittest
import pandas as pd
from app.utils.name_mapping import NameMapping
from pandas.util.testing import assert_frame_equal


class TestNameMapping(unittest.TestCase):
    """
    Test that it can check work for class NameMapping
    """
    _test_df_good = pd.DataFrame(data={'col1': ['11', '']})
    _test_df_good_result = pd.DataFrame(data={'col1': ['11', '11']})
    _test_df_no_changes = pd.DataFrame(data={'col1': [1, 1]})
    _test_df_no_changes_result = pd.DataFrame(data={'col1': [1, 1]})
    _test_df_bad = 1
    _column_name = [3.9]

    def test_get_mapping_good(self):
        """
        Test that the expected column will change value if it has length is more than 1
        """
        assert_frame_equal(NameMapping(self._test_df_good, 'col1').get_mapping(),
                           self._test_df_good_result)

    def test_get_mapping_no_changes(self):
        """
        Test that the expected column will not change value if it has length is less or equal 1
        """
        assert_frame_equal(NameMapping(self._test_df_no_changes, 'col1').get_mapping(),
                           self._test_df_no_changes_result)

    def test_get_mapping_check_type(self):
        """
        Test that it can check that value is not dataframe
        """
        with self.assertRaisesRegex(TypeError, "Wrong type"):
            NameMapping(self._test_df_bad, 'col1').get_mapping()

    def test_get_mapping_no_column(self):
        """
        Test that it can check if column doesn't exist in a dataframe
        """
        with self.assertRaisesRegex(KeyError, "This column doesn't exist in a dataframe"):
            NameMapping(self._test_df_good, self._column_name).get_mapping()


if __name__ == '__main__':
    unittest.main()
