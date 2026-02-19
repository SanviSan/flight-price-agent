#!/bin/bash
set -x

cd /Users/sandeeppadmanabhan/Documents/Study/AI/AI_Agents/Flight_Search || exit 1

#Load env vars
export $(grep -v '^#' .env | xargs)

/Users/sandeeppadmanabhan/anaconda3/bin/python3 -m src.main >> flight_agent.log 2>&1
