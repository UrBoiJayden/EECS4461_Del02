# EECS4461_Del02
## Project Overview
A Mesa-based computational model based on the Schelling Segregation model for exploring how individual feedback and collective trend scores influence content rankings in a simplified Instagram-style recommendation system.

The model includes three categories: Fitness, Cooking, and Gaming. It uses three simulated users with different preferences to calculate individual and overall trend scores.

The project investigates how changing the sensitivity of the recommendation system affects user preferences and the overall ranking of trends.

## Model Description

Users

* Represent simulated social media users.
* Each user has preferences for Fitness, Cooking, and Gaming.
* Preferences are represented using values from 0 to 3.
* Each preference is converted into a personal trend score.

Trends

* Represent the three content categories: Fitness, Cooking, and Gaming.
* Each trend calculates the personal scores associated with that category across all users.
* The average personal score is calculated for each trend.
* The recommendation system’s sensitivity is applied to calculate adjusted scores.
