# MTG Set/Color/Mechanic Trend Visualizer

## Overview

This project analyzes historical trends in Magic: The Gathering (MTG) card design, focusing on the frequency of mechanics, color distribution, and complexity over time. It aims to provide insight into the evolution of card design using time-series data and visual storytelling.

---

## Functional Requirements

### 1. Data Ingestion

* Load and parse `AllPrintings.json` from [MTGJSON](https://mtgjson.com/).
* Flatten nested structures into a tabular format.
* Extract and retain relevant fields:

  * `setCode`, `releaseDate`
  * `cardName`, `colors`, `colorIdentity`
  * `manaCost`, `convertedManaCost (cmc)`
  * `oracleText`, `keywords`

### 2. Mechanic Trend Analysis

* Track frequency of specific mechanics (e.g., "proliferate") by year or set.
* Identify and list top N mechanics introduced or trending each year.
* Visualize mechanic frequency using line or bar charts.

### 3. Color Distribution Analysis

* Count and visualize cards by individual colors (W, U, B, R, G).
* Group cards by color combination (mono, dual, tri-color, etc.).
* Show color distribution trends per year or per set.

### 4. Mana Cost and Complexity Trends

* Calculate average converted mana cost (CMC) by year.
* Measure card complexity using average oracle text length.
* Visualize changes using line plots, box plots, or histograms.

### 5. Visualization

* Generate visualizations using `matplotlib`, `seaborn`, or `plotly`.
* Save visualizations to `visualizations/` directory as `.png` or interactive `.html`.
* Optional: Interactive dashboard using `streamlit`.

### 6. Filtering and Exporting

* Enable filtering by:

  * Year or year range
  * Set type (core, expansion, commander, etc.)
  * Block or specific set code
* Export filtered data and summaries to CSV.
* Export selected visualizations to PNG or SVG.

---

## Non-Functional Requirements

* Python-based solution with clear module separation:

  * `parse.py` for data ingestion
  * `analyze.py` for aggregation logic
  * `plot.py` for visualizations
* Compatible with Jupyter notebooks and CLI execution.
* Codebase must be clean, commented, and modular.
* README must include setup instructions and usage examples.

---

## Use Cases

### Use Case 1: Mechanic Frequency Over Time

* **Goal**: Visualize how frequently "proliferate" appeared over time.
* **Input**: Mechanic name
* **Output**: Line chart with yearly frequency counts

### Use Case 2: Color Distribution Trends

* **Goal**: Show how common multicolor cards have become since 2000.
* **Input**: Year range
* **Output**: Stacked bar chart of color combinations by year

### Use Case 3: Card Design Complexity

* **Goal**: Determine whether cards have become more complex.
* **Metric**: Average length of oracle text
* **Output**: Line graph of complexity trend by year

### Use Case 4: Mana Curve Evolution

* **Goal**: See if mana curves are getting cheaper over time.
* **Metric**: Average converted mana cost (CMC)
* **Output**: Line or box plot of CMC per year

### Use Case 5: Year-in-Review Snapshot

* **Goal**: Summarize design trends for a specific year (e.g., 2010).
* **Output**: Top mechanics, color distribution, average CMC, average text length

---

## Tools and Libraries

* `pandas`, `json`, `collections`
* `matplotlib`, `seaborn`, `plotly`
* `jupyter` or `VS Code`
* Optional: `streamlit` for dashboard

---

## Directory Structure

```bash
mtg-trend-viz/
├── data/
│   └── AllPrintings.json
├── notebooks/
│   ├── mechanic_frequency.ipynb
│   ├── color_distribution.ipynb
│   └── avg_mana_cost_trend.ipynb
├── src/
│   ├── parse.py
│   ├── analyze.py
│   └── plot.py
├── visualizations/
│   └── ...
└── README.md
```

---

## Future Enhancements

* Add support for parsing `Rulings`, `Legalities`, or `Formats`.
* Integrate Scryfall API for art or external metadata.
* Animate trends over time with `plotly` or `matplotlib.animation`.
* Tag and group cards by design themes (e.g., graveyard recursion, token generation).

---

## License

This project is open source and uses data available under MTGJSON’s community license.
