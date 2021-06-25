# TODO: add sound support
import subprocess
import asyncio
from pathlib import Path


async def main():
  await asyncio.gather(twenty_twenty(), pomodoro())


async def twenty_twenty(n=1):
  while True:
    await pipe(20, minutes, asyncio.sleep)
    send_notification("Look away!")

    await pipe(20, seconds, asyncio.sleep)
    send_notification("You can look back now.")

    n += 1


async def pomodoro(cycles=2, n=1):
  while True:
    send_notification("Time to work!")
    await pipe(25, minutes, asyncio.sleep)

    if n % 4 == 0:
      send_notification("Long break!")
      await pipe(15, minutes, asyncio.sleep)
    else:
      send_notification("Small break!")
      await pipe(5, minutes, asyncio.sleep)

    if n == cycles * 4:
      send_notification("Pomodoro finished!")
      return

    n += 1


def pipe(n, *funcs):
  for f in funcs:
    n = f(n)
  return n


def send_notification(info):
  root = get_root_dir()
  icon = str(root.resolve()) + "/art/helpepper.png"
  command = f"notify-send 'Helpepper' '{info}' -i {icon}"
  subprocess.call(command, shell=True)


def get_root_dir():
  return Path(__file__).parent.parent


def seconds(n):
  return n


def minutes(n):
  return n * 60


if __name__ == '__main__':
  asyncio.run(main())
