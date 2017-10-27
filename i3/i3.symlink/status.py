"""This file configures the statusline shown i3 bar."""
from i3pystatus import Status
from i3pystatus.core.command import run_through_shell

COLOR_GOOD = "#859900"
COLOR_DEGRADED = "#b58900"
COLOR_NEUTRAL = "#ffffff"
COLOR_BAD = "#dc322f"

status = Status()

# Date / Clock
# Tue 30.10l 14:59:46 KW31
status.register("clock",
    format="%a %-d.%m. %H:%M:%S KW%V",)

# Battery
status.register("battery",
    format="[{status} ]{consumption:.1f} W [{percentage:.0f} %] {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "▼",
        "CHR": "▲",
        "FULL": "",
    },
    full_color=COLOR_GOOD,
    critical_color=COLOR_BAD,
    charging_color=COLOR_GOOD,
    )

# System load
status.register("load",
    critical_color=COLOR_BAD)

# CPU usage
status.register("cpu_usage")

# CPU Temperature
status.register("temp",
        format="{temp:.0f} °C",)

# CPU frequency
status.register("cpu_freq",
    format="{avgg} GHz",)

# Wired network
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="enp0s25",
    format_up="{v4cidr}",
    format_down="{interface}:",
    color_up=COLOR_GOOD,
    color_down=COLOR_BAD)

# Wireless network
# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interface="wlp3s0",
    format_up="{essid} {quality:2.0f} % {v4cidr} {kbs} kiB/s",
    format_down="{interface}: ",
    dynamic_color=False,
    color_up=COLOR_GOOD,
    color_down=COLOR_BAD)

# Shows disk usage of /
status.register("disk",
    path="/",
    format="{avail:.1f} GiB",
    critical_color=COLOR_BAD,
    )

status.register("mem",
        format="{avail_mem:.1f} GiB",
        divisor=1073741824,
        color=COLOR_GOOD,
        warn_color=COLOR_DEGRADED,
        alert_color=COLOR_BAD)

# Sound volume
status.register("alsa",
        format="{volume} %")

def backlight_up():
    run_through_shell(["xbacklight", "-inc", 10])

def backlight_down():
    run_through_shell(["xbacklight", "-dec", 10])

# Backlight
status.register("backlight",
        format="{percentage} %",
        base_path="/sys/class/backlight/intel_backlight/",
        on_leftclick=backlight_up,
        on_rightclick=backlight_down)


status.run()
