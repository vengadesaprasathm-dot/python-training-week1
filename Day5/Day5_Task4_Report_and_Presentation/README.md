# Day 5 – Task 4: Report and Presentation

This folder completes the report/presentation part of the employee data analysis project.

## Important folder placement

Extract this folder into your existing `Day5` directory. Keep Task 2 and Task 3 next to it:

```text
Day5/
├── Day5_Task2_Exploratory_Analysis/
│   └── employee_data.csv
├── Day5_Task3_Five_Visualisations/
│   └── Five_Visualisations.ipynb
└── Day5_Task4_Report_and_Presentation/
    ├── generate_findings.py
    ├── requirements.txt
    ├── README.md
    ├── report/
    └── presentation/
```

The report generator reads the actual Task 2 CSV, calculates numeric findings, and writes `report/Findings_Summary.md`. This avoids guessing the results.

## 1. Install requirements

Open the VS Code terminal at your repository root and run:

```powershell
python -m pip install -r Day5/Day5_Task4_Report_and_Presentation/requirements.txt
```

## 2. Generate the one-page findings summary

From the repository root, run:

```powershell
python Day5/Day5_Task4_Report_and_Presentation/generate_findings.py
```

It reads `Day5/Day5_Task2_Exploratory_Analysis/employee_data.csv` and creates:

`Day5/Day5_Task4_Report_and_Presentation/report/Findings_Summary.md`

Open the generated file and review the findings/recommendations before submitting.

## 3. Export the Task 3 notebook as HTML

Run this from the repository root:

```powershell
jupyter nbconvert --to html "Day5/Day5_Task3_Five_Visualisations/Five_Visualisations.ipynb" --output-dir "Day5/Day5_Task4_Report_and_Presentation/report"
```

The output should be `report/Five_Visualisations.html`. Open it in a browser and check that all five charts appear. Run all cells in the notebook and save it before exporting.

## 4. Presentation

Open `presentation/Presentation_Outline.md`. It contains a five-minute speaking plan. Use three charts from the Task 3 `reports/figures/` folder for the chart section.

## 5. GitHub Pull Request

The branch used in the training work is `feature/data-analysis`. First commit and push the completed work:

```powershell
git add Day5/
git commit -m "Add Day 5 Task 4 Report and Presentation"
git push origin feature/data-analysis
```

Then on GitHub:
1. Open the repository and select **Pull requests**.
2. Click **New pull request**.
3. Set base to `main` and compare to `feature/data-analysis`.
4. Create the pull request and share it with your trainer/reviewer.
5. Wait for review/approval. Address any requested changes.
6. Merge only after the reviewer approves and your repository rules allow it.
7. Copy the merged Pull Request URL for submission.

A review and merge must be performed by an authorized GitHub user; this package cannot perform that external approval or merge on your behalf.

## Submission checklist

- [ ] `report/Findings_Summary.md` generated and reviewed
- [ ] `report/Five_Visualisations.html` exported and checked
- [ ] `requirements.txt` included
- [ ] Five-minute presentation delivered to trainer
- [ ] Pull Request reviewed and merged
- [ ] Merged Pull Request URL shared with trainer
