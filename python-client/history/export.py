import csv
import json

from plotly.express import pd

from utils.constants import ExporterConstants


class Exporter:
    def __init__(self, filename, data, export):
        self.exportType = export
        self.filename = filename
        self.data = data

        if self.exportType == ExporterConstants.CSV:
            self.export_csv(data)

        elif self.exportType == ExporterConstants.JSON:
            self.export_json()

        elif self.exportType == ExporterConstants.PANDAS:
            self.export_pandas()

    def export_json(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def export_pandas(self):
        # keep date, open, high, low, close
        for line in self.data:
            del line[5:]
        df = pd.DataFrame(self.data, columns=['date', 'open', 'high', 'low', 'close'])
        df.set_index('date', inplace=True)
        return df

    def export_csv(self, data):
        with open(self.filename, 'w', newline='') as f:
            wr = csv.writer(f)
            for line in data:
                wr.writerow(line)
