import random

def get_dad_jokes():
    return [

    "I'm afraid for the calendar. Its days are numbered.",
    "Why do fathers take an extra pair of socks when they go golfing? In case they get a hole in one!",
    "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
    "What do a tick and the Eiffel Tower have in common? They're both Paris sites.",
    "How do you follow Will Smith in the snow? You follow the fresh prints.",
    "If April showers bring May flowers, what do May flowers bring? Pilgrims.",
    "I only know 25 letters of the alphabet. I don't know y.",
    "What does a bee use to brush its hair? A honeycomb!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call fake spaghetti? An impasta!",
    "How does a penguin build its house? Igloos it together.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why couldn't the bicycle stand up by itself? It was two tired.",
    "What do you call an alligator in a vest? An investigator.",
    "Why did the math book look sad? Because it had too many problems.",
    "What do you call a factory that makes good products? A satisfactory.",
    "Why was the broom late? It swept in.",
    "What did the ocean say to the shore? Nothing, it just waved.",
    "Why don't some couples go to the gym? Because some relationships don't work out."
    "Why did the scarecrow become a successful neurosurgeon? He was outstanding in his field!",
    "Why don’t eggs tell jokes? They’d crack each other up.",
    "I don’t trust stairs because they’re always up to something.",
    "Why did the coffee file a police report? It got mugged.",
    "How does a snowman get around? By riding an ‘icicle.",
    "Why can’t you give Elsa a balloon? Because she will let it go.",
    "What’s orange and sounds like a parrot? A carrot!",
    "Why did the math book look sad? Because it had too many problems.",
    "How do you organize a space party? You planet.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "How many tickles does it take to make an octopus laugh? Ten-tickles.",
    "What do you call a pile of cats? A meowtain.",
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "How does a penguin build its house? Igloos it together.",
    "Why did the bicycle fall over? Because it was two-tired."]








def main():
    jokes = get_dad_jokes()
    while True:
        print("\nWelcome to the Dad Joke Simulator!")
        print("Press Enter to hear a dad joke or type 'exit' to quit.")
        user_input = input("Your choice: ").strip().lower()
        
        if user_input == 'exit':
            break
        
        joke = random.choice(jokes)
        print(f"\nHere's a dad joke for you: {joke}\n")
    
    print("Thanks for using the Dad Joke Simulator! Goodbye!")

if __name__ == "__main__":
    main()


