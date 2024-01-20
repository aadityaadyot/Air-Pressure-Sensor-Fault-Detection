import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/labDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set.csv"
DATABASE_NAME= "aps-air-pressure-sensor"
COLLECTION_NAME= "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns, {df.shape}")

    #convert dataframe to json so that we can dump these record in mongodb
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    #print(json_record[0])

# below line is used to load the json data into the database mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)