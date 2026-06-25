import gymnasium as gym
import numpy as np
import time

# --- Configuration ---
# 'Ant-v5' is the latest standard MuJoCo Ant environment in Gymnasium
ENVIRONMENT_ID = "Ant-v5"
RENDER_MODE = "human"  # Use "human" to display a window, or "rgb_array" for recording

# --- 1. Initialize the Environment ---
try:
    # We pass render_mode to the make function to enable visualization
    env = gym.make(ENVIRONMENT_ID, render_mode=RENDER_MODE)
    print(f"Successfully created environment: {ENVIRONMENT_ID}")
except Exception as e:
    print(f"Error creating environment. Did you install 'gymnasium[mujoco]'? Error: {e}")
    exit()

# Print environment details
print(f"Observation Space Shape: {env.observation_space.shape}")
print(f"Action Space Shape: {env.action_space.shape}")
print(f"Action Space High: {env.action_space.high}")
print(f"Action Space Low: {env.action_space.low}")

# --- 2. Run a Sample Episode ---
MAX_STEPS = 50000
total_reward = 0
step_count = 0

# Reset the environment to start a new episode
# obs is the initial observation, info contains diagnostic/debugging info
observation, info = env.reset(seed=42)

done = False
while not done and step_count < MAX_STEPS:
    # 1. Select an Action: Use a random action for this example
    # The action space is a continuous vector, e.g., for Ant, it's 8 values between -1.0 and 1.0
    action = env.action_space.sample() 
    
    # 2. Step the Environment: Apply the action
    # The step method returns 5 values (the new standard for Gymnasium):
    # observation, reward, terminated, truncated, info
    observation, reward, terminated, truncated, info = env.step(action)
    
    # Check if the episode is over (either terminated or truncated)
    done = terminated or truncated

    total_reward += reward
    step_count += 1
    
    # 3. Render (Visualize) the environment
    # The 'human' render mode automatically updates the window on each step
    if RENDER_MODE == "human":
        # Introduce a small delay to make the visualization observable
        time.sleep(env.metadata["render_fps"] / 1000.0)

# --- 3. Cleanup ---
env.close()

print("-" * 30)
print(f"Episode finished after {step_count} steps.")
print(f"Total Reward: {total_reward:.2f}")