# Comparative Analysis of Reinforcement Learning Algorithms in MuJoCo Ant-v5

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Stable-Baselines3](https://img.shields.io/badge/Stable--Baselines3-RL-orange?style=for-the-badge)
![Gymnasium](https://img.shields.io/badge/Gymnasium-Ant--v5-green?style=for-the-badge)
![MuJoCo](https://img.shields.io/badge/MuJoCo-Physics%20Engine-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A comprehensive comparative study of four state-of-the-art Deep Reinforcement Learning algorithms—**PPO**, **DDPG**, **TD3**, and **SAC**—on the **MuJoCo Ant-v5** continuous control environment. The project evaluates each algorithm based on learning efficiency, stability, and locomotion performance over **2 million training timesteps**.

---

## Project Overview

Reinforcement Learning (RL) has become one of the most effective approaches for solving complex continuous control problems in robotics. This project presents a comparative analysis of four widely used Deep Reinforcement Learning algorithms—**Proximal Policy Optimization (PPO)**, **Deep Deterministic Policy Gradient (DDPG)**, **Twin Delayed Deep Deterministic Policy Gradient (TD3)**, and **Soft Actor-Critic (SAC)**—using the **MuJoCo Ant-v5** environment.

The objective is to train a quadrupedal robot (Ant) to learn an efficient and stable walking gait by maximizing cumulative rewards through interaction with the environment. Each algorithm is trained for **2 million timesteps** under the same conditions to ensure a fair comparison.

The study evaluates each algorithm based on:

- Learning performance
- Sample efficiency
- Stability during training
- Final cumulative reward
- Overall locomotion behavior

The project also includes an evaluation pipeline for comparing trained agents and analyzing their performance through quantitative metrics and reward visualizations.

---

## Key Features

- Comparative analysis of four Deep Reinforcement Learning algorithms.
- Training on the MuJoCo Ant-v5 continuous control benchmark.
- Performance comparison using standardized evaluation metrics.
- Reward analysis and algorithm performance visualization.
- Implementation using Stable-Baselines3 and Gymnasium.
- Focus on sample efficiency, stability, and learning behavior.
- Includes complete project documentation and experimental report.

---

## Algorithms Compared

The project evaluates the performance of four popular Deep Reinforcement Learning algorithms on the MuJoCo Ant-v5 environment.

| Algorithm | Category | Description |
|-----------|----------|-------------|
| **PPO (Proximal Policy Optimization)** | On-Policy | Uses a clipped surrogate objective to improve policy updates while maintaining training stability. |
| **DDPG (Deep Deterministic Policy Gradient)** | Off-Policy | Learns deterministic policies for continuous action spaces using actor-critic architecture. |
| **TD3 (Twin Delayed DDPG)** | Off-Policy | Improves DDPG by reducing overestimation bias using twin critics and delayed policy updates. |
| **SAC (Soft Actor-Critic)** | Off-Policy | Maximizes both cumulative reward and policy entropy, encouraging efficient exploration and robust learning. |

### Comparison Objectives

The algorithms are compared based on:

- Learning efficiency
- Average cumulative reward
- Maximum achieved reward
- Training stability
- Sample efficiency
- Overall locomotion performance

---

## Environment

The experiments were conducted using the **MuJoCo Ant-v5** environment from the **Gymnasium** reinforcement learning library.

### Environment Specifications

| Property | Value |
|----------|-------|
| Environment | Ant-v5 |
| Physics Engine | MuJoCo |
| Framework | Gymnasium |
| State Space | 27-dimensional observation vector |
| Action Space | 8-dimensional continuous actions |
| Episode Length | Up to 1000 steps |
| Training Timesteps | 2,000,000 |

### Reward Function

The environment rewards the agent for moving forward efficiently while maintaining a healthy posture and penalizes unnecessary control effort and excessive contact forces.

The reward can be expressed as:

```text
Reward = Forward Velocity + Healthy Reward − Control Cost − Contact Cost
```

### Objective

The primary objective is to train the Ant agent to learn a stable and efficient walking gait that maximizes cumulative reward while maintaining balance throughout each episode.

---

## Project Structure

```text
Comparative-Analysis-of-RL-Algorithms-in-MuJoCo-Ant-v5/
│
├── docs/
│   └── report.pdf
│
├── src/
│   └── antEnv.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

### Directory Overview

| Directory / File | Description |
|------------------|-------------|
| **docs/** | Contains the project report and supporting documentation. |
| **src/** | Contains the Python source code for training and experimentation. |
| **README.md** | Project documentation and setup guide. |
| **requirements.txt** | List of required Python packages. |
| **LICENSE** | MIT License for the project. |
| **.gitignore** | Specifies files and directories ignored by Git. |

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Subhra0309/Comparative-Analysis-of-RL-Algorithms-in-MuJoCo-Ant-v5.git

cd Comparative-Analysis-of-RL-Algorithms-in-MuJoCo-Ant-v5
```

### Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv environment

environment\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv environment

source environment/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training

After installing the required packages, run the training script.

```bash
python src/antEnv.py
```

The script initializes the MuJoCo Ant-v5 environment, trains the selected Reinforcement Learning algorithm, and saves the learned policy for evaluation.

> **Note:** Depending on your hardware configuration and selected algorithm, training for **2 million timesteps** may require several hours.

---

## Results

The performance of four Deep Reinforcement Learning algorithms was evaluated on the **MuJoCo Ant-v5** environment after training for **2,000,000 timesteps**.

The comparison focuses on:

- Average cumulative reward
- Maximum achieved reward
- Training stability
- Sample efficiency
- Overall locomotion performance

### Performance Comparison

| Algorithm | Mean Reward | Maximum Reward | Stability |
|-----------|------------:|---------------:|-----------|
| **DDPG** | **4210.33** | **4919.42** | Medium |
| **TD3** | 3950.15 | 4200.50 | High |
| **SAC** | 3800.21 | 4100.10 | High |
| **PPO** | 1650.45 | 1986.70 | Moderate |

### Key Observations

- **DDPG** achieved the highest reward but showed higher variance during training.
- **SAC** provided the best balance between performance and stability.
- **TD3** delivered consistently strong performance with stable convergence.
- **PPO** required more training timesteps to achieve competitive results.

---

## Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Reinforcement Learning | Stable-Baselines3 |
| Simulation Environment | Gymnasium |
| Physics Engine | MuJoCo |
| Numerical Computing | NumPy |
| Visualization | Matplotlib |
| Data Analysis | Pandas |

---

## Future Improvements

Possible extensions of this project include:

- Hyperparameter optimization for each RL algorithm.
- Training for longer durations (5M+ timesteps).
- Evaluation on additional MuJoCo environments such as Hopper-v5, Walker2d-v5, and HalfCheetah-v5.
- Integration with experiment tracking tools (TensorBoard or Weights & Biases).
- Comparative benchmarking on different hardware configurations.

---

## References

1. Gymnasium Documentation – Farama Foundation
2. MuJoCo Physics Engine
3. Stable-Baselines3 Documentation
4. Sutton, R. S., & Barto, A. G. *Reinforcement Learning: An Introduction* (2nd Edition)

---

## Author

**Subhrajit Jana**

M.Sc. in Computer Science                                         
Ramakrishna Mission Vivekananda Educational and Research Institute

GitHub: https://github.com/Subhra0309

Email: subhrajitjana2018@gmail.com

---

## License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more details.
