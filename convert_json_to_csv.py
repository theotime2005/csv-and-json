import json
import csv


class JsonToTable:
    def __init__(self, file_to_convert):
        """
        Class to convert JSON to table
        :param file_to_convert: str
        """
        self.file_name = file_to_convert
        self.data = []
        self.headers = set()

    def open_and_parse_file(self):
        with open(self.file_name, "r", encoding="utf-8") as f:
            self.data = json.load(f)
            self._extract_headers()

    def _extract_headers(self):
        for row in self.data:
            self.headers.update(row.keys())

    def convert_to_csv(self, output_file):
        with open(output_file, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=sorted(self.headers))
            writer.writeheader()
            writer.writerows(self.data)
