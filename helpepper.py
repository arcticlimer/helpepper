#!/usr/bin/env python3

from pathlib import Path
import subprocess
import asyncio


async def main():
    await asyncio.gather(twenty_twenty(), pomodoro())


async def twenty_twenty(n=1):
    while True:
        # TODO: Different sound for this one
        await asyncio.sleep(minutes(20))
        send_notification("Look away!")
        play_sound("start_pomodoro.wav")
        await asyncio.sleep(20)
        play_sound("finish_pomodoro.wav")
        send_notification("You can look back now.")
        n += 1


async def pomodoro(cycles=2, n=1):
    while True:
        play_sound("start_pomodoro.wav")

        send_notification("Time to work!")
        await asyncio.sleep(minutes(25))

        play_sound("finish_pomodoro.wav")

        if n % 4 == 0:
            send_notification("Long break!")
            await asyncio.sleep(minutes(15))
        else:
            send_notification("Small break!")
            await asyncio.sleep(minutes(5))

        if n == cycles * 4:
            send_notification("Pomodoro finished!")
            return

        n += 1


def pipe(n, *funcs):
    for f in funcs:
        n = f(n)
        return n


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
    return Path(__file__).parent.parent


def minutes(n):
    return n * 60


if __name__ == '__main__':
    asyncio.run(main())
