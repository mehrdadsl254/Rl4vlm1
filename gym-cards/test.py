
import matplotlib.pyplot as plt
import gymnasium as gym
import gym_cards
from text_wrapper import info_to_text_obs, text_projection

# env_name = 'gym_cards/NumberLine-v0'
# env = gym.make(env_name)
# obs, info = env.reset()
# plt.imshow(obs)
# text_obs = info_to_text_obs(env_name, info)
# print(info)
# print(text_obs)
# obs, reward, terminated, truncated, info = env.step(1)
# plt.imshow(obs)
# print(reward, terminated, truncated, info)
# act = text_projection(['"action": "+"'], env_name)
# obs, reward, terminated, truncated, info = env.step(act)
# plt.imshow(obs)
# print(reward, terminated, truncated, info)



env_name = 'gym_cards/EZPoints-v0'
env = gym.make(env_name)
# obs, info = env.reset()
# plt.imshow(obs)
# text_obs = info_to_text_obs(env_name, info)
# print(info)
# print(text_obs)
# obs, reward, terminated, truncated, info = env.step(4)
# plt.imshow(obs)
# text_obs = info_to_text_obs(env_name, info)
# print(reward, terminated, truncated, info)
# print(text_obs)