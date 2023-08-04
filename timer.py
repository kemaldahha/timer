from plyer import notification
import time


def start_timer(minutes):
    t_start = time.time()
    while True:
        time.sleep(1)
        seconds_elapsed = int(time.time() - t_start)
        print(
            f"{minutes - (seconds_elapsed // 60 + 1):02.0f}:{60-seconds_elapsed}",
            end="\r",
        )
        if seconds_elapsed > minutes * 60:
            break
    notification.notify(title="Timer", message="Time's up!", timeout=5)


if __name__ == "__main__":
    limit_minutes = int(input("minutes: "))
    start_timer(limit_minutes)
