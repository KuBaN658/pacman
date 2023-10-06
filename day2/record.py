import gymnasium as gym
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import datetime
import json


keys_to_action = {
    KeyCode.from_char('w'): 1,
    KeyCode.from_char('a'): 3,
    KeyCode.from_char('s'): 4,
    KeyCode.from_char('d'): 2
}

keys_pressed = {}


def on_press(key):
    keys_pressed[key] = True


def on_release(key):
    keys_pressed[key] = False


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()


env = gym.make("ALE/MsPacman-ram-v5", render_mode='human')

observation, info = env.reset()

saved_data = []

while not keys_pressed.get(Key.esc):
    observation, info = env.reset()
    observation, reward, terminated, truncated, info = env.step(0)

    while not terminated and not truncated:

        if keys_pressed.get(Key.esc):
            break

        action = 0
        for key in keys_to_action:
            if keys_pressed.get(key):
                action = keys_to_action[key]

        next_observation, reward, terminated, truncated, info = env.step(action)
        saved_data.append([[int(var) for var in observation], int(action)])
        observation = next_observation

print("[EXPERT RECORDER] Сохранение...")
filename = f'states/expert_{datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")}.txt'
with open(filename, 'w') as file:
    file.write(json.dumps(saved_data))
print(f"[EXPERT RECORDER] Сохранено в {filename}")
env.close()
