import pandas as pd
import numpy as np
import os
from app.additional.mapping import Mapping


class Converter:
    def __init__(self, **kwargs):
        self._dest_dir = kwargs.get('dest_dir')
        self._work_dir = kwargs.get('work_dir')
        self._output_dir = kwargs.get('output_dir')
        os.makedirs(self._work_dir, exist_ok=True)
        os.makedirs(self._output_dir, exist_ok=True)

    def convert_to_csv(self):
        os.chdir(self._dest_dir)
        for f in os.listdir():
            for sheet in pd.ExcelFile(f).sheet_names:
                db = pd.read_excel(f, sheet)
                db.to_csv(self._work_dir + f[:-4] + '_' + sheet + '.csv', encoding='utf-8-sig', index=False)
        return True

    def converter(self):
        os.chdir(self._work_dir)
        for f in os.listdir():
            db = pd.read_csv(f)
            for k in db.columns:
                for i in range(len(db)):
                    if db[k][i] == 'Data':
                        db_index = i
                        break

            if db_index != '':
                db.columns = db.loc[db_index]
                db = db.iloc[db_index + 1:]
                db['territory'] = np.where(db[db.columns[-2]].isnull(), db['Data'], '1')
                db = Mapping(db, 'territory').get_mapping()
                db['indicator'] = np.where(~db[db.columns[-2]].isnull(), db['Data'], '')
                db['indicator'] = np.where(db[db.columns[-1]].isnull(), '', db['indicator'])
                db = Mapping(db, 'indicator').get_mapping()
                db = db[~db[db.columns[db_index]].isnull()]
            db_index = ''
            db.to_csv(self._output_dir + f[:-4] + '_converter' + '.csv', encoding='utf-8-sig', index=False)

        return True
