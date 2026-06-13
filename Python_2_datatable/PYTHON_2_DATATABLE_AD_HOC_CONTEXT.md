# Python 2 DataTable project context

[ad-hoc note]

The user is working in:

`/home/ayhan/Masaüstü/Python Piscine/piscine_github/Python_2_datatable`

The authoritative project subject is:

`Python_2_Datatable.pdf`

A detailed Turkish cross-session context document was created at:

`/home/ayhan/Masaüstü/Python Piscine/piscine_github/Python_2_datatable/PYTHON_2_DATATABLE_CONTEXT_TR.md`

Project identity:

- Ecole 42 Training Piscine Python for datascience, module 2, DataTable.
- Subject version 1.00, ten pages.
- Four exercises: CSV loading, one-country life expectancy, two-country
  population comparison, and 1900 GDP/life-expectancy scatter projection.

Global subject requirements:

- Python 3.10.
- Explicit imports; wildcard imports are forbidden.
- No global variables and no executable application code at global scope.
- Every executable program must define `main()` and use a main guard.
- Every function must have a docstring.
- Code must pass flake8.
- Uncaught exceptions invalidate an exercise.
- Only correctly named files in the Git repository are evaluated.

Required exercise files:

- `ex00/load_csv.py`
- `ex01/load_csv.py`, `ex01/aff_life.py`
- `ex02/load_csv.py`, `ex02/aff_pop.py`
- `ex03/load_csv.py`, `ex03/projection_life.py`

Exercise essentials:

- ex00: `load(path)` prints dataset dimensions, returns the dataset, handles
  bad path/format cases, and returns `None` on error.
- ex01: load `life_expectancy_years.csv` through `load()`, select the campus
  country, and draw life expectancy with a title and both axis labels.
- ex02: load `population_total.csv` through `load()`, compare the campus
  country with another country, include only 1800-2050, and provide title,
  axis labels, and a legend identifying both lines.
- ex03: load
  `income_per_person_gdppercapita_ppp_inflation_adjusted.csv` and
  `life_expectancy_years.csv` through `load()`, match countries for year 1900,
  and draw GDP versus life expectancy. The PDF example is a scatter plot with
  a logarithmic GDP axis and shows a positive correlation.

At the time the context was prepared, the repository contained the PDF and
empty `ex00` through `ex03` directories; the CSV datasets were not present.

For future sessions, read `PYTHON_2_DATATABLE_CONTEXT_TR.md` first, then inspect
the current repository because implementation and dataset state may have
changed. The PDF remains the final authority where the context document labels
an item as an implementation recommendation or an inference from an example.
