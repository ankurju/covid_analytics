document.addEventListener('DOMContentLoaded', function () {
    // Get the selected country dropdown element
    var countryDropdown = document.getElementById('countryDropdown');
    var yearDropdown1 = document.getElementById('yearDropdown1');
    var yearDropdown2 = document.getElementById('yearDropdown2');

    // Get the card text elements
    var totalDeathsText = document.getElementById('totalDeathsText');
    var totalVaccinatedText = document.getElementById('totalVaccinatedText');
    var totalHospitalizationsText = document.getElementById('totalHospitalizationsText');

    // Set initial values based on the first country and first year
    updateCardData(countryDropdown.value, yearDropdown1.value, yearDropdown2.value);

    // event listener for country dropdown change
    countryDropdown.addEventListener('change', function () {
        var selectedCountry = countryDropdown.value;
        var selectedYear1 = yearDropdown1.value;
        var selectedYear2 = yearDropdown2.value;
        updateCardData(selectedCountry, selectedYear1, selectedYear2);
    });

    // event listener for year dropdown change
    yearDropdown1.addEventListener('change', function () {
        var selectedCountry = countryDropdown.value;
        var selectedYear1 = yearDropdown1.value;
        var selectedYear2 = yearDropdown2.value;
        updateCardData(selectedCountry, selectedYear1, selectedYear2);
    });

    yearDropdown2.addEventListener('change', function () {
        var selectedCountry = countryDropdown.value;
        var selectedYear1 = yearDropdown1.value;
        var selectedYear2 = yearDropdown2.value;
        updateCardData(selectedCountry, selectedYear1, selectedYear2);
    });

    function updateCardData(selectedCountry, selectedYear1, selectedYear2) {
        // To find the selected country data in the countryData array
        var selectedCountryData = countryData.find(function (country) {
            return country.countryName === selectedCountry;
        });

        // to update the graphs based on the selected years
        updateGraph('countryGraph1', selectedCountryData.plot_data_cases, selectedYear1);
        updateGraph('countryGraph2', selectedCountryData.plot_data_deaths, selectedYear2);

        // to update card text content
        totalDeathsText.textContent = 'Total Deaths: ' + selectedCountryData.total_deaths;
        totalVaccinatedText.textContent = 'Total Vaccinated: ' + selectedCountryData.total_vaccinated;
        totalHospitalizationsText.textContent = 'Total Hospitalizations: ' + selectedCountryData.total_hospitalizations;
    }

    function updateGraph(graphId, plotData, selectedYear) {
        var graphElement = document.getElementById(graphId);
        graphElement.src = "data:image/png;base64," + plotData;
    }
});