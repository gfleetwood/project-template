from functions import *
import multiprocessing
import logging
from datetime import datetime
import pytz
from pathlib import Path
import csv
import pandas as pd
from tkinter.filedialog import askopenfilename
from fire import Fire

def read_dir_files(directory_path):
    
    files = [
        f
        for f in os.listdir(directory_path) 
        if os.path.isfile(os.path.join(directory_path, f))
        #and "pdf" in f
    ]
    
    return(files)

logging.basicConfig(filename = 'example.log', encoding = 'utf-8', level=logging.DEBUG)
pool = multiprocessing.Pool(multiprocessing.cpu_count())
home = str(Path.home())
now = datetime.now().isoformat()

# a,b = Fire(lambda x,y: x,y)

#with open(askopenfilename(), "r") as f: 
#    code = f.readlines()

#logging.debug('This message should go to the log file')
#logging.info('So should this')

#ans = pool.map(process_file, files)
#pool.close()

#est = pytz.timezone('America/New_York')
#current_time_in_est = datetime.now(est)
#formatted_time = current_time_in_est.strftime("%Y-%m-%d %H:%M:%S")

#df.to_csv("df.csv", index = False, quoting = csv.QUOTE_NONNUMERIC)
