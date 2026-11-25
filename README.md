# Gravity Lab

[![Tests](https://github.com/kolawolesolomon/gravity-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/kolawolesolomon/gravity-lab/actions/workflows/tests.yml)

A Python and Pygame sandbox for experimenting with 2D projectile motion. Launch particles, adjust gravity and observe trajectories and boundary bounces. Simulation code lives in `physics.py` and is independent of Pygame.

## Setup and use

Use Python 3.12 and run the following commands from the repository root.

```sh
python -m pip install -r requirements.txt
python main.py
```

- Drag and release the left mouse button to launch a particle opposite the drag direction.
- Press Up or Down to change gravity. The lower limit is zero.
- Press R to clear particles or Escape to quit.

## Tests

```sh
python -m unittest -v
python -m py_compile main.py physics.py
python smoke_render.py
```

The physics suite covers acceleration, zero gravity and boundary bounces. The SDL dummy-display check exercises Pygame startup, mouse launching, gravity controls, trail drawing and reset. It captures a rendered frame in `gravity-lab.png`.

## Limitations

The simulation uses pixel units, simplified boundary collisions and independent particles. It does not simulate collisions between particles.

## Screenshot

Open the latest successful [Actions run](https://github.com/kolawolesolomon/gravity-lab/actions/workflows/tests.yml) and download `gravity-lab-preview` from **Artifacts** to see a screenshot captured from the running application.
