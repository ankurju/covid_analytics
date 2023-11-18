import csv
from datetime import datetime


def process_data(csv_file_path,countries_of_interest):
    total_deaths_by_country_and_month = {}
    total_cases_by_country_and_month = {}
    available_years = set()
    
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            date_str = row['date']
            country = row['location']
            total_deaths = float(row['total_deaths']) if row['total_deaths'] else 0.0
            total_cases = float(row['total_cases']) if row['total_cases'] else 0.0

            if country in countries_of_interest:
                # Parse the date to get the month
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                year_key = date_obj.strftime('%Y')
                month_key = date_obj.strftime('%Y-%m')

                # Initialize the dictionary if it doesn't exist
                if country not in total_deaths_by_country_and_month:
                    total_deaths_by_country_and_month[country] = {}
                if country not in total_cases_by_country_and_month:
                    total_cases_by_country_and_month[country] = {}

                # Update the total deaths for the specific month
                total_deaths_by_country_and_month[country][month_key] = \
                    total_deaths_by_country_and_month[country].get(month_key, 0) + total_deaths
                
                total_cases_by_country_and_month[country][month_key] = \
                    total_cases_by_country_and_month[country].get(month_key,0) + total_cases
                
                available_years.add(year_key)

    return total_cases_by_country_and_month , total_deaths_by_country_and_month ,list(available_years)
# Print the results
# for country, monthly_data in total_deaths_by_country_and_month.items():
#     print(f"{country}:")
#     for month, total_deaths in monthly_data.items():
#         print(f"  {month}: {total_deaths}")


# for country, monthly_data in total_cases_by_country_and_month.items():
#     print(f"{country}:")
#     for month, total_cases in monthly_data.items():
#         print(f"  {month}: {total_cases}")




# with open("../../static/data/covid-hospitalizations.csv") as csv_file2:
#     reader = csv.DictReader(csv_file2)
#     header = reader.fieldnames
#     print(header)


# with open("../../static/data/excess_mortality.csv") as csv_file3:
#     reader = csv.DictReader(csv_file3)
#     header = reader.fieldnames
#     print(header)