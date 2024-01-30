import gym

env = gym.make("Taxi-v3").env

# Initialize the environment
env.reset()  # Add this line before the first render call

# Now you can render the environment
env.render()

epochs = 0
penalties, reward = 0, 0

frames = [] # for animation

done = False

while not done:
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

    if reward == -10:
        penalties += 1
    
    # Put each rendered frame into dict for animation
    frames.append({
        'frame': env.render(mode='ansi'),
        'state': state,
        'action': action,
        'reward': reward
        }
    )

    epochs += 1

# Render the final state after the episode is done
env.render()
print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))
