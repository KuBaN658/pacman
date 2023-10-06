import gymnasium as gym


env = gym.make("ALE/MsPacman-v5", render_mode='human')

observation, info = env.reset()

print(info, observation)

while True:
    try:
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    except KeyboardInterrupt:
        break


env.close()
