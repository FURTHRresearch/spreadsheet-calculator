# Spreadsheet Evaluation Service

Run with 
```
docker compose build
docker compose up

docker build . -f Dockerfile -t furthrresearch/spreadsheet-calculator
docker push furthrresearch/spreadsheet-calculator    
```

By default the service is listing on port 5555. Modify the start.sh to change the port

## API
```
GET http://localhost/evaluate?spreadsheeturl=xyz&field=A1
ACCESS-KEY=asdf
```
Response body
```
{
    "result": "abc"
}
```