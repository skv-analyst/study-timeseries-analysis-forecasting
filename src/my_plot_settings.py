import matplotlib.pyplot as plt
import seaborn as sns

def set_plot_style():
    sns.set_theme(
        style="whitegrid",
        context="notebook", 
        palette="husl",
        font_scale=1.1,
        rc={
            'figure.figsize': (10, 4),
            'figure.dpi': 120,
            'savefig.dpi': 300,
            'axes.titlesize': 16,
            'axes.labelsize': 14,
        }
    )
    
    
    plt.rcParams['font.family'] = 'DejaVu Sans'

set_plot_style()