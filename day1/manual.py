import gymnasium as gym
from gymnasium.utils.play import play


env = gym.make("ALE/MsPacman-v5", render_mode='rgb_array')

play(env, zoom=4, keys_to_action={
    'w': 1, 's': 4, 'a': 3, 'd': 2, 'q': 7, 'z': 8, 'r': 5, 'f': 7
})
