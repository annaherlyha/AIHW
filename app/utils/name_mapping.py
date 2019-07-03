import pandas as pd


class NameMapping:
    """
    This class fills the gaps in the database column with values ​​that were before the gap,
    if value in column has length more than 1
    ....

    Attributes
    ----------
    self._df: dataframe
        dataframe with gaps in column or without gaps
    self._df_column_name: str
        column in dataframe
    self.__value_codes: NoneType
        a dummy into which values ​​from the column will be written
         when a certain condition described above is met

    Methods
    -------
    get_mapping
        Fills the gaps in the database column with values ​​that were before the gap,
            if value in column has length more than 1
    """

    def __init__(self, df, df_column_name):
        self._df = df
        self._df_column_name = df_column_name
        self.__value_codes = None

    def get_mapping(self):
        """
        Fills the gaps in the database column with values ​​that were before the gap,
            if value in column has length more than 1

        Raises
        ------
        TypeError
                  If self._df is not dataframe
                  If self._df_column_name can not be use as name of dataframe column
        KeyError
                  If self._df_column_name doesn't exist in a dataframe
        :return:
        dataframe
           a dataframe with updated values if gaps was in dataframe column
           the same dataframe if gaps was not found in column
        """
        if isinstance(self._df, pd.DataFrame):
            try:
                if str(self._df_column_name) in self._df.columns:
                    for v in self._df.index:
                        if len(str(self._df[self._df_column_name][v])) > 1:
                            self.__value_codes = self._df[self._df_column_name][v]
                        else:
                            if self.__value_codes is not None:
                                self._df[self._df_column_name][v] = self.__value_codes
                    return self._df
                else:
                    raise KeyError("This column doesn't exist in a dataframe")
            except TypeError:
                raise TypeError("This type cannot be use for dataframe column")

        else:
            raise TypeError("Wrong type")
