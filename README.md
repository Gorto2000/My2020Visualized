# My 2020 Visualized
My year 2020 compared to the years 2018 &amp; 2019: Biking, hiking, reading books

This repository shows my biking and hiking distances from 2018, 2019, and 2020. Additionally, 
I collected the numbers of non-fiction and fiction books I read in the same timeframe.

Brief process:
1. I collected the biking and hiking distances in BaseCamp ([Garmin](https://www.garmin.com/)). For the books, I have a long list of all books that I read in the last years. The data was just collected in a LibreOffice spreadsheet.
2. Out of the spreadsheet, I created simple CSV files for the three topics.
3. The CSV files were converted into JSON files with the help of self-written Python scripts to convert from the tabular format to the dataset format that [Chart.js](https://www.chartjs.org/) needs.
4. The JSON files were then copied into corresponding "dummy" HTML pages where Chart.js renders the diagrams.