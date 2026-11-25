# Day 5 – Task 3: Five Visualisations

## Folder structure

```text
Day5_Task3_Five_Visualisations/
├── Five_Visualisations.ipynb
├── README.md
└── reports/
    └── figures/
```

## Important: reuse the Task 2 dataset

This notebook reads the existing CSV from:

`../Day5_Task2_Exploratory_Analysis/employee_data.csv`

Keep the Task 2 and Task 3 folders next to each other inside `Day5`, like this:

```text
Day5/
├── Day5_Task2_Exploratory_Analysis/
│   └── employee_data.csv
└── Day5_Task3_Five_Visualisations/
    ├── Five_Visualisations.ipynb
    └── reports/
        └── figures/
```

## Steps to run

1. Open the `Day5` project in VS Code.
2. Open `Day5_Task3_Five_Visualisations/Five_Visualisations.ipynb`.
3. Select your Python virtual environment (`.venv`) as the notebook kernel.
4. If needed, install the libraries in the VS Code terminal:

   ```powershell
   python -m pip install pandas matplotlib seaborn jupyter ipykernel
   ```

5. Run all notebook cells from top to bottom.
6. Check `reports/figures/`. The notebook saves five PNG chart files there.

## Charts included

1. Bar chart – average monthly income by department.
2. Histogram – employee age distribution.
3. Scatter plot – age versus monthly income, coloured by department.
4. Line chart – average monthly income by age.
5. Box plot – monthly income distribution by department.

Each chart has a title, labelled axes, units, and a legend where needed. A short insight sentence follows each chart.

**Note:** The notebook expects the Task 2 folder and its `employee_data.csv` to remain in the same `Day5` directory.
