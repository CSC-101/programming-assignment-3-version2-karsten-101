from data import CountyDemographics
from build_data import get_data


full_data = get_data()
reduced_data = [
    CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

# Part 1
# Returns the total population recorded in 2014 across all counties provided in the input list
# input: a list of CountyDemographics objects
# output: an int
def population_total(counties: list[CountyDemographics])-> int:
    pop = 0
    for i in counties:
        pop += i.population['2014 Population']
    return pop


# Part 2
# From a provided list of counties, returns a list of counties
# that are in a specified state.
# input: a list of CountyDemographics objects
# input: a state
# output: a list of CountyDemographics objects
def filter_by_state(counties: list[CountyDemographics], state: str)-> list[CountyDemographics]:
    result = [x for x in counties if x.state == state]
    return result


# Part 3
# Returns the total 2014 population of people with a specified level
# of education from a provided list of counties
# input: a list of counties
# input: a level of education
# output: a float
def population_by_education(counties: list[CountyDemographics], edu: str) -> float:
    pop = 0
    for i in counties:
        try:
            percent = i.education[edu]
            pop += i.population['2014 Population'] * (percent * (10**(-2)))
        except KeyError:
            pop = pop
    return pop

# Returns the total 2014 population of people with a specified ethnicity
# from a provided list of counties
# input: a list of counties
# input: an ethnicity
# output: a float
def population_by_ethnicity(counties: list[CountyDemographics], eth: str) -> float:
    pop = 0
    for i in counties:
        try:
            percent = i.ethnicities[eth] * (10**(-2))
            pop += i.population['2014 Population'] * percent
        except KeyError:
            pop = pop
    return pop

# Returns the total 2014 population of people below the poverty level
# in their county from a provided list of counties
# input: a list of counties
# output: a float
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    pop = 0
    for i in counties:
        percent = i.income['Persons Below Poverty Level'] * (10**(-2))
        pop += i.population['2014 Population'] * percent
    return pop


# Part 4
# Returns the percent of the total 2014 population that have achieved
# a specified level of education from a list of counties
# input: a list of counties
# input: an education level
# output: a float
def percent_by_education(counties: list[CountyDemographics], edu: str) -> float:
    tot_pop = population_total(counties)
    if tot_pop == 0:
        return 0
    else:
        edu_pop = population_by_education(counties, edu)
        return (edu_pop / tot_pop) * 100

# Returns the percent of the total 2014 population that identify as
# a specified ethnicity from a list of counties
# input: a list of counties
# input: an ethnicity group
# output: a float
def percent_by_ethnicity(counties: list[CountyDemographics], eth: str) -> float:
    tot_pop = population_total(counties)
    if tot_pop == 0:
        return 0
    else:
        eth_pop = population_by_ethnicity(counties, eth)
        return (eth_pop / tot_pop) * 100

# Returns the percent of the total 2014 population that are below the
# poverty level of their respective county from a list of counties
# input: a list of counties
# output: a float
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    tot_pop = population_total(counties)
    if tot_pop == 0:
        return 0
    else:
        pov_pop = population_below_poverty_level(counties)
        return (pov_pop / tot_pop) * 100


# Part 5
# From a provided list of counties, returns a list of counties
# that each have a percentage of a specified achieved education level
# above a specified threshold percentage.
# input: a list of CountyDemographics objects
# input: a level of education as a string
# input: a threshold percentage as a float
# output: a list of CountyDemographics objects
def education_greater_than(counties: list[CountyDemographics],
                           edu: str, thresh_perc: float)-> list[CountyDemographics]:
    result_lst = []
    for i in counties:
        try:
            edu_perc = i.education[edu]
            if edu_perc > thresh_perc:
                result_lst.append(i)
        except KeyError:
            thresh_perc = thresh_perc
    return result_lst

# From a provided list of counties, returns a list of counties
# that each have a percentage of a specified achieved education level
# below a specified threshold percentage.
# input: a list of CountyDemographics objects
# input: a level of education as a string
# input: a threshold percentage as a float
# output: a list of CountyDemographics objects
def education_less_than(counties: list[CountyDemographics],
                           edu: str, thresh_perc: float)-> list[CountyDemographics]:
    result_lst = []
    for i in counties:
        try:
            edu_perc = i.education[edu]
            if edu_perc < thresh_perc:
                result_lst.append(i)
        except KeyError:
            thresh_perc = thresh_perc
    return result_lst

# From a provided list of counties, returns a list of counties
# that each have a percentage of a specified ethnicity
# above a specified threshold percentage.
# input: a list of CountyDemographics objects
# input: an ethnicity as a string
# input: a threshold percentage as a float
# output: a list of CountyDemographics objects
def ethnicity_greater_than(counties: list[CountyDemographics],
                           eth: str, thresh_perc: float)-> list[CountyDemographics]:
    result_lst = []
    for i in counties:
        try:
            eth_perc = i.ethnicities[eth]
            if eth_perc > thresh_perc:
                result_lst.append(i)
        except KeyError:
            thresh_perc = thresh_perc
    return result_lst

# From a provided list of counties, returns a list of counties
# that each have a percentage of a specified ethnicity
# below a specified threshold percentage.
# input: a list of CountyDemographics objects
# input: an ethnicity as a string
# input: a threshold percentage as a float
# output: a list of CountyDemographics objects
def ethnicity_less_than(counties: list[CountyDemographics],
                           eth: str, thresh_perc: float)-> list[CountyDemographics]:
    result_lst = []
    for i in counties:
        try:
            eth_perc = i.ethnicities[eth]
            if eth_perc < thresh_perc:
                result_lst.append(i)
        except KeyError:
            thresh_perc = thresh_perc
    return result_lst

# From a provided list of counties, returns a list of counties
# that each have their percentage of those below the poverty level
# above a specified threshold percentage.
# input: a list of CountyDemographics objects
# input: a threshold percentage as a float
# output: a list of CountyDemographics objects
def below_poverty_level_greater_than(counties: list[CountyDemographics],
                                     thresh_perc: float)-> list[CountyDemographics]:
    result_lst = []
    for i in counties:
        pov_perc = i.income['Persons Below Poverty Level']
        if pov_perc > thresh_perc:
            result_lst.append(i)
    return result_lst

# From a provided list of counties, returns a list of counties
# that each have their percentage of those below the poverty level
# below a specified threshold percentage.
# input: a list of CountyDemographics objects
# input: a threshold percentage as a float
# output: a list of CountyDemographics objects
def below_poverty_level_less_than(counties: list[CountyDemographics],
                                     thresh_perc: float)-> list[CountyDemographics]:
    result_lst = []
    for i in counties:
        pov_perc = i.income['Persons Below Poverty Level']
        if pov_perc < thresh_perc:
            result_lst.append(i)
    return result_lst