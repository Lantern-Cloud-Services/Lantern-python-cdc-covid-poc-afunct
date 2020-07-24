import logging
import requests
import json
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Retrieving data')

    cdc_endpoint = os.environ.get('cdc_endpoint')
    cdc_dataset  = os.environ.get('cdc_dataset')
    cdc_apptoken = os.environ.get('cdc_apptoken')


    result = requests.get(cdc_endpoint + cdc_dataset, headers={"$$app_token": cdc_apptoken})
    result_obj_arr = json.loads(result.content)
    for result in result_obj_arr:
        state = result.get('state', "unknown state")
        sex = result.get('sex', "unknown sex")
        age   = result.get('age_group', "unknown age")
        cdeaths = result.get('covid_19_deaths', "0")
        
        logging.warn(state + " - " + sex + "/" + age + "/" + cdeaths)
       

    return func.HttpResponse("Data retreived")
