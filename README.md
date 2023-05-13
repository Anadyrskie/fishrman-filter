## Purpose
Matches ADFG numbers to vessel/fisherman
## Install
pandas is required

```pip3 install pandas```

## Usage
```fisherman.csv``` is a list of fishermen and vessel names with headings as so

|   Fisherman Name  |   Boat   |   Last name  |

```vessels.csv``` is the yearly download of vessel information for the current year at [CFEC](https://www.cfec.state.ak.us/plook/#downloads)

run with
```python3 filter.py```

It outputs a csv file ```fisherman_filtered.csv``` with the following headings
|   Fisherman Name  |   Boat  |   Last name  |   ADFG Number  |   Vessel Name  |
|-------------------|---------|--------------|----------------|----------------|
|                   |         |              |                |                |
|                   |         |              |                |                |

