from chatterbot import ChatBot as Bot
from chatterbot.trainers import ListTrainer as Train

# Create bot
b = Bot('ChaiBot', 
       read_only=True,
       logic_adapters=[{
           'import_path': 'chatterbot.logic.BestMatch',
           'default_response': 'Ask: menu, where, time or call',
           'maximum_similarity_threshold': 0.7
       }])

# Train bot
t = Train(b)
t.train([
    ["hi", "Hello! Welcome to Chai Wala, Narhe."],
    ["hello", "Hi! What do you need?"],
    ["what do you sell", "We sell:\n- Tea (Rs 10)\n- Coffee (Rs 15)\n- Vada Pav (Rs 15)\n- Burger (Rs 40)"],
    ["tea", "We have:\n1. Regular (Rs 10)\n2. Masala (Rs 15)\n3. Ginger (Rs 15)"],
    ["coffee", "Hot Coffee: Rs 15\nCold Coffee: Rs 25"],
    ["food", "Quick snacks:\n- Vada Pav (Rs 15)\n- Bhel (Rs 40)\n- Samosa (Rs 15)"],
    ["where are you", "We are at:\nShop 5, SITS Road, Narhe, Pune 411041"],
    ["address", "Shop 5, SITS Road, Narhe"],
    ["time", "Open daily 7 AM to 10 PM"],
    ["open", "7 AM to 10 PM every day"],
    ["contact", "Call us: 96XXXXXX69"],
    ["help", "Call owner: 96XXXXXX69"],
    ["bye", "Thanks! Visit us!"],
    ["exit", "Goodbye! Come again!"]
])

# Simple chat loop
print("ChaiBot ready! Type 'bye' to exit")

while True:
    u = input("You: ").lower()
    
    if u in ["bye", "exit"]:
        print("ChaiBot: Thanks! Visit us at SITS Road!")
        break
        
    r = b.get_response(u)
    print("ChaiBot:", r)