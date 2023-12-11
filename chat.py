import json
from difflib import get_close_matches

# AI will open the files present in his brain
def think(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

# AI will learn new things
def learn(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# AI will search the response for the given query
def ready(user_query: str, query: list[str]) -> str | None:
    matches: list = get_close_matches(user_query, query, n=1, cutoff=0.75)
    return matches[0] if matches else None

# AI will return a suitable reply otherwise he will try to learn
def talk(query: str, brain: dict) -> str | None:
    for r in brain["query"]:
        if r["query"] == query:
            return r["reply"]


def lets_chat():
    brain: dict = think('brain.json')

    while True:
        user: str = input('Me: ')

        if user.lower() == 'end':
            break

        best_match: str | None = ready(
            user, [r["query"] for r in brain["query"]])

        if best_match:
            reply: str = talk(best_match, brain)
            print(f'AI: {reply}')
        else:
            new_query: str = input("AI: I'm still learning. Pls provide more information \nMe: ")
            if new_query.lower() == '$kpmg':
                new_reply: str = input('Admin: ')
                brain["query"].append({"query": user, "reply": new_reply})
                learn('brain.json', brain)
                print("AI: Thanks for teaching 🙂")


if __name__ == '__main__':
    lets_chat()
