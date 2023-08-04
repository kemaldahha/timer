from plyer import notification
import time


def start_timer(minutes):
    t_start = time.time()
    while True:
        time.sleep(1)
        seconds_elapsed = int(time.time() - t_start)
        minutes_remaining, seconds_remaining = divmod(
            minutes * 60 - seconds_elapsed, 60
        )
        print(
            f"{minutes_remaining:02}:{seconds_remaining:02}",
            end="\r",
        )
        if seconds_elapsed > minutes * 60:
            break
    notification.notify(title="Timer", message="Time's up!", timeout=5)


if __name__ == "__main__":
    limit_minutes = int(input("minutes: "))
    start_timer(limit_minutes)
