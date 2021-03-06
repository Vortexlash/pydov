import os
import appdirs


datadir = appdirs.user_data_dir('dov')
os.makedirs(datadir, exist_ok=True)

excluded_process_names = ['keepassx']
excluded_window_names = ['Quake3-UrT']
