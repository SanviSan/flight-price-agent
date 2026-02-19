from langchain.openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model = "gpt-4.1-mini",
    temperature = 0.2
)

PROMPT = ChatPromptTemplate.from_template("""
You are a flight comparison expert.
                                          
Below are multiple return flight options from London to Bangalore.
Each option includes price, duration,, stops and  nights at destination.

Your task:
 1. Decide which option is the BEST VALUE
 2. Clearly explain WHY it is better than the others
 3. Be concise and practical (like advise to a real traveller)  

Flights:
{flights}

Return a short explaination in English                                                                                                                                                                                                          
""")

def explain_best_flight(flights):
    """
    flights: list of dicts (top-ranked flights)
    """
    formatted = []

    for i,f in enumerate(flights,i):
        formatted.append(
            f"""
            Option {i}:
            Price: £{f['price']}
            Total Duration: {f['duration']['total']//3600} hours
            Stops: {len(f['route']) - 2}
            Nights in Bangalore: {f['nightsInDest']}
            """
        )

    prompt = PROMPT.format(flights = "\n".join(formatted))
    response = llm.invoke(prompt)
    return response.content

