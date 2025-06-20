from datetime import datetime
import pandas as pd

def compute_release_year(df, cutoff=None):
    if cutoff is None:
        cutoff = datetime.now().year
    df['release_year'] = pd.to_datetime(df['release_date']).dt.year
    df = df[df['release_year'] <= cutoff]
    return df

def compute_color_features(df):
    df['number_of_colors'] = df['colors'].apply(len)
    return df

def compute_oracle_length(df):
    df['oracle_length'] = (df['oracle_text']
                           .apply(lambda t: 0 if not t else len(t))
    )
    return df

def compute_rulings_count(df):
    df['rulings_count'] = (df['rulings']
                                    .apply(lambda r: 0 if not r else len(r))
    )
    return df

def compute_cards_per_year(df):
    df_cards_per_year = (df
                        .groupby('release_year')
                        .size()
                        .reset_index(name='count')
    )
    return df_cards_per_year

def explode_by_keywords(df):
    df_keywords_exploded = df.explode('keywords')
    df_keywords = df_keywords_exploded[df_keywords_exploded['keywords'].notna()].copy()
    df_keywords['keyword_normalized'] = df_keywords['keywords'].str.lower()
    return df_keywords

def explode_by_colors(df):
    df['colors_fixed'] = df['colors'].apply(lambda c: ['C'] if not c else c)    
    df_colors = df.explode('colors_fixed').copy()
    return df_colors

def keyword_frequency(df_keywords, keyword):
    # Total cards per year
    df_total = df_keywords.groupby('release_year').size().reset_index(name='count')
    
    # Cards with the selected keyword
    df_keyword = df_keywords[df_keywords['keyword_normalized'] == keyword]
    df_keyword_per_year = df_keyword.groupby('release_year').size().reset_index(name=keyword)
    
    # Merge and compute ratio
    df_merged = pd.merge(df_total, df_keyword_per_year, on='release_year', how='left')
    df_merged[keyword] = df_merged[keyword].fillna(0).astype(int)
    df_merged['keyword_ratio'] = df_merged[keyword] / df_merged['count']
    
    return df_merged

def top_keywords(df_keywords):
    df_keyword_counts_by_year = (df_keywords
                             .groupby(['release_year', 'keyword_normalized'])
                             .size()
                             .reset_index(name='count')
    )

    top_keywords_by_year = (
        df_keyword_counts_by_year
        .groupby("release_year", group_keys=False)
        .apply(lambda grp: grp.nlargest(3, "count"))
    )

    top_keywords_summary = (
        top_keywords_by_year
        .groupby("release_year")["keyword_normalized"]
        .apply(lambda kws: ", ".join(kws))
        .reset_index(name="top_keywords")
    )

    return top_keywords_summary

def compute_color_frequency(df_colors, df_cards_per_year):
    colors = ['W', 'U', 'B', 'R', 'G', 'C']
    df_merged = df_cards_per_year.copy()
    for color in colors:
        df_color = df_colors[df_colors['colors_fixed'] == color]
        df_color_per_year = (
            df_color.groupby('release_year').size().reset_index(name=color)
        )
        df_merged = pd.merge(df_merged, df_color_per_year, on='release_year', how='left')
        df_merged[color] = df_merged[color].fillna(0).astype(int)
        df_merged[f'{color}_ratio'] = df_merged[color] / df_merged['count']
    return df_merged

def compute_num_color_frequency(df_all_cards, df_cards_per_year):
    df_merged = df_cards_per_year.copy()
    for number in range(6):
        df_number = df_all_cards[df_all_cards['number_of_colors'] == number]
        df_number_per_year = (
            df_number.groupby('release_year').size().reset_index(name=number)
        )
        df_merged = pd.merge(df_merged, df_number_per_year, on='release_year', how='left')
        df_merged[number] = df_merged[number].fillna(0).astype(int)
        df_merged[f'number_{str(number)}_ratio'] = df_merged[number] / df_merged['count']
    return df_merged

def compute_complexity(df_all_cards):
    df_means = (
        df_all_cards
        .groupby("release_year")[["oracle_length", "rulings_count"]]
        .mean()
        .reset_index()
    )
    return df_means

def compute_mana_value(df_all_cards):
    df_mana_value_over_time = (
        df_all_cards
        .groupby('release_year')[['mana_value']]
        .mean()
        .reset_index()
    )
    return df_mana_value_over_time