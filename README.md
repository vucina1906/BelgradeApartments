- Project idea was to built Selenium Scraper of dynamic website, collect data in usable format (csv or excel) and later analyse data using Tableau or pandas,matplotlib and seaborn in Jupiternotebook.

- First to use Scraper.py script you have to download Google Chrome browser and accurate chromedriver version. Versions must be same. Check your Google Chrome version and for example if your version is 114.0.5735.199 you should download chromedriver version 114.0.5735. Also in stall exact version of selenium from requirements.txt file. I had a problems with newest version of selenium and its compatibility with newest chromedriver version. 

- After you scrape webpage (range 1 to 101 becuase website has 100 pages) script will save data in csv format. Than you can analyse data in notebook (my notebook add in project) and also train a model on collected data. You can also use script convertor.py to convert it to excel file and connect to Tableau for analysis and visualization (everything added in project repository). 

- User Setup.py file to install requirements.txt

    - Project Update

- Automatic Selenium added (new script AutomaticScraper.py). You can chose how often do you want script to run, for example in script is every day at 11:32 morning. Cron is a time-based job scheduling syntax that consists of five fields: minute, hour, day of the month, month, and day of the week so you can chose your options.

- Also requirements.txt added becuase for automatic scraper you need to install APScheduler package 

- Each time AutomaticScraper run and create excel file it will overwrite existing one that is already connected to Tableau (so you will have fresh data on Dashboard), you just need to refresh datasource in each sheet (see image Refresh in repository).
