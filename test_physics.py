import unittest
from physics import Particle

class PhysicsTests(unittest.TestCase):
    def test_gravity(self):
        p = Particle(100, 100, 20, 0)
        p.step(0.5, 100, 960, 600)
        self.assertAlmostEqual(p.x, 110)
        self.assertAlmostEqual(p.y, 112.5)
        self.assertAlmostEqual(p.vy, 50)

    def test_zero_gravity(self):
        p = Particle(100, 100, 20, -10)
        p.step(1, 0, 960, 600)
        self.assertEqual((p.x, p.y), (120, 90))

    def test_floor_bounce(self):
        p = Particle(100, 585, 0, 100)
        p.step(0.1, 0, 960, 600)
        self.assertEqual(p.y, 590)
        self.assertEqual(p.vy, -75)

    def test_wall_bounce(self):
        p = Particle(15, 100, -100, 0)
        p.step(0.1, 0, 960, 600)
        self.assertEqual(p.x, 10)
        self.assertEqual(p.vx, 75)

if __name__ == "__main__":
    unittest.main()
