import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleSquare(Node):

    def __init__(self):
        super().__init__('turtle_square')

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

    def move_forward(self):
        msg = Twist()
        msg.linear.x = 1.5
        msg.angular.z = 0.0

        for _ in range(20):
            self.publisher_.publish(msg)
            time.sleep(0.1)

        self.stop()

    def turn_left(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 1.57

        for _ in range(10):
            self.publisher_.publish(msg)
            time.sleep(0.1)

        self.stop()

    def stop(self):
        self.publisher_.publish(Twist())
        time.sleep(0.5)

    def draw_square(self):
        time.sleep(1)

        for side in range(4):
            print(f"Moving side {side + 1}")
            self.move_forward()

            print("Turning 90 degrees")
            self.turn_left()

        print("Square completed")


def main(args=None):
    rclpy.init(args=args)

    node = TurtleSquare()
    node.draw_square()

    node.destroy_node()
    rclpy.shutdown()


if name == '__main__':
    main()
