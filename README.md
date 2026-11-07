# MachineLearning_with_AT

My learning notes for the path toward machine learning engineering: small, self-contained Python scripts for core Python, NumPy and Pandas, plus short notes on neural networks and generative AI. It is a study log, not a library or a finished course.

## Contents

### 1. Python programming

Folder: [`Python_Programming/`](Python_Programming)

| Topic | Scripts |
|---|---|
| [Python basics, Variables, Operators, Conditional Statements](Python_Programming/Python%20basics%2C%20Variables%2C%20Operators%2C%20Conditional%20Statements) | [`variables.py`](Python_Programming/Python%20basics%2C%20Variables%2C%20Operators%2C%20Conditional%20Statements/variables.py), [`operators.py`](Python_Programming/Python%20basics%2C%20Variables%2C%20Operators%2C%20Conditional%20Statements/operators.py), [`conditional_statements.py`](Python_Programming/Python%20basics%2C%20Variables%2C%20Operators%2C%20Conditional%20Statements/conditional_statements.py) |
| [Lists and Strings](Python_Programming/Lists%20and%20Strings) | [`lists.py`](Python_Programming/Lists%20and%20Strings/lists.py), [`strings.py`](Python_Programming/Lists%20and%20Strings/strings.py) |
| [Dictionary, Tuple, Set](Python_Programming/Dictionary%2C%20Tuple%2C%20Set) | [`dictionary.py`](Python_Programming/Dictionary%2C%20Tuple%2C%20Set/dictionary.py), [`tuple.py`](Python_Programming/Dictionary%2C%20Tuple%2C%20Set/tuple.py), [`set.py`](Python_Programming/Dictionary%2C%20Tuple%2C%20Set/set.py), [`break_continue.py`](Python_Programming/Dictionary%2C%20Tuple%2C%20Set/break_continue.py) |
| [Loops](Python_Programming/Loops) | [`while_loop.py`](Python_Programming/Loops/while_loop.py), [`nested_loops.py`](Python_Programming/Loops/nested_loops.py), [`loop_else.py`](Python_Programming/Loops/loop_else.py) |
| [For Loop, Break, and Continue statements](Python_Programming/For%20Loop%2C%20Break%2C%20and%20Continue%20statements) | [`for_loop.py`](Python_Programming/For%20Loop%2C%20Break%2C%20and%20Continue%20statements/for_loop.py) |
| [Functions, Return Statement, Recursion](Python_Programming/Functions%2C%20Return%20Statement%2C%20Recursion) | [`functions.py`](Python_Programming/Functions%2C%20Return%20Statement%2C%20Recursion/functions.py), [`return_statement.py`](Python_Programming/Functions%2C%20Return%20Statement%2C%20Recursion/return_statement.py), [`recursion.py`](Python_Programming/Functions%2C%20Return%20Statement%2C%20Recursion/recursion.py) |
| [File Handling, Exception Handling](Python_Programming/File%20Handling%2C%20Exception%20Handling) | [`file_handling.py`](Python_Programming/File%20Handling%2C%20Exception%20Handling/file_handling.py), [`exception_handling.py`](Python_Programming/File%20Handling%2C%20Exception%20Handling/exception_handling.py) |
| [Object-Oriented Programming (OOP)](Python_Programming/Object-Oriented%20Programming%20%28OOP%29) | [`classes.py`](Python_Programming/Object-Oriented%20Programming%20%28OOP%29/classes.py), [`inheritance.py`](Python_Programming/Object-Oriented%20Programming%20%28OOP%29/inheritance.py), [`encapsulation.py`](Python_Programming/Object-Oriented%20Programming%20%28OOP%29/encapsulation.py), [`polymorphism.py`](Python_Programming/Object-Oriented%20Programming%20%28OOP%29/polymorphism.py) |

### 2. Data analysis

**NumPy** ([`Data_Analysis/NumPy/`](Data_Analysis/NumPy))

- [`vectors_matrix.py`](Data_Analysis/NumPy/vectors_matrix.py): creating vectors and matrices
- [`reshaping_arrays.py`](Data_Analysis/NumPy/reshaping_arrays.py): reshaping arrays
- [`diagonal_trace.py`](Data_Analysis/NumPy/diagonal_trace.py): diagonal and trace of a matrix
- [`mean_variance_std.py`](Data_Analysis/NumPy/mean_variance_std.py): mean, variance and standard deviation
- [`operations.py`](Data_Analysis/NumPy/operations.py): add, subtract, multiply, dot and cross product

**Pandas** ([`Data_Analysis/Pandas/`](Data_Analysis/Pandas))

- [`create_dataframe.py`](Data_Analysis/Pandas/create_dataframe.py): creating DataFrames from a list and a dict
- [`series_dataframes.py`](Data_Analysis/Pandas/series_dataframes.py): Series and DataFrames
- [`slicing.py`](Data_Analysis/Pandas/slicing.py): slicing rows and columns
- [`csv_read_write.py`](Data_Analysis/Pandas/csv_read_write.py): reading a CSV, filtering it and writing `output.csv` (uses the bundled [`data.csv`](Data_Analysis/Pandas/data.csv) and recreates it if it is missing)
- [`handling_missing_values.py`](Data_Analysis/Pandas/handling_missing_values.py): finding, filling and dropping missing values
- [`groupby_concat.py`](Data_Analysis/Pandas/groupby_concat.py): `groupby` (mean with `numeric_only=True`, multi-aggregation with `agg`) and `concat`

### 3. Neural networks

- [`neural_network.md`](Neural_Network/neural_network.md): a short definition of what a neural network is

### 4. Generative AI

- [`Fundamentals_notes.md`](GenerativeAI/Fundamentals_notes.md): notes on generative AI fundamentals (AI's impact on work, LLM tokens, prompt injection, legal risks of generative AI, open-source LLMs for commercial use, Databricks Lakehouse AI features)

## Running the scripts

Each script is standalone and prints its results. The Python scripts use only the standard library; the data-analysis scripts need NumPy and Pandas.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # numpy, pandas (pandas 2.x)

python Data_Analysis/NumPy/operations.py
python Data_Analysis/Pandas/groupby_concat.py
python "Python_Programming/Loops/nested_loops.py"
python "Python_Programming/File Handling, Exception Handling/exception_handling.py" 5
```

Folder names contain spaces, so quote paths on the command line. `exception_handling.py` takes the number as an argument or asks for it interactively. All scripts were checked to run on Python 3.11 with pandas 3.x and NumPy 2.x.

## Roadmap

The repo follows a Python-first ML learning path. Covered so far:

1. Python programming
2. Data analysis with NumPy and Pandas
3. Neural network basics (started)
4. Generative AI fundamentals (started)
