#!/usr/bin/env python3

import pandas as pd

def get_csv_from_drive(sheet_id, sheet_name):
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={sheet_name}'
    return pd.read_csv(url, header=1, dtype=str)


