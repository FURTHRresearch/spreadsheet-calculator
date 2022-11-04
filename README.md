# Spreadsheet Evaluation Service

Run with 
```
docker compose build
docker compose up
```

By default the service is listing on port 5555. Modify the start.sh to change the port

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