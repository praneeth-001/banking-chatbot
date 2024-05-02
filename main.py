from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper
import exp_cat

app = FastAPI()




@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "service.balance-context: ongoing-service":
        return account_balance(parameters)

    elif intent == "service.card - context: ongoing-card" :
        return card_status(parameters)

    elif intent == "expense.categorise-context: ongoing-classification" :
        return classify_spending(parameters)



def account_balance(parameters: dict):
    acc_number = parameters['number']
    balance= db_helper.get_account_balance(acc_number)

    if balance:
        fulfillment_text = f"The account balance for account number: {acc_number} is {balance}"
    else:
        fulfillment_text = f"please enter a valid account number"


    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

def card_status(parameters: dict):
    acc_number = parameters['number']
    status = db_helper.get_card_status(acc_number)


    fulfillment_text = f"hey your card is blocked now. apply for a new card to avail our services for {acc_number}"
    # else:
    #     fulfillment_text = f"please enter a valid account number"
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

def classify_spending(parameters: dict):
    acc_number = parameters['number']

    table_data = exp_cat.get_classification(acc_number)
    paragraph = " ".join([row['TRANSACTION_DETAILS'] for row in rows])
    fulfillment_text = f"{paragraph}"
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


