# DS Med Cabinet 4 api
A simple datascience api that receives user inputs as a json payload, processes that payload using a natural language processing model, and returns a recommended cannabis strain as a json object.

## Usage
### Base URL
https://medicabi.herokuapp.com
### POST */send*
Takes a json object containing user inputs, and returns a json object with recommended strain.

#### Request:
```JSON
{
    "UserID": "dbkeyuser123",
    "Strain": "User_strain", 
    "Type": "Sativa",
    "Effects": "Happy, energetic, and creative", 
    "Flavor": "Sour, fruity, pineapple, citrus", 
    "Description": "I'm bummed most the time.  I'm just looking to feel good, and keep my creative juices flowing. I'm an artist and I find some herb helps my art."
}
```  

#### Response:
```JSON
{
    "UserID": "dbkeyuser123",
    "Strain": "Golden-Pineapple",
    "Type": "hybrid",
    "Effects": "Happy,Euphoric,Uplifted,Relaxed,Creative",
    "Flavor": "Pineapple,Tropical,Citrus",
    "Description": "Golden Pineapple is a hybrid cross between Golden Goat and Pineapple Kush that delivers creative, uplifting effects with a fruity, tropical flavor. Its aroma is remarkably similar to sour pineapple, providing a flavorful escape from stress, anxiety, and depression. Golden Pineapple’s engaged, active effects will give you the energy you need to keep going throughout your day, although in larger doses, it can be difficult to direct that focus effectively."
}
```

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
curl --location --request POST 'https://medicabi.herokuapp.com/send' \
--header 'Content-Type: application/json' \
--data-raw '{"UserID": "dbkeyuser123",
"Strain": "User_strain", 
"Type": "Sativa",
"Effects": "Happy, energetic, and creative", 
"Flavor": "Sour, fruity, pineapple, citrus", 
"Description": "I'\''m bummed most the time.  I'\''m just looking to feel good, and keep my creative juices flowing. I'\''m an artist and I find some herb helps my art."}'
```