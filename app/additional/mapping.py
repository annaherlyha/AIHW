class Mapping:
    def __init__(self, df, df_column_name):
        self._df = df
        self._df_column_name = df_column_name

    def get_mapping(self):
        value_codes = 0

        for v in self._df.index:
            if len(str(self._df[self._df_column_name][v])) > 1:

                value_codes = self._df[self._df_column_name][v]
            else:

                self._df[self._df_column_name][v] = value_codes

        return self._df
