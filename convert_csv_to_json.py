"""
This file can be convert a csv file to json format
"""
import csv
import json


class TableToJson:
    def __init__(self, file_to_convert, separator):
        """
        Class to convert table
        :param file_to_convert: str
        :param separator: str
        """
        self.file_name = file_to_convert
        self.separator = separator
        # Initialize variable to save the data
        self.table = []
        self.data = []
        self.heading_table = []

    def open_and_structur_file(self):
        with open(self.file_name, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f, delimiter=self.separator)
            self.heading_table = next(csv_reader)
            for line in csv_reader:
                self.table.append(line)
            self._check_and_delete_sub_column()

    def _check_and_delete_sub_column(self):
        max_length = len(self.heading_table)
        self.table = [row[:max_length] for row in self.table]

    def transform_to_json(self):
        for row in self.table:
            data = {}
            for header, value in zip(self.heading_table, row):
                data[header] = value
            self.data.append(data)

    def save_data(self):
        """
        Save data
        :return: None
        """
        file_name = self.file_name.split(".")[0]
        with open("{}.json".format(file_name), "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)
