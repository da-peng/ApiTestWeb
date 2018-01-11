#encoding=utf-8
import xlrd


class ExcelUtil(object):

    def __init__(self,file_path,sheet_name=None):

        self._file_path = file_path
        self._sheet_name = sheet_name


    def get_workbook_and_sheet(self):

        workbook = xlrd.open_workbook(self._file_path)

        if self._sheet_name is None:

            sheet_name = workbook.sheet_names()[0]
            sheet = workbook.sheet_by_name(sheet_name)

            return workbook,sheet

        sheet = workbook.sheet_by_name(sheet_name=self._sheet_name)

        return workbook,sheet







