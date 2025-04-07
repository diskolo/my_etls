Using the real python fake jobs page i am going to:
1. Scrap the web page
2. Save the results in my datalake as raw data in the bronze area
3. Do some transformations on it reading from the datalake and writing again on it
4. read the data from the datalake and apply validations with pandera
5. take the data in the datalake and store it in my DW (fake postgresql)