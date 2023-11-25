document.addEventListener('DOMContentLoaded', function () {

    // Get the selected country dropdown element
    var countryDropdown = document.getElementById('countryDropdown');
    var yearDropdown = document.getElementById('yearDropdown');
    var yearDropdownCombined = document.getElementById('yearDropdownCombined');

    yearDropdownCombined.addEventListener('change',function(){
        var selectedYear = yearDropdownCombined.value;
        updateGraph('combinedGraph', plot_data_deaths_combined[selectedYear]);
    });

    // Get the card text elements
    var totalDeathText = document.getElementById('totalDeathText');

    // Set initial values based on the first country and first year
    updateCardData(countryDropdown.value, yearDropdown.value);

    // event listener for country dropdown change
    countryDropdown.addEventListener('change', function () {
        var selectedCountry = countryDropdown.value;
        var selectedYear = yearDropdown.value;
        updateCardData(selectedCountry, selectedYear);
    });

    // event listener for year dropdown change
    yearDropdown.addEventListener('change', function () {
        var selectedCountry = countryDropdown.value;
        var selectedYear = yearDropdown.value
        updateCardData(selectedCountry, selectedYear);
    });


    function updateCardData(selectedCountry, selectedYear) {
        // To find the selected country data in the countryData array
        var selectedCountryData = countryData.find(function (country) {
            return country.countryName === selectedCountry;
        });
        
        // to update the graphs based on the selected years
        updateGraph('countryGraph', selectedCountryData.plot_data_deaths[selectedYear]);

        // to update card text content
        totalDeathText.textContent = selectedCountryData.total_deaths;
        selectedCountryGraph.textContent = selectedCountryData.countryName;     
    }

    function updateGraph(graphId, plotData) {
        var graphElement = document.getElementById(graphId);
        graphElement.src = "data:image/png;base64," + plotData;
    }
});
