#!/usr/bin/env python3

from pathlib import Path
import subprocess
import time
import sys


def twenty_twenty(n=1):
    while True:
        # TODO: Different sound for this one
        time.sleep(minutes(20))
        send_notification("Look away!")
        play_sound("start_pomodoro.wav")
        time.sleep(20)
        play_sound("finish_pomodoro.wav")
        send_notification("You can look back now.")
        n += 1


def pomodoro(cycles=2):
    n = 1
    while True:
        play_sound("start_pomodoro.wav")

        send_notification("Time to work!")
        time.sleep(minutes(25))

        play_sound("finish_pomodoro.wav")

        if n % 4 == 0:
            send_notification("Long break!")
            time.sleep(minutes(15))
        else:
            send_notification("Small break!")
            time.sleep(minutes(5))

        if n == cycles * 4:
            send_notification("Pomodoro finished!")
            return

        n += 1


def play_sound(filename):
    file = f"{get_root_dir()}/sound/{filename}"
    command = f"play {file}"
    subprocess.Popen(command, shell=True,
                     stderr=subprocess.DEVNULL,
                     stdout=subprocess.DEVNULL)


def send_notification(info):
    root = get_root_dir()
    icon = str(root.resolve()) + "/art/helpepper.png"
    command = f"notify-send 'Helpepper' '{info}' -i {icon}"
    subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL)


def get_root_dir():
    return Path(__file__).parent


def minutes(n):
    return n * 60

if __name__ == '__main__':
    argv = sys.argv
    if argv[1] == 'pomo':
        pomodoro(int(argv[2]))
    elif argv[1] == '2020':
        twenty_twenty()

