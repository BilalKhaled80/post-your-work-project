>**Note**: Please **fork** this Udacity repository so you have a **remote** repository in **your** GitHub account. Then you can clone the remote repository to your local machine. Later, as a part of the project, you will push your changes to the remote repository in your GitHub account.


# Project Title

This project contains a **bikeshare_starter.py** script, which provides functionality to:
- load and filter data using load_data() and get_filters()
- Calculate & display statistics on the most frequent times of travel using time_stats(df)
- Calculate & display statistics on the most popular stations and trip using station_stats(df)
- Calculate & display statistics on the total and average trip duration using trip_duration_stats(df)
- Calculate & display statistics on bikeshare users using user_stats(df)

## Information about how to use your project

### Tools and Dependecies
- Install Python Version 3.x
- Install dependencies in bash using:
```bash
  - pip install pandas
  - pip install numpy
```

### Data
The city data files are:
- chicago.csv
- new_york_city.csv
- washington.csv
 
**_Note_**: We do not want to push the city data files to GitHub, as they are large files. Add them to `.gitignore`

### How to run the script
```bash
python bikeshare_starter.py
```
After running, the script will prompt you to choose:
- City: name of the city to analyze
- Month: name of the month to filter by, or "all" to apply no month filter
- Day: name of the day of week to filter by, or "all" to apply no day filter

#### Example:

```bash
    1   Please enter the name of the city to analyze (chicago, new york city, washington):
    2   new york city
    3   Please enter the month to analyze (all, january, february, ..., june):
    4   february
    5   Please enter the day to analyze (all, monday, tuesday, ..., sunday):
    6   monday
```

The script will then display e.g.:
- the most common month
- the most common day of week
- the most common start hour

## Contribution guidelines

Feel free to contribute to this project!. Please make sure to follow these steps:
1. Fork the repo. and create your own branch
```bash
git checkout -b your-branch-name
```
2. Ensure your code is clean 
3. Test your changes
4. Commit and push your changes
5. Create new PR

## Credits

- _Udacity_ for providing the project and the corresponding data
- _Python_ for dependencies like pandas and numpy
- for everyone who supported the project

## Date created

- November 14, 2025
- Author: Bilal Khaled