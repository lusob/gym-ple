gym-ple
******
OpenAI PLE environment.
PLE (PyGame Learning Environment) is a learning environment, mimicking the Arcade Learning Environment interface, allowing a quick start to Reinforcement Learning in Python. 
The goal of PLE is allow practitioners to focus design of models and experiments instead of environment design.
This package allows to use PLE as a gym environment.

Installing everything
---------------------
gym_ple requires PLE, to install PLE clone the repo and install with pip.

.. code:: shell

    git clone https://github.com/ntasfi/PyGame-Learning-Environment.git
    cd PyGame-Learning-Environment/
    pip install -e .


PLE requires PyGame installed:

On OSX:

.. code:: shell

    brew install sdl sdl_ttf sdl_image sdl_mixer portmidi  # brew or use equivalent means
    conda install -c tlatorre pygame=1.9.2 # using Anaconda

On Ubuntu 14.04:

.. code:: shell

    apt-get install -y python-pygame

More configurations and installation details on: http://www.pygame.org/wiki/GettingStarted#Pygame%20Installation

And finally clone and install this package

.. code:: shell

    git clone https://github.com/lusob/gym-ple.git 
    cd gym-ple/
    pip install -e .

You also can install it from PyPi:

.. code:: shell

    pip install gym_ple 


Example
=======

Run ``python example.py`` file to play a PLE game (flappybird) with a random_agent (you need to have installed openai gym).

