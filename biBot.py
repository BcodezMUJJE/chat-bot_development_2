#!/usr/bin/python3

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create a ChatBot instance named 'BillBot'
chatbot = ChatBot('BillBot')

# Create a ChatterBotCorpusTrainer and train the chatbot on English language data
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.english")

# Create a ListTrainer and train the chatbot on a custom list of conversations
list_trainer = ListTrainer(chatbot)
list_trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You're welcome."
])
list_trainer.train([
    "How can I assist you with your fitness journey today?",
    "Hey! I'm looking to start working out. Any tips for a beginner?",
])
list_trainer.train([
    "Absolutely! Begin with light exercises like walking or jogging. Set realistic goals and gradually increase intensity.",
    "What about diet? Any suggestions for a balanced meal plan?",
])
list_trainer.train([
    "Sure thing! Focus on lean proteins, whole grains, and plenty of fruits and veggies. Stay hydrated too!",
    "I get bored easily. How do I make workouts more interesting?",
])
list_trainer.train([
    "Spice it up! Try different activities like cycling, swimming, or dance. Keep it fun to stay motivated.",
    "Dealing with sore muscles. Any quick relief tips?",
])
list_trainer.train([
    "Rest, ice, compression, and elevation (RICE) can help. Also, consider a warm bath and gentle stretches.",
    "How about staying motivated long-term?",
])
list_trainer.train([
    "Set clear, achievable goals, and celebrate your progress. Find a workout buddy for mutual motivation.",
    "Struggling with consistency. Any hacks to stay on track?",
])
list_trainer.train([
    "Schedule workouts like appointments. Mix up routines to prevent monotony. Small, consistent efforts make a big impact.",
    "What about recovery after intense workouts?",
])
list_trainer.train([
    "Prioritize rest! Sleep well, and consider activities like yoga or foam rolling to aid recovery.",
    "Are supplements necessary?",
])
list_trainer.train([
    "Not essential, but they can complement a balanced diet. Consult a nutritionist for personalized advice.",
    "How can I track my progress effectively?",
])
list_trainer.train([
    "Keep a fitness journal, use apps to log workouts, and track changes in strength, endurance, and overall well-being.",
    "I sometimes lose motivation. Any mental strategies?",
])
list_trainer.train([
    "Visualize your fitness goals, remind yourself of achievements, and surround yourself with positive influences.",
    "Balancing work and workouts is tough. Any time management tips?",
])
list_trainer.train([
    "Prioritize self-care. Schedule workouts during less busy periods, and focus on efficient, high-intensity workouts.",
    "What's the importance of warming up before exercising?",
])
list_trainer.train([
    "Warming up increases blood flow, flexibility, and reduces injury risk. Spend 5-10 minutes with dynamic stretches.",
    "How do I know if I'm overtraining?",
])
list_trainer.train([
    "Watch for signs like persistent fatigue, mood swings, and decreased performance. Allow time for recovery.",
    "What's your favorite workout?",
])
list_trainer.train([
    "I don't work out, but I love helping you achieve your fitness goals! What else can I assist you with?",
    "Thanks for the tips! Feeling motivated now.",
])
list_trainer.train([
    "You're welcome! Remember, progress, not perfection. Happy exercising!",
])

# Get a response from the chatbot
response = chatbot.get_response("Hello, how are you?")
print(response)

