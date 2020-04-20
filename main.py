import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import MyModules.get_data as gd
import MyModules.generate_graph as gg
from pathlib import Path
import re

# Uncomment the following lines of code while executing for the first time
gd.get_data()
gd.clean_data() 
df = pd.read_excel(gd.CLEAN_DATA)

gg.generate_male_female_statewise_graph(df,Path('./Visualisations/MaleFemaleStatewise.png'))
gg.generate_statewise_death_recovery_graph(df,Path('./Visualisations/statewiseStatusGraph.png'))
gg.generate_death_recovery_total_plot(df,Path('./Visualisations/deathandrecoveryandtotal.png'))
gg.generate_age_based_graph(df,Path('./Visualisations/AgeHist.png'))

print("FINISH") 