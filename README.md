# DS Med Cabinet 4 api
A datascience api for serving up cannabis strains to a webdev team.

## Usage
TODO: Update address when deployed to Heroku  
Send a `POST` request to `http://herokuplaceholder.com/send` with a json payload structured like this:
```Python
{
    "UserID": "dbkeyuser123", #db key for our user
    "Strain": "User_Strain", #Leave as User_Strain when POSTing to us
    "Type": "Sativa",
    "Rating": 0, #Leave as a zero when POSTing to us
    "Effects": "Uplifed, Happy, Relaxed, Energetic, Creative",
    "Flavor": "Spicy, Herbal, Sage, Woody",
    "Description": "a sativadominant hybrid bred in spain by medical seeds co the breeders claim to guard the secret genetics due to security reasons but regardless of its genetic heritage it is a thc powerhouse with a sweet and spicy bouquet subtle fruit flavors mix with an herbal musk to produce uplifting sativa effects one specific phenotype is noted for having a pungent odor that fills a room similar to burning incense"
}
```  
You will receive a response, structured exactly the same, with a details on our recommended strain.  In the response `Strain` will list the recommended strain name and `Rating` is an average user rating from our sourced dataset.

## Project structure
All data sets will live [here](https://github.com/BuildWeek-Med-Cabinet-4/DS/tree/master/data)  
All pickled models will live [here](https://github.com/BuildWeek-Med-Cabinet-4/DS/tree/master/models)  
All notebooks will live [here](https://github.com/BuildWeek-Med-Cabinet-4/DS/tree/master/notebooks)  
API lives [here](https://github.com/BuildWeek-Med-Cabinet-4/DS/tree/master/web_app)

## References
[Main Dataset](https://www.kaggle.com/kingburrito666/cannabis-strains)  
[Team Trello](https://trello.com/b/6fHmnowA/med-cabinet-4)  
[Git Workflow](https://www.notion.so/Git-Workflow-34f9b468dcf74a669aff0d3797870d37)  

### Curl commands for testing api
```sh
curl --location --request POST 'http://127.0.0.1:5000/send' \
--header 'Content-Type: application/json' \
--data-raw '{"UserID": "dbkeyuser123", 
"Strain": "User_Strain", 
"Type": "Sativa",
"Rating": 0, 
"Effects": "Uplifed, Happy, Relaxed, Energetic, Creative", 
"Flavor": "Spicy, Herbal, Sage, Woody", 
"Description": "a sativadominant hybrid bred in spain by medical seeds co the breeders claim to guard the secret genetics due to security reasons but regardless of its genetic heritage it is a thc powerhouse with a sweet and spicy bouquet subtle fruit flavors mix with an herbal musk to produce uplifting sativa effects one specific phenotype is noted for having a pungent odor that fills a room similar to burning incense"}'
```