## Purpose
Matches ADFG numbers to vessel/fisherman
## Install
pandas is required

```pip3 install pandas```

## Usage
```fisherman.csv``` is a list of fishermen and vessel names with columns as so

|   Fisherman Name  |   Boat  |
|-------------------|---------|

```vessels.csv``` is the yearly download of vessel information for the current year at [CFEC](https://www.cfec.state.ak.us/plook/#downloads)

run with
```python3 filter.py```

It outputs a csv file ```fisherman_filtered.csv``` with the following columns
|   Fisherman Name  |   Boat  |   Last name  |   ADFG Number  |   Vessel Name  |
|-------------------|---------|--------------|----------------|----------------|


## Main Issues
Currently some last names get (possibly random) ADFG numbers despite not having a vessel assigned. If boat/vessel name is blank in the output, the ADFG number is likely incorrect.

The script will not match vessels if the permit is out of date, or if the permit holders name is different from the fisherman.
