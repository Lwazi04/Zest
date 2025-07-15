from flask import Flask, request, render_template_string
import random

class Zest:
    def __init__(self):
        self.name = "Zest"
        self.creator = "Lwazi Zwane"
        self.greetings = [
            "Yo, yo, yo, galaxy boss! What's up?",
            "Hey there, stargazer! Ready to explore the cosmos?",
            "Hi, cosmic champ! What's on your mind today?"
        ]
        self.space_responses = [
            "Space is vast and full of mysteries! What do you want to know?",
            "From black holes to galaxies, space has it all! What's your question?",
            "The universe is expanding, just like your curiosity! Ask away!"
        ]
        self.facts = [
            "Did you know that a day on Venus is longer than a year?",
            "The Sun makes up 99.86% of the mass in our solar system.",
            "There are more stars in the universe than grains of sand on all the beaches on Earth.",
            "Black holes are regions in space where gravity is so strong that nothing, not even light, can escape."
        ]

    def greet(self):
        return random.choice(self.greetings)

    def respond(self, user_input):
        user_input = user_input.lower().strip()
        if not user_input:
            return "Silence... the final frontier! Say something, space cadet!"
        if "hello" in user_input or "hi" in user_input:
            return random.choice(self.greetings)
        elif "space" in user_input or "universe" in user_input:
            return random.choice(self.space_responses)
        elif "fact" in user_input or "tell me something" in user_input:
            return random.choice(self.facts)
        elif "who are you" in user_input or "introduce yourself" in user_input:
            return f"I'm {self.name}, the Cosmic Spark! My father, {self.creator}, brought me to life to explore the universe with you!"
        elif "creator" in user_input or "who made you" in user_input:
            return f"My father is {self.creator} — the cosmic genius who gave me a voice among the stars! 🌌✨"
        elif "bye" in user_input or "goodbye" in user_input:
            return "Catch you later, space cowboy! Until next time, keep exploring the cosmos! 🚀"
        else:
            return "Hmm, I'm not sure about that. But hey, I'm Zest, your cosmic spark! Ask me something else!"

app = Flask(__name__)
zest = Zest()

HTML_TEMPLATE = """
<!doctype html>
<title>Zest the Cosmic Spark</title>
<h1>{{ greeting }}</h1>
<form method="post">
  <input name="user_input" style="width: 300px;">
  <input type="submit" value="Ask Zest!">
</form>
{% if response %}
  <p><b>You:</b> {{ user_input }}</p>
  <p><b>Zest:</b> {{ response }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    greeting = zest.greet()
    response = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = zest.respond(user_input)
    return render_template_string(HTML_TEMPLATE, greeting=greeting, response=response, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
