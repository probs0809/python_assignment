import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import get_data
import generate_graph as gg
from pathlib import Path

# Uncomment the following lines of code while executing for the first time
get_data.get_data()
get_data.clean_data() 
df = pd.read_excel(get_data.CLEAN_DATA)
print("Generating graphs...")
gg.generate_male_female_statewise_graph(df,Path('./MaleFemaleStatewise.png'))
gg.generate_statewise_death_recovery_graph(df,Path('./statewiseStatusGraph.png'))
gg.generate_death_recovery_total_plot(df,Path('./deathandrecoveryandtotal.png'))
print("Graphs generated in local files")
print("FINISH")