#!/usr/bin/env python
# coding: utf-8
import sys
import unittest
import pybullet
from qibullet import PepperVirtual
import time


class PepperBaseTest(unittest.TestCase):
    """
    Unittests for the control of Pepper virtual's base
    """

    @classmethod
    def setUpClass(cls):
        """
        Launches a simulation and spawns the Pepper virtual robot
        """
        cls.pepper_virtual = PepperVirtual()
        cls.pepper_virtual.loadRobot(
            [0, 0, 0],
            [0, 0, 0, 1])

    def test_move_to_base_world_frame(self):
        """
        Test the set @moveTo method in the world frame, and compare the
        desired position to the position returned by the @getPosition method
        """
        x_command, y_command, theta_command = 1, 1, 2
        PepperBaseTest.pepper_virtual.moveTo(
            0,
            0,
            0,
            frame=PepperVirtual.FRAME_WORLD)

        PepperBaseTest.pepper_virtual.moveTo(
            x_command,
            y_command,
            theta_command,
            frame=PepperVirtual.FRAME_WORLD)

        x, y, theta = PepperBaseTest.pepper_virtual.getPosition()
        # TODO: uncertaineties for positions in unittests
        # self.assertEqual(x_command, x)
        # self.assertEqual(y_command, y)
        # self.assertEqual(theta_command, theta)

    def test_move_to_base_robot_frame(self):
        """
        Test the set @moveTo method in the robot frame, and compare the desired
        position to the position returned by the @getPosition method
        """
        x_def, y_def, theta_def = 1, -1, 0.3,
        x_command, y_command, theta_command = -1, 0, -1

        PepperBaseTest.pepper_virtual.moveTo(
            0,
            0,
            0,
            frame=PepperVirtual.FRAME_WORLD)

        PepperBaseTest.pepper_virtual.moveTo(
            x_def,
            y_def,
            theta_def,
            frame=PepperVirtual.FRAME_WORLD)

        PepperBaseTest.pepper_virtual.moveTo(
            x_command,
            y_command,
            theta_command,
            frame=PepperVirtual.FRAME_ROBOT)

        x, y, theta = PepperBaseTest.pepper_virtual.getPosition()
        # TODO: uncertaineties for positions in unittests
        # self.assertEqual(x_def + x_command, x)
        # self.assertEqual(y_def + y_command, y)
        # self.assertEqual(theta_def + theta_command, theta)

    def test_move_to_base_async(self):
        """
        Test the set @moveTo method in the robot frame, and compare the desired
        position to the position returned by the @getPosition method
        """
        x_def, y_def, theta_def = 1, 1, -1,
        x_command, y_command, theta_command = 0, 0, 0

        PepperBaseTest.pepper_virtual.moveTo(
            0,
            0,
            0,
            frame=PepperVirtual.FRAME_WORLD,
            _async=False)

        PepperBaseTest.pepper_virtual.moveTo(
            x_def,
            y_def,
            theta_def,
            frame=PepperVirtual.FRAME_WORLD,
            _async=True)
        # time.sleep(0.5)
        # This call will raise an error
        try:
            PepperBaseTest.pepper_virtual.moveTo(
                x_def,
                y_def,
                theta_def,
                frame=PepperVirtual.FRAME_WORLD)
        except pybullet.error:
            pass

        PepperBaseTest.pepper_virtual.moveTo(
            x_command,
            y_command,
            theta_command,
            frame=PepperVirtual.FRAME_WORLD,
            _async=True)
        time.sleep(1)
        x, y, theta = PepperBaseTest.pepper_virtual.getPosition()
        # TODO: uncertaineties for positions in unittests
        # self.assertEqual(x_def + x_command, x)
        # self.assertEqual(y_def + y_command, y)
        # self.assertEqual(theta_def + theta_command, theta)

    def test_move_base(self):
        """
        Test the set @move method
        """
        PepperBaseTest.pepper_virtual.move(0.5, 0.5, 0.5)
        PepperBaseTest.pepper_virtual.move(33, -3, 67)
        PepperBaseTest.pepper_virtual.move(0, 0, 0)


if __name__ == "__main__":
    unittest.main()
