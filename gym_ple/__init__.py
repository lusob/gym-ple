from gym.envs.registration import registry, register, make, spec
from gym_ple.ple_env import PLEEnv
# Pygame
# ----------------------------------------
'''
for game in ['Tetris']:
    for obs_type in ['image']:
        nondeterministic = False
        register(
            id='{}-v0'.format(game),
            entry_point='gym_ple.envs.pygame:TetrisEnv',
            kwargs={},
            timestep_limit=10000,
            nondeterministic=nondeterministic,
        )

'''

for game in ['Catcher', 'MonsterKong', 'FlappyBird', 'PixelCopter', 'PuckWorld', 'RaycastMaze', 'Snake', 'WaterWorld']:
    for obs_type in ['image']:
        nondeterministic = False
        register(
            id='{}-v0'.format(game),
            entry_point='gym_ple:PLEEnv',
            kwargs={'game_name': game, 'obs_type': obs_type},
            timestep_limit=10000,
            nondeterministic=nondeterministic,
        )
