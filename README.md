- Project idea was to built Selenium Scraper of dynamic website, collect data in usable format (csv or excel) and later analyse data using Tableau or pandas,matplotlib and seaborn in Jupiternotebook.

- First to use Scraper.py script you have to download Google Chrome browser and accurate chromedriver version. Versions must be same. Check your Google Chrome version and for example if your version is 114.0.5735.199 you should download chromedriver version 114.0.5735. Also in stall exact version of selenium from requirements.txt file. I had a problems with newest version of selenium and its compatibility with newest chromedriver version. 

- After you scrape webpage script will save data in csv format. Than you can analyse data in notebook (my notebook add in project) and also train a model on collected data. You can also use script convertor.py to convert it to excel file and connect to Tableau for analysis and visualization (everything added in project repository). 

- User Setup.py file to install requirements.txt