import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('Agg')
matplotlib.rc('font', family='Microsoft JhengHei')

def generate_player_stat_plot(player_name, data):
    output_dir = "static/playerstats"
    os.makedirs(output_dir, exist_ok=True)

    player_data = data[data['Player'] == player_name]
    if player_data.empty:
        raise ValueError(f"找不到球員 {player_name} 的資料")

    stats = player_data.iloc[0][['PPG', 'RPG', 'APG', 'SPG', 'BPG']]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=stats.index, y=stats.values, palette="viridis")
    plt.title(f"{player_name} 的球員數據表現")
    plt.ylabel("每場平均數值")
    plt.ylim(0, max(stats.values) + 5)
    plt.grid(axis='y')
    plt.tight_layout()

    filename = f"stats_{player_name.replace(' ', '_')}.png"
    output_path = os.path.join(output_dir, filename)
    plt.savefig(output_path)
    plt.close()

    return output_path
