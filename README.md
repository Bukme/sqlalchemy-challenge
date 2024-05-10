# SQLAlchemy Challenge

This project is a SQLAlchemy challenge focused on analyzing climate data in Hawaii. The project involves querying and analyzing a SQLite database containing weather data. The analysis includes exploratory data analysis (EDA) and building a Flask API to expose the analysis results.

## Project Overview

The project is divided into two main parts:

1. **Exploratory Data Analysis (EDA)**: In this part, we use SQLAlchemy to analyze climate data stored in a SQLite database. The analysis includes:

   - Finding the most recent date in the dataset.
   - Retrieving the last 12 months of precipitation data and plotting the results.
   - Calculating summary statistics for precipitation data.
   - Performing station analysis to find the total number of stations and the most active stations.
   - Analyzing temperature data for the most active station, including finding the lowest, highest, and average temperatures, and plotting a histogram of temperature observations.

2. **Flask API Development**: In this part, we create a Flask API to expose the climate analysis results as JSON objects. The API provides the following endpoints:

   - `/api/v1.0/precipitation`: Returns a JSON representation of the last 12 months of precipitation data.
   - `/api/v1.0/stations`: Returns a JSON list of weather stations.
   - `/api/v1.0/tobs`: Returns a JSON representation of the temperature observations (tobs) for the most active station for the last 12 months.
   - `/api/v1.0/start_date`: Returns a JSON list of the minimum, maximum, and average temperatures for all dates greater than or equal to the given start date (in the format YYYY-MM-DD).
   - `/api/v1.0/start_date/end_date`: Returns a JSON list of the minimum, maximum, and average temperatures for dates between the given start and end dates (in the format YYYY-MM-DD).

## Files Included

- **Resources/**: Directory containing the SQLite database (`hawaii.sqlite`) used for analysis.
- **climate_analysis.ipynb**: Jupyter Notebook containing the SQLAlchemy analysis code.
- **app.py**: Python script containing the Flask API code.

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- Flask
- SQLAlchemy
- Pandas
- Matplotlib

## Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/SQLAlchemy-Challenge.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SQLAlchemy-Challenge
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask API:

   ```bash
   python app.py
   ```

5. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the landing page and explore the available routes.

## Author

[Bukola Fatile]

## Acknowledgements

The climate data used in this project is provided by the University of Oregon and is available through the following link: [Hawaii Climate Database](https://www.earthchem.org/science/observing-geochemical-properties/geochemical-data). Special thanks to the University of Oregon for providing this dataset.


### References
Creating the app.py file. CloudxLab. (n.d.). https://cloudxlab.com/assessment/displayslide/5947/creating-the-apppy-file 
Grinberg, M. (n.d.). The Flask mega-tutorial, part I: Hello, world!. miguelgrinberg.com. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world 

YouTube. (2022, August 18). How to create a simple flask app in just 5 minutes | python flask tutorial for beginners. YouTube. https://www.youtube.com/watch?v=6M3LzGmIAso 

YouTube. (2023, April 5). Orm | advantages and disadvantages of Orm | Object relational mapper| sqlalchemy Orm Crud Operations. YouTube. https://www.youtube.com/watch?v=7036aOaxhXA 



Other resourceful ideas gotten from office hours, other students, slack and tutor.
