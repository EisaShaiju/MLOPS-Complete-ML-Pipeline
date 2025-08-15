# MLOps Complete ML Pipeline

This repository demonstrates a complete MLOps workflow for building, training, and evaluating machine learning models using DVC, DVCLive, and Supabase cloud storage.

## Project Structure

```
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_building.py
│   └── model_evaluation.py
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── models/
│   └── model.pkl
├── reports/
│   └── metrics.json
├── params.yaml
├── dvc.yaml
├── .gitignore
└── README.md
```

## Features

- **Modular pipeline:** Each ML step is a separate script and DVC stage.
- **Parameter management:** Easily tune hyperparameters via `params.yaml`.
- **Experiment tracking:** Integrated with DVCLive for metrics and plots.
- **Cloud storage:** Uses Supabase buckets for remote data and model storage.
- **Version control:** All code and pipeline steps tracked with Git and DVC.

## Getting Started

### Prerequisites

- Python 3.8+
- [DVC](https://dvc.org/doc/install)
- [DVCLive](https://github.com/iterative/dvclive)
- [Supabase Python client](https://github.com/supabase-community/supabase-py)
- (Optional) [Virtual environment](https://docs.python.org/3/library/venv.html)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/mlops-complete-ml-pipeline.git
   cd mlops-complete-ml-pipeline
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Initialize DVC:

   ```
   dvc init
   ```

### Usage

1. **Run the pipeline:**

   ```
   dvc repro
   ```

2. **Track experiments:**

   ```
   dvc exp run
   dvc exp show
   ```

3. **Push data and models to Supabase:**

   ```
   dvc push
   ```

4. **Pull data and models from Supabase:**
   ```
   dvc pull
   ```

### Customization

- Edit `params.yaml` to change model or pipeline parameters.
- Modify scripts in `src/` for custom data processing or modeling.

## Contributing

Feel free to open issues or submit pull requests for improvements!

