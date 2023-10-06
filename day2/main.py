import gymnasium as gym


env = gym.make("ALE/MsPacman-v5", render_mode='rgb_array')

print(env.action_space)

observation, info = env.reset()
print(len(observation), len(observation[0]), len(observation[0][0]))
