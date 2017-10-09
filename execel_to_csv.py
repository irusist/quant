# -*- coding: utf-8 -*-

import os
import zipfile

import pandas as pd
from xlrd import open_workbook


dest_path = "/Users/zhulx/workspace/python/quant/data/ccs/"
for filename in os.listdir("/Users/zhulx/workspace/python/quant_data/ccs/"):
    fullname = "/Users/zhulx/workspace/python/quant_data/ccs/" + filename
    sheet_names = open_workbook(fullname).sheet_names()
    for sheet_name in sheet_names:
        data = pd.read_excel(fullname, sheet_name)
        base_filename = dest_path + filename[:-5] + '_' + sheet_name
        csv_filename = base_filename + ".csv"
        data.to_csv(csv_filename, sep='\t', header=False, index=False, encoding='utf-8')
        # zip_filename = base_filename + ".zip"
        # ziphandler = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
        # ziphandler.write(csv_filename)
        # ziphandler.close()
