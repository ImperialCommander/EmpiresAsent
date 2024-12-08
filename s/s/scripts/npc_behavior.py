import random

def npc_behavior():
    actions = ["patrol", "attack", "defend", "retreat"]
    action = random.choice(actions)
    print(f"NPC decides to: {action}")
    return action

if __name__ == "__main__":
    npc_behavior()
