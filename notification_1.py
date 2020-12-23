from plyer import notification
import time

if __name__ == "__main__":
    notification.notify(
             title="plz drink water",
             message="We believe that health information should be free to everyone and we rely on advertising to make this possible. Providing the best health information in the world is expensive.",
             # app_icon="PS C:\\python\\python notification\\glass.jfif",
             timeout=10
         )