# Auto Insurance Analysis

This project aims to analyze auto insurance data obtained from Kaggle. The analysis will focus on exploring the dataset, cleaning the data, and visualizing key insights.

## Project Structure

```
auto-insurance-analysis
├── data
│   └── auto-insurance-data.xlsx
├── notebooks
│   └── analysis.ipynb
├── src
│   └── data_processing.py
├── requirements.txt
└── README.md
```

## Files Description

- **data/auto-insurance-data.xlsx**: Contains the auto insurance data downloaded from Kaggle in Excel format.
  
- **notebooks/analysis.ipynb**: A Jupyter notebook for data analysis, including code for loading the data, performing exploratory data analysis, and visualizing results.

- **src/data_processing.py**: Python file with functions for data processing, including `load_data()`, `clean_data()`, and `transform_data()`.

- **requirements.txt**: Lists the Python packages required for the project, such as `pandas`, `numpy`, and `openpyxl`.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd auto-insurance-analysis
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

- To start the analysis, open the Jupyter notebook located in the `notebooks` directory:
  ```
  jupyter notebook notebooks/analysis.ipynb
  ```

- Use the functions defined in `src/data_processing.py` to load and preprocess the data as needed.