import glob
import os

directory = os.path.dirname(os.path.realpath(__file__))
noises_list = glob.glob(f'{directory}/*.mp3')
