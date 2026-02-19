from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_best_flight(flight):
    price = flight["price"]["grandTotal"]
    segments = flight["itineraries"][0]["segments"]

    route = " -> ".join([s["departure"]["iataCode"] for s in segments])
    airlines = ",".join(set(s["carrierCode"] for s in segments))

    prompt = f"""
    Summarise this flight deal clearly for email:
    Route: {route}
    Airlines: {airlines}
    Total price: £{price}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=120
    )

    return response.choices[0].message.content