# Python tricks
Personal notes from cool but easy-to-forget Python syntax

# Setup
This project is designed to be used with conda. For that purpose, there is an `environment.yml` file provided for you

```
conda env create -f environment.yml
```

This will create a conda environment named `tricks`

Running this command will create a conda environment with all needed dependencies, fixed to Python 3.6.x

# Environment files per project

Due to versioning conflicts, the environment files might be split per project. The following table tell you which environment file to use for which project. If the project is not listed in this table, then use the `environment.yml` file.

|Project|Environment file|
|--|--|
|azure_ml|azureml-environment.yml|

# Python native

## Collections and arrays

* [Create sequence from range](python_native/01_collections/array_from_range.py)


# Attribution

As these are personal notes, content in this repo is inspired or taken from reading material I've come across:

* Fluent Python, by Luciano Ramalho
* Deep Learning with Python, by François Chollet