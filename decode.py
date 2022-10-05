import sys
import os
import requests, json, datetime, csv, time
from pandas import json_normalize
import pandas as pd
from datetime import datetime

df= pd.read_csv('sportbetec.csv', encoding ='utf-8')


df.to_excel('sportbetec.xlsx', index=False, encoding ='ISO-8859-1')