from src.flight_search import search_flights
from src.ai_reasoning import explain_best_flight
from src.emailer import send_email

def run_agent():
    flight = search_flights()
    summary = explain_best_flight(flight)
    send_email(summary)

if __name__ == "__main__":
    run_agent()