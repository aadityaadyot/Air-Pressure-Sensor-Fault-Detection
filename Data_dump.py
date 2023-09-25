import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/labDB")

Database_name = 'aps'
Collection_name = 'sensors'
data_file_path = "/config/workspace/aps_failure_training_set.csv"

if __name__ == "__main__":
    df = pd.read_csv(data_file_path)
    print(f"Rows and Columns : {df.shape}") 

    #convert dataframe to Json so that we can dump these record to the MongoDB
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])

    #insert coverted record into MongoDB
    
    client[Database_name][Collection_name].insert_many(json_record)