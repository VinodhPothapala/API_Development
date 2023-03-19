# Stock Returns Rest API
Build Rest API to obtain stock returns using IEX cloud. It contains get Returns method and Alpha method.
* Get return method  calculates the daily returns for the given dates.
* Get Alpha method calculates the alpha of the ticker and the benchmark over the time period requested.

## Technologies and frameworks:
* Python, flask, Swagger UI, Git 

## Installations:
* pip install flask_swagger_ui

## Project Structure:

caseStudy
    
    ├── src  
        ├── Configuration (yaml files)
    ├── test 
    └── README.md

 
## Instructions to test the API:
* Unzip and make sure it has two different folders (src and tests). 
* Run the configure.py file.
* URL for swagger: http://localhost:5009/stocksdata/ 
* Once you hit the URL, you will be displayed with Swagger UI which contains two Get Methods (Stock Returns and Stock Alpha).
* For testing API, click on any get method -> Click “Try it out” -> Enter the parameters -> click “Execute”
* Similarly try another method.

## Input Format:
* Ticker Symbol: String Format (Ex: AAPL)
* Benchmark: String format (Ex: MSFT)
* From Date: Date Format (Use YYYY-MM-YY)
* To Date: Date Format (Use YYYY-MM-YY)
## Response Format: 
* These methods return responses in JSON format.
* Response Body: { "closing": 125.07, "daily_return": -5.21, "date": "Tue, 03 Jan 2023 00:00:00 GMT", "opening": 130.28 }
* It will also return Error messages in HTML format in Swagger under the response body section.

## Exceptions Handling

|         Input        |     Exception Thrown    |
| ---------------------| ----------------------- |
| No stock data found  | Content Cell            |
| Future Date          | Content Cell            |
| Invalid input format | ValueError              | 
| Stock Data is Zero   | DivisionByZeroException |
| Invalid URL          | HTTPExceptions          |


## Limiting Rate: 
* According to IEX Client API response

## YouTube Link: https://youtu.be/USjHxSES4t8

#### Note: Generate IEX cloud token and copy it to the token.py file under configuration folder



