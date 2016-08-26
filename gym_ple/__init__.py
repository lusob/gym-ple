from gym.envs.registration import registry, register, make, spec
from gym_ple.ple_env import PLEEnv
# Pygame
# ----------------------------------------
for game in ['Catcher', 'MonsterKong', 'FlappyBird', 'PixelCopter', 'PuckWorld', 'RaycastMaze', 'Snake', 'WaterWorld']:
    nondeterministic = False
    register(
        id='{}-v0'.format(game),
        entry_point='gym_ple:PLEEnv',
        kwargs={'game_name': game},
        timestep_limit=10000,
        nondeterministic=nondeterministic,
    )
