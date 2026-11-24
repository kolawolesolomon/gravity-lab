# Gravity Lab

An interactive 2D projectile sandbox built with Python and Pygame. Explore gravity, launch velocity, trajectories and boundary bounces.

## Run locally

```sh
python -m pip install -r requirements.txt
python main.py
```

## Controls

- Drag and release the left mouse button to launch a particle opposite the drag direction.
- Up/Down: adjust gravity.
- R: clear particles.
- Escape: quit.

The simulation uses pixel-based units, simplified boundary collisions and independent particles, not a full rigid-body physics engine. The physics module is separate from rendering for testability.

Status: initial implementation; graphical and automated testing pending.
