#echo Starting Rasa NLU...
#rasa run -p 18888 --enable-api --cors "*"
echo Starting Rasa Action...
rabbit run actions -p 18889
echo Done.