##Data Exploration for DDL Incubator Group 4

##Team

Mason Unger - Statistics, Graphing, **Team Lead**

Nathan Danielsen -- Data Analysis, Model building and validation, and Django stuff

Jordan Lewis - Data wrangling, Database

Max Heiber - Front End, APIs, Scraping


##Problem Statement

Distill economic data from BLS and various public sources, combined with user input about income and spending to simply answer a simple question: 
 
“Can I make it in this city?”


###Research Questions

Can we make a prediction on if someone can 'make it' if they move to DC (or any other large city)?

What is making it in DC? Can we define making it or is it defined by user preferences?

Does 'making it' require a certain income threshold or budget breakdown for different locations (zip code, neighborhood) depending on the persons gross household income and/or household size?

Can we recommend or predict where the best place is for a person to live based on a combination of their resources, quality of life preferences and other information/ preferences?

What are the strongest dependant variables (ie. costs for housing, grocery or insurance; or perhaps walkability score?) that feed into 'making it' or not? 

Can we predict if 'making it' will change over time due to inflation or other changes in consumer prices?


###Hypothesis

I hypothesize that by using open data sources (open and user-given) and by using widely accepted models for 'making it', we will find that a ratio of housing price to net-income, cost/ease of the work commute, and ability to save are the greatest determinants of making it.    


###Value Proposition

We can give users a realistic picture of the total costs of living in a certain area and give them guidance on if they can make it or not - in short term and long term. 



###Strategy for Analysis

**For the DC Market:**

Segment - Divide and segment publically available consumer expenditure data into demographic groups (young singles under 25 and 25+, married without kids etc)

Location - Break down all data in DC by Ward, Zip code and/or neighboorhood

Machine Learning Applications - For microdata, unsupervised clustering approaches would interesting to pull out patters. 


**Output**

Attempt to create a model (min, mean, max) of consumer purchasing power by segment and location in DC 

With this model, can we complement this model with additional information to give users a more realistic understanding of 'can they make it'?



##Data Sources

**Seed Data**

Bureau of Labor Statistics Data
[Consumer Expenditure (CE) tabular data](http://www.bls.gov/cex/tables.htm)
[CE microdata](http://www.bls.gov/cex/pumdhome.htm)
[Component CPI price indexes by elementary item and area](http://www.bls.gov/cpi/data.htm)

[Guide for CE Survey Data in R](http://www.asdfree.com/search/label/consumer%20expenditure%20survey%20%28ce%29)

[Getting started with Consumer Expenditure Survey Public-Use Microdata](http://www.bls.gov/cex/pumd\_novice_guide.pdf)



Can we find more data out there on this?

**Complementary Data**

[Craigs List's Apartment Listings](http://washingtondc.craigslist.org/search/apa?)

[Zillow API](http://www.zillow.com/howto/api/APIOverview.htm)


**Data Feature Backlog**

Mint Intergration

##Budget Models
We should define 3 classes of "Making It" Budgets. Anything below the Min would be the danger zone for not making it.

"Min - Barely Making It"
[Frugal Budget](http://www.leavedebtbehind.com/frugal-living/budgeting/10-recommended-category-percentages-for-your-family-budget/)

"Mean - Making It"
[Young Adult Budget - Can Make it](http://www.forbes.com/2010/06/08/budgeting-young-adults-personal-finance-spending.html)

"Max - Got It Made"
[Where the poor and rich really spend their money](http://www.washingtonpost.com/blogs/wonkblog/wp/2015/04/14/where-the-poor-and-rich-spend-really-spend-their-money/)

*Links are illistrative for getting a sense of the budget models



##Already Invented Features (To refactor and not reinvent wheels)


###Craigslist

Craigslist Apartment Crawler
[Craig's List Apartment Crawler](https://github.com/Madrox/CraigsLister)

[craigsuck: A Craigslist RSS poller](https://github.com/jbrukh/craigsuck)


###Zillow API

[PyZillow](https://github.com/hanneshapke/pyzillow)



###Mint API
[a screen-scraping API for Mint.com](https://github.com/mrooney/mintapi)