import random
responses={
    "hey":["hlo","hi there!","hey! how are you?"],
    "hlo":["hlo","hi there!","hey! how are you?"],
    "hi":["hlo","hi there!","hey! how are you?"],
    "how are you":["i am good! how about you?","i am doing great", "i am fine! how about you?"],
    "bye":["goodbye!","see you later!","take care!"],
    "oky":["ok!","yeah!"],
    "good":["that's great to hear!","awesome!"],
    "name":["i am a friend bot!","i am your friend!","i am a chatbot! created by jagriti!"],
    "help":["i can chat with you!","i can be your friend!","i can talk about various topics!"],
}
default_responses=["i am not sure how to respond to that.",
                   "can you tell me more?","that's interesting!",
                   "i see!",
                   "let's talk about something else!",
                   "i'm here to listen!",
                   "sorry, i don't understand that."]
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(default_responses)
print("Welcome to the chatbot! Type 'bye' to end the conversation.")
while True:    
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)