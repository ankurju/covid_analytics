import csv
from datetime import datetime

#utility function to gather deaths and cases data from csv
def process_deaths_cases_data(csv_file_path, countries):
    total_deaths_by_country_and_year = {}
    total_cases_by_country_and_year = {}
    overall_total_deaths_by_country={}
    overall_total_cases_by_country={}
    available_years = set()

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            date_str = row['date']
            country = row['location']
            total_deaths = float(row['total_deaths']) if row['total_deaths'] else 0.0
            total_cases = float(row['total_cases']) if row['total_cases'] else 0.0

            if country in countries:
                # Parse the date to get the month and year
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                year_key = date_obj.strftime('%Y')
                month_key = date_obj.strftime('%Y-%m')

                # Initialize the dictionary if it doesn't exist
                if country not in total_deaths_by_country_and_year:
                    total_deaths_by_country_and_year[country] = {}
                if country not in total_cases_by_country_and_year:
                    total_cases_by_country_and_year[country] = {}

                # Initialize the dictionary if it doesn't exist
                if country not in overall_total_deaths_by_country:
                    overall_total_deaths_by_country[country] = 0
                if country not in overall_total_cases_by_country:
                    overall_total_cases_by_country[country] = 0

                overall_total_cases_by_country[country] += total_cases
                overall_total_deaths_by_country[country] += total_deaths

                # Initialize the year dictionary if it doesn't exist
                if year_key not in total_deaths_by_country_and_year[country]:
                    total_deaths_by_country_and_year[country][year_key] = {}
                if year_key not in total_cases_by_country_and_year[country]:
                    total_cases_by_country_and_year[country][year_key] = {}

                # Update the total deaths for the specific month and year
                total_deaths_by_country_and_year[country][year_key][month_key] = \
                    total_deaths_by_country_and_year[country][year_key].get(month_key, 0) + total_deaths

                total_cases_by_country_and_year[country][year_key][month_key] = \
                    total_cases_by_country_and_year[country][year_key].get(month_key, 0) + total_cases

                available_years.add(year_key)

    return total_cases_by_country_and_year, total_deaths_by_country_and_year, list(available_years),overall_total_cases_by_country,overall_total_deaths_by_country

#utility function to gather vaccination data from csv
def process_vaccination_data(csv_file_path,countries):
    total_vaccinations_by_country_and_year = {}
    overall_total_vaccinations_by_country={}
    available_years = set()

    with open(csv_file_path,"r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            date_str = row['date']
            country = row['location']
            total_vaccinations = float(row['daily_vaccinations']) if row['daily_vaccinations'] else 0.0

            if country in countries:
                # Parse the date to get the month and year
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                year_key = date_obj.strftime('%Y')
                month_key = date_obj.strftime('%Y-%m')

                # Initialize the dictionary if it doesn't exist
                if country not in total_vaccinations_by_country_and_year:
                    total_vaccinations_by_country_and_year[country] = {}

                 # Initialize the dictionary if it doesn't exist
                if country not in overall_total_vaccinations_by_country:
                    overall_total_vaccinations_by_country[country] = 0

                overall_total_vaccinations_by_country[country] += total_vaccinations

                if year_key not in total_vaccinations_by_country_and_year[country]:
                    total_vaccinations_by_country_and_year[country][year_key] = {}

                # Update the total vaccination for the specific month and year
                total_vaccinations_by_country_and_year[country][year_key][month_key] = \
                    total_vaccinations_by_country_and_year[country][year_key].get(month_key, 0) + total_vaccinations

                available_years.add(year_key)

    return total_vaccinations_by_country_and_year,overall_total_vaccinations_by_country,list(available_years)

#utility function to gather hospitalisation data from csv
def process_hospitalization_data(csv_file_path,countries):
    total_hospitalizations_by_country_and_year = {}
    overall_total_hospitalization_by_country={}
    available_years = set()

    with open(csv_file_path,"r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['indicator'] != "Daily ICU occupancy per million":
                date_str = row['date']
                country = row['entity']
                total_hospitalizations = float(row['value']) if row['value'] else 0.0

                if country in countries:
                    # Parse the date to get the month and year
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                    year_key = date_obj.strftime('%Y')
                    month_key = date_obj.strftime('%Y-%m')

                    # Initialize the dictionary if it doesn't exist
                    if country not in total_hospitalizations_by_country_and_year:
                        total_hospitalizations_by_country_and_year[country] = {}

                    # Initialize the dictionary if it doesn't exist
                    if country not in overall_total_hospitalization_by_country:
                        overall_total_hospitalization_by_country[country] = 0

                    overall_total_hospitalization_by_country[country] += total_hospitalizations

                    if year_key not in total_hospitalizations_by_country_and_year[country]:
                        total_hospitalizations_by_country_and_year[country][year_key] = {}

                    # Update the total hospitalization for the specific month and year
                    total_hospitalizations_by_country_and_year[country][year_key][month_key] = \
                        total_hospitalizations_by_country_and_year[country][year_key].get(month_key, 0) + total_hospitalizations

                    available_years.add(year_key)

    return total_hospitalizations_by_country_and_year,overall_total_hospitalization_by_country,list(available_years)

