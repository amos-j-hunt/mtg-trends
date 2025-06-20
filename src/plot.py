import matplotlib.pyplot as plt
import pandas as pd

def plot_keyword_frequency(df, keyword):
    plt.plot(df["release_year"], df["keyword_ratio"], marker="o")
    plt.title(f"Keyword Frequency: {keyword.capitalize()} Over Time")
    plt.xlabel("Year")
    plt.ylabel(f"Ratio of Cards with {keyword.capitalize()}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_color_frequency(df_merged):
    colors = ['W', 'U', 'B', 'R', 'G', 'C']
    color_map = {'W': 'yellow', 'U': 'blue', 'B': 'black', 'R': 'red', 'G': 'green', 'C': 'gray'}

    plt.figure(figsize=(10, 6))

    for color in colors:
        plt.plot(
            df_merged["release_year"],
            df_merged[f"{color}_ratio"],
            marker="o",
            label=color,
            color=color_map[color]
        )

    plt.title("Color Frequency Over Time")
    plt.xlabel("Year")
    plt.ylabel("Ratio of Cards")
    plt.legend(title="Color")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_num_color_frequency(df_merged):
    plt.figure(figsize=(10,6))

    ## iterate over each number 0-5, plotting each
    for number in range(6):
        plt.plot(
            df_merged['release_year'],
            df_merged[f'number_{str(number)}_ratio'],
            marker='o',
            label=number
        )

    plt.title('Frequency of Numbers of Colors over Time')
    plt.xlabel('Year')
    plt.ylabel('Ratio of Cards')
    plt.legend(title = 'Number of Colors')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_complexity(df_means):
    # Create figure and twin axes
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot oracle text length on the left y-axis
    ax1.plot(df_means["release_year"], df_means["oracle_length"], color="blue", marker='o', label="Oracle Text Length")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Oracle Text Length (Median)", color="blue")
    ax1.tick_params(axis='y', labelcolor="blue")

    # Create twin axis for ruling count
    ax2 = ax1.twinx()
    ax2.plot(df_means["release_year"], df_means["rulings_count"], color="red", marker='s', label="Rulings Count")
    ax2.set_ylabel("Rulings Count (Median)", color="red")
    ax2.tick_params(axis='y', labelcolor="red")

    # Title and layout
    plt.title("Mean Oracle Text Length and Rulings Count Over Time")
    fig.tight_layout()
    plt.grid(True)
    plt.show()

def plot_mana_value(df_mana_value_over_time):
    plt.figure(figsize=(10,6))
    plt.plot(
        df_mana_value_over_time['release_year'],
        df_mana_value_over_time['mana_value'],
        marker = 'o'
    )