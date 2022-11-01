# Spreadsheet Evaluation Service

Run with 
```
docker compose build
docker compose up
```

## API
```
GET http://localhost/evaluate?spreadsheeturl=xyz&field=A1
ACCESS_KEY=asdf
```
Response body
```
{
    "result": "abc"
}
```