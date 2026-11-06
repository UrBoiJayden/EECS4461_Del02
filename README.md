# EECS4461_Del02
## Project Overview
A Mesa-based computational model based on the Schelling Segregation model to explore how individual user preferences and collective trend scores influence content rankings in a simplified Instagram-style recommendation system.

The model includes three categories: Fitness, Cooking, and Gaming. It uses three simulated users with different preferences to calculate individual and overall trend scores.

For the project’s inquiry question, rationale, representation choices, assumptions, interpretation of results, and proposed next steps, refer to the DEL02.1 report.

## Original Mesa Example

The original example used as the basis for this project is Mesa’s Schelling Segregation Model.

Its preserved source code is located in:

src/schelling/

The SOURCE.md file contains the original source information, version details, and attribution.


## Adapted Project Model

Our adapted social media trends simulation is located in:

src/project_model/model.py

It uses user and trend agents to represent different content categories and investigates how recommendation system sensitivity influences individual and overall trend rankings.


## Software Requirements
The Python version needed to run the code, and the one we used is 3.15.2. For python, we used Python 3.11 .
The Mesa version used to run this code is 3.5.2
Python can be downloaded from the official ⁠Python website: https://www.python.org/downloads/

## Model Description
Users:

* Represent simulated social media users.
* Each user has preset preferences for Fitness, Cooking, and Gaming.
* Preferences range from 0 to 3, representing how many videos the user liked within each trend.
* A value of 0 means the user liked none of the three videos, while a value of 3 means they liked all three videos.
* Each preference is converted into a personal trend score.

Trends:

* Represents the three content categories: Fitness, Cooking, and Gaming.
* Each trend calculates the personal scores based on that category across all users.
* The average personal score is calculated for each trend.
* The recommendation system’s sensitivity is applied to each user’s personal score to calculate their adjusted trend scores.

## Outputs
The adapted model produces two types of results:

* Individual user rankings for Fitness, Cooking, and Gaming.
* Overall rankings and scores for each trend.

The submitted output files are located in:

outputs/

These outputs allow the baseline and alternative sensitivity conditions to be compared, they are shown in .txt files

## Commands 

python -m pip install -U mesa    Installs mesa 

python -c "import mesa; print('Mesa installed successfully!')"    checks to see if mesa installed

python model.py    this runs the code

## Configuration, Input Files, and Run-Time Limitations

### Configuration

The model uses a sensitivity parameter to control how strongly average trend scores influence individual users’ adjusted scores and overall trend averages.

### Input Files

The adapted model currently uses predefined user preferences within model.py, that can be adjusted by changing the values in the lines under the comment "Three users with scores from 0-3" . No external datasets or input files are required.

### Run-Time Limitations

* The simulation uses three predefined users.
* The model represents three content categories: Fitness, Cooking, and Gaming.
* User preferences are predefined rather than collected from real social media interactions.
* The simulation represents a simplified recommendation system rather than an actual social media platform.
